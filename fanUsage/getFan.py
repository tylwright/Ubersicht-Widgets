#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "/Applications/smcFanControl.app/Contents/Resources/smc -f"
results = subprocess.check_output(command, shell=True)

currentSpeed = results.splitlines()[3]
minSpeed = results.splitlines()[4]
maxSpeed = results.splitlines()[5]

currentSpeed = re.sub('[A-z,: ]','',currentSpeed)
minSpeed = re.sub('[A-z,: ]','',minSpeed)
maxSpeed = re.sub('[A-z,: ]','',maxSpeed)

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

minSpeed = int(float(minSpeed))
print "<style>%s</style><label>Fan Usage:&nbsp;</label><meter value='%s' min='%s' max='%s'></meter>" % (style, currentSpeed, minSpeed, maxSpeed)