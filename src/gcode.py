"""
Inspiration for this class was dirrived from PyCNC's gcode.py class
https://github.com/Nikolay-Kha/PyCNC/blob/master/cnc/gcode.py
"""

import re

# extract letter-digit pairs
g_pattern = re.compile('([A-Z])([-+]?[0-9.]+)')
# white spaces and comments start with ';' and in '()'
clean_pattern = re.compile('\s+|\(.*?\)|;.*')

class GCode(object):
    # represents a single line of GCode

    def __init__(self, params, raw_line):
        self.params = params
        self.raw_line = raw_line
    
    def has(self, arg_name):
        # see if argument value is present
        return arg_name in self.params
    
    def get(self, arg_name, default=None):
        ## get the value of an argument
        if arg_name not in self.params:
            return default
        return float(self.params[arg_name])
    
    def get_raw(self):
        return self.raw_line
    
    def coordinates(self, default):
        # get X, Y, and Z values as object

        x = self.get('X', default)
        y = self.get('Y', default)
        z = self.get('Z', default)
        e = self.get('E', default)

        return x, y, z, e
    
    def has_coordinates(self):
        # see if at least one coordinate exists in a command
        return 'X' in self.params or 'Y' in self.params or 'Z' in self.params \
            or 'E' in self.params

    def command(self):
        if 'G' in self.params:
            return 'G' + self.params['G']
        if 'M' in self.params:
            return 'M' + self.params['M']
        if 'O' in self.params:
            return 'O' + self.params['O']

    @staticmethod
    def parse_line(line):
        line = line.upper()
        line = re.sub(clean_pattern, '', line)

        if len(line) == 0:
            return None
        if line[0] == '%':
            return None
        
        m = g_pattern.findall(line)

        if not m:
            # ERROR: G CODE NOT FOUND
            print('ERROR: GCODE NOT FOUND')
        if len(''.join(["%s%s" % i for i in m])) != len(line):
            # ERROR: EXTRA CHARACTER IN LINE
            print('ERROR: EXTRA CHARACTER IN LINE')

        params = dict(m)

        # this should go away. this is very common.
        # EX: HAAS Safe startup:
        # G00 G90 G40 G49 G54 
        if len(params) != len(m):
            print('ERROR: DUPLICATE CODE ENTRIES')
        if 'G' in params and 'M' in params:
                print('ERROR: G AND M CODE FOUND')
        return GCode(params, line)