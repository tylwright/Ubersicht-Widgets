#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "df / | awk '{print $8}'"
results = subprocess.check_output(command, shell=True)

percentUsed = results.splitlines()[1]

percentUsed = re.sub('%','',percentUsed)

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
		
print "<style>%s</style><label>Disk Usage:</label><meter value='%s' min='0' max='100'></meter>" % (style, percentUsed)