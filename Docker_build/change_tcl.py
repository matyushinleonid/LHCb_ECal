import sys
import os
from pathlib import Path

logs_path = Path(os.environ['LOGS_DIR'])
input_file = logs_path / "input.txt"
if not input_file.exists:
	raise Exception("No input file {}". format(logs_path / "input.txt"))

with open(input_file, "r") as f:
	param1, param2 = f.readline().split()

temp1, temp2 = (727.2 * 2) / param1, (969.6 * 2) / param2
fname = './Gauss/Sim/LbDelphes/options/cards/delphes_card_LHCb_EndVelo_Rich2_withEcal.tcl'

with open(fname, 'r') as file:
    data = file.readlines()

data[365] = '   for {set i 0} {$i <= ' + str(param1) + '} {incr i} {\n'
data[366] = '       add YBins [expr { -727.2 + $i * ' + str(temp1) + ' }]\n'
data[368] = '   for {set i 0} {$i <= ' + str(param2) + '} {incr i} {\n'
data[369] = '       set X [expr { -969.6 + $i * ' + str(temp2) + ' }]\n'

with open(fname, 'w') as file:
    file.writelines(data)
