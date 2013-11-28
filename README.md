# VPyLife 

A 3D Visual Python implementation of Conway's Game of Life.

By default the rule of life is '23/3', the environment size is 10, and the life
seed is the current system time. 

Rules are in the notation '{S}/{B}' where {S} is a string containing a list of numbers to determine how many adjacent cells are necessary for a cell to survive, and {B} is a string containing a list of numbers to determine how many adjacent cells are necessary to be born (activate).

The environment size is a single positive integer which determines the volume of the cubic ecosystem. 

Cells show age by changing color slowly from green to brown the longer they remain active.

*Note: If for some reason when you run it the rendering panel doesn't appear, just keep restarting until it does. I have yet to figure out why it does that.*

----------


Visit the [Wiki](https://github.com/Aurenos/VPyLife/wiki) for screenshots and a list of good parameter sets.


----------

#### Requirements

VPyLife requires VPython-wx (VPython 6.05) and Python 2.7.5.