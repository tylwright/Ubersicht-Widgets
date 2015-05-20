#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "top -l 1 | head -n 10 | grep 'CPU usage: ' | awk '{print $7}'"
results = subprocess.check_output(command, shell=True)

cpuFree = results.splitlines()[0]

cpuFree = re.sub('[A-z,: %]','',cpuFree)

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
		
cpuUsed = 100 - int(float(cpuFree))
print "<style>%s</style><label>CPU Usage:</label><meter value='%s' min='0' max='100'></meter>" % (style, cpuUsed)