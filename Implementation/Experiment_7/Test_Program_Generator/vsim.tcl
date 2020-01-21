
# run the simulation

vsim -vopt -coverage -voptargs="+acc" minimips_rtl.sim_minimips(bench)

# START VCD file generation

#vcd dumpports sim_minimips/u_minimips/* -file dumpports_rtl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:* -file dumpports_rtl.vcd

# create an event to stop the simulation

when -label end_of_simulation {end_sim == '1'} {
	echo "End of simulation"
	vcd dumpportsflush
	quit -f
}

# run the simulation

run 100 ms
quit -f
