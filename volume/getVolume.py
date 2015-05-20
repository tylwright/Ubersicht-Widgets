#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "osascript -e 'get volume settings' | awk '{print $2}'"
results = subprocess.check_output(command, shell=True)

volume = results.splitlines()[0]

volume = re.sub('[A-z,: ]','',volume)

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
		
print "<style>%s</style><label>Volume:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><meter value='%s' min='0' max='100'></meter>" % (style, volume)