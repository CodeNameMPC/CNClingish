# CNClingish
CNClingish is a utility that will take CNC G and M code and convert it to English statements that are easier to read

## About
I recently started a new position at work that requires working with CNC G and M code for HAAS Mills and Lathes. This is a training position and I am coming in blind. Since I have programming background, my first task was to take a piece of code used for out mill and figure out what it does and make necessary improvements.

G and M code is not easy to understand for a first time user, it doesn't read like normal code, it is just a series if commands starting with G or M with other arguments and that's it.

```
G01 X1 Y1 Z0
```

That code tells the lathe to move to (1, 1, 0). Not intuative unless you have all those G and M codes.

The goal of CNClingish is to take the hard-to-read G and M code and make it read more like a sentence.

```
G01 X1 Y1 Z0 > "Move to (1,1,0)
```