#!/usr/bin/env python
# Tyler Wright

import subprocess, re

command = "uptime | awk '{print $3}'"
number = subprocess.check_output(command, shell=True)
command2 = "uptime | awk '{print $4}'"
unit = subprocess.check_output(command2, shell=True)

number = number.splitlines()[0]
unit = unit.splitlines()[0]
unit= re.sub(',','',unit)

style = """label{
			color: white;
			padding-right: 5px;
			font-weight: bold;
			font-family: Helvetica;
		}
		ul{
			margin-top: 0px;
			margin-left: 0px;
			padding-left: 0px;
		}
		li{
			color: white;
			font-family: Helvetica;
			list-style-type: none;
		}
		"""

print "<style>%s</style><label>Uptime</label><ul>" % style

print "<li>%s %s</li>" % (number, unit)
	
print "</ul>"