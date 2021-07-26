# AD9117 DPG2-EBZ Devkit @ AFCK v1.1

This repository contains a demonstration project for 
[AD9117 devkit ](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9117.html)
connected to [AFCK v1.1] FMC carrier board with AD-DAC-FMC-ADP adapter.

It is assumed that DCLKIO is connected together with CLKIN, so devkit clock tree 
is essentially not used.

Designed for 125 MHz clocking from `fpga_clk`.

This simplistic project generates a sine waves shifted by pi/4 at I/Q outputs. Period is 100 samples long, what results in output 
frequency of 1.25 MHz.

## Building

```
PYTHONPATH="$(pwd)/modules/migen:$PYTHONPATH" python3 ./gateware/top.py
```