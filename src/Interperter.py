from enums import *

class Interperter():
    coordinate_system = Coordinate_System.ABSOLUTE
    unit_system = UNITS.IMPERIAL



    def __init__(self, nc_program):
        # nc_program is a collection of GCode lines
        self.program = nc_program

    

    def _parse_g_code_line(self, gcode):
        if gcode is None:
            return ''

        if gcode.command() is None:
            return f'--NO COMMAND-- ({gcode.get_raw()})'
        
        print('Interpertating command ' + gcode.command())

        c = gcode.command()

        if c.startswith('O'):
            return f'Program Name is {c}'
        elif c == 'G0':
            if gcode.has_coordinates():
                cords = gcode.coordinates(0)
                return f'Rapid Move to {cords[0]}, {cords[1]}, {cords[2]}, {cords[3]}'
            else:
                return 'Rapid move to home' # THIS MIGHT BE WRONG
    
    def parse_program(self):
        result = [] # this will be the english-ified version of each line

        for line in self.program:
            result.append(self._parse_g_code_line(line))

        return result