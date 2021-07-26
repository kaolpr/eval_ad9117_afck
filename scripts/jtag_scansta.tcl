#set JTAG */xilinx_tcf/Xilinx/*
set JTAG */xilinx_tcf/Digilent/*

catch open_hw
catch {connect_hw_server -url localhost:3121}
get_hw_targets
current_hw_target [get_hw_targets $JTAG]
set_property PARAM.FREQUENCY 3000000 [get_hw_targets $JTAG]
catch {open_hw_target -jtag_mode 1}

run_state_hw_jtag reset
run_state_hw_jtag idle
scan_ir_hw_jtag 8 -tdi 00
scan_ir_hw_jtag 8 -tdi a0
scan_ir_hw_jtag 8 -tdi a5
scan_dr_hw_jtag 8 -tdi 5a
scan_ir_hw_jtag 8 -tdi c3
#On proper setup last step should return 0x00
scan_dr_hw_jtag 8 -tdi 5a -tdo 00
close_hw_target
open_hw_target
