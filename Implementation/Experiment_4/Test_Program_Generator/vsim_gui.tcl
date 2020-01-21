
# run the simulation
vsim -vopt -coverage -voptargs="+acc" minimips_rtl.sim_minimips(bench)

# show waveforms
source wave.do

# START VCD file generation

#vcd dumpports /sim_minimips/u_minimips/* -file dumpports_rtl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:* -file dumpports_rtl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u1_pf:* -file dumpports_pf.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u3_di:* -file dumpports_di.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u4_ex:* -file dumpports_ex.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u6_renvoi:* -file dumpports_renvoi.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u7_banc:* -file dumpports_banc.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u8_syscop:* -file dumpports_syscop.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u9_bus_ctrl:* -file dumpports_bus_ctrl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u10_predict:* -file dumpports_predict.vcd

# create an event to stop the simulation
when -label end_of_simulation {end_sim == '1'} {
	echo "End of simulation"
	vcd dumpportsflush
	quit -f
	#stop
}

# run the simulation
run 50 ms
#quit -f
