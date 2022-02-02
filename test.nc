%
(SAMPLE G12)
T1 M06 (Select tool 1) ;
G00 G90 G40 G49 G54 (Safe startup) ;
G00 X0 Y0 (Rapid to 1st position) ;
S1000 M03 (Spindle on CW) ;
G43 H01 Z0.1 (Tool offset 1 on) ;
M08 (Coolant on) ;
( Cut the circle ) ;
G12 I0.75 F10. Z-1.2 D01 (Finish pocket CW) ;
G00 Z0.1 (Retract) ;
G00 Z0.1 M09 (Rapid retract, Coolant off) ;
G53 G49 Z0 M05 (Z home, Spindle off) ;
G53 Y0 (Y home) ;
M30 (End program) ;
%