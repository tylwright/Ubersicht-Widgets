#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "top -l 1 | head -n 10 | grep PhysMem | awk '{print $6}'"
results = subprocess.check_output(command, shell=True)

ramFree = results.splitlines()[0]

ramFree = re.sub('[A-z,: ]','',ramFree)

style = """label{
			color: white;
			padding-right: 5px;
			font-weight: bold;
			font-family: Helvetica;
		}
		meter{
			width: 300px;
			-webkit-appearance: none;
		}
		meter::-webkit-meter-bar{
		    background: transparent;
		    border: 1px solid white;
		    border-radius: 10px;
		}
		meter::-webkit-meter-optimum-value{
			background: white;
		    border-radius: 10px;
		}
		meter::-webkit-meter-suboptimum-value{
			background: white;
		    border-radius: 10px;
		}
		meter::-webkit-meter-even-less-good-value{
			background: white;
		    border-radius: 10px;
		}"""
		
ramUsed = 32 - int(float(ramFree))
print "<style>%s</style><label>RAM Usage:</label><meter value='%s' min='0' max='32'></meter>" % (style, ramUsed)