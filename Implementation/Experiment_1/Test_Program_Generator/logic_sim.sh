#!/bin/sh

./compile_tst.sh || { echo "COMPILE ERROR." ; exit 1; }

vsim -do vsim_gui.tcl || { echo "LOGIC SIMULATION ERROR." ; exit 1; }
