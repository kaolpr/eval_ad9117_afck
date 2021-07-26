from migen import *
import numpy as np


class Generator(Module):

    def __init__(self, nsamples=100, nbits=14, type="sine", phase=0):

        self.out = Signal(nbits)

        # # #

        if type == "sine":
            float_samples = 0.5*(np.sin(np.linspace(0, 2*np.pi, num=nsamples, endpoint=False)+phase) + 1)
        elif type == "ramp":
            float_samples = np.linspace(0, 1, num=nsamples, endpoint=False)
        float_samples = np.round((2**nbits-1)*float_samples)
        samples = [int(x) for x in float_samples]

        samples_array = Array(samples)
        self.address = address = Signal(max=nsamples)

        self.sync += [
            self.out.eq(samples_array[address]),
            If(address < nsamples, address.eq(address+1)).Else(address.eq(0))
        ]


if __name__ == "__main__":
    dut = SineGenerator()

    def testbench():
        for i in range(200):
            yield
    
    run_simulation(dut, testbench(), vcd_name="sine_generator.vcd")