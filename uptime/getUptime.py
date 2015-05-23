#!/usr/bin/env python
# Tyler Wright

import subprocess, re

# External IP
command = "uptime | awk '{print $3}'"
results = subprocess.check_output(command, shell=True)

results = results.splitlines()[0]

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

if int(float(results)) == 1:
	print "<li>%s Day</li>" % results
else:
	print "<li>%s Days</li>" % results
	
print "</ul>"