from migen import *
from migen.genlib.io import CRG, DDROutput, DifferentialOutput
from migen.build.platforms.afck1v1 import Platform
from migen.build.generic_platform import *
from gateware.generator import Generator
import numpy as np
from modules.ELHEP_Cores.elhep_cores.cores.xilinx_ila import add_xilinx_ila, ILAProbe


class Top(Module):

    def __init__(self):
        self.platform = Platform()
        self.add_extension()

        # fpga_clk will be sys clock
        fpga_clk = self.platform.request("fpga_clk")
        self.submodules.crg = CRG(fpga_clk)
        self.platform.add_period_constraint(fpga_clk.p, 8.0)
        
        self.submodules.igen = Generator(type="sine", phase=0)
        self.submodules.qgen = Generator(type="sine", phase=np.pi/2)

        self.data = self.platform.request("data")
        for i in range(len(self.data)):
            self.specials += DDROutput(self.igen.out[i], self.qgen.out[i], self.data[i])
        self.clkout = self.platform.request("dataclk_port")
        self.comb += self.clkout.eq(ClockSignal())

        self.submodules += [
            ILAProbe(self.igen.address),
            ILAProbe(self.qgen.address),
            ILAProbe(self.igen.out),
            ILAProbe(self.qgen.out)
        ]
        add_xilinx_ila(self, self.crg.cd_sys.clk, "build/")

    def add_extension(self):
        ios = [
            ("dataclk_port", 0, Pins("fmc1:LA04_P"), IOStandard("LVCMOS25")),
            ("data", 0, Pins(
                "fmc1:LA02_P",  # db0
                "fmc1:LA03_P",  # db1
                "fmc1:LA06_P",  # db2
                "fmc1:LA08_P",  # db3
                "fmc1:LA07_P",  # db4
                "fmc1:LA10_P",  # db5
                "fmc1:LA05_P",  # db6
                "fmc1:LA12_P",  # db7
                "fmc1:LA11_P",  # db8
                "fmc1:LA13_P",  # db9
                "fmc1:LA09_P",  # db10
                "fmc1:LA16_P",  # db11
                "fmc1:LA14_P",  # db12
                "fmc1:LA15_P"), # db13
                IOStandard("LVCMOS25")
            )
        ]
        self.platform.add_extension(ios)

    def build(self, *args, **kwargs):
        self.platform.build(self, *args, **kwargs)



if __name__ == "__main__":
    top = Top()
    top.finalize()
    top.build(run=True, build_dir="build/gateware")





