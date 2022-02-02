import sys
from gcode import *
from Interperter import Interperter
import os

def do_line(line):
    try:
        g = GCode.parse_line(line)

        return g
    except:
            print('ERROR ' + str(sys.exec_info()[0]))

def main():
    program = []

    try:
        # TESTING
        file = '../test.nc'

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)

        # END TESTING

        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                print('> ' + line)
                program.append(do_line(line))

            print ('\n-----------------------\n')
            if len(program) > 0:
                i = Interperter(program)

                for new_line in i.parse_program():
                    print (new_line)

                
    except KeyboardInterrupt as e:
        pass


if __name__ == '__main__':
    main()