#!/bin/sh


## Create & Map Libraries
v.7

# Compile modules
vcom -check_synthesis -work minimips_rtl src/pack_mips.vhd \
 src/my_package.vhd \
 src/alu.vhd \
 src/bus_ctrl.vhd \
 src/pps_di.vhd \
 src/pps_ex.vhd \
 src/pps_pf.vhd \
 src/renvoi.vhd \
 src/banc.vhd \
 src/pps_ei.vhd \
 src/pps_mem.vhd \
 src/predict.vhd \
 src/syscop.vhd \
 src/minimips.vhd \
 src/ram.vhd \
 src/rom.vhd \
 src/bench_minimips.vhd
