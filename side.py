from keithley2600 import Keithley2600, ResultTable
import numpy as np
import pathlib
import sys
k = Keithley2600('TCPIP::192.168.1.11::INSTR')
rt = ResultTable(params={'sweep_type': 'iv'})
stp = float(sys.argv[2])
sweeplistPos = np.arange(
    0, float(sys.argv[1]) + stp, stp
    )
sweeplistNeg = np.arange(
    0, -float(sys.argv[1]) - stp, -stp
    )
sweeplist = np.append(np.arrange(-float(sys.argv[1]), float(sys.argv[1]) + stp, stp), np.flip(np.arrange(-float(sys.argv[1]), float(sys.argv[1]) + stp, stp)))
v, i = k.voltage_sweep_single_smu(
    k.smua, sweeplist, t_int=float(sys.argv[3]), delay=-1, pulsed=False
)
rt.append_column(v, 'Voltage', 'V')
rt.append_column(i, 'Current', 'A')
rt.plot(live=False)
rt.save(pathlib.Path(pathlib.Path(__file__).parent, input("File name and relative path: ")))
if input("Do you want to exit? [y/n]") == 'y':
    quit()
while True:
    rt = ResultTable(params={'sweep_type': 'iv'})
    range, stp, t = map(float, input("Enter range(V), step(V), time(s) separated by space: ").split())
    sweeplistPos = np.arange(
        0, range + stp, stp
        )
    sweeplistNeg = np.arange(
        0, -range - stp, -stp
        )
    sweeplist = np.append(np.append(sweeplistPos, np.flip(sweeplistPos)), np.append(sweeplistNeg, np.flip(sweeplistNeg)))
    v, i = k.voltage_sweep_single_smu(
        k.smua, sweeplist, t_int=t, delay=-1, pulsed=False
    )
    rt.append_column(v, 'Voltage', 'V')
    rt.append_column(i, 'Current', 'A')
    rt.plot(live=False)
    rt.save(pathlib.Path(pathlib.Path(__file__).parent, input("File name and relative path: ")))
    if input("Do you want to exit? [y/n]") == 'y':
        quit()    