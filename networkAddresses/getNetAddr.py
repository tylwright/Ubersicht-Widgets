#!/usr/bin/env python
# Tyler Wright

import subprocess, re

# Internal IPs
command = "ifconfig | grep 'inet ' | awk '{print $2}'"
results = subprocess.check_output(command, shell=True)

results = results.splitlines()

results.remove("127.0.0.1")
#results.remove("10.211.55.2")
#results.remove("10.37.129.2")
#results.remove("10.1.100.1")

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
			padding-bottom: 2px;
		}
		"""

print "<style>%s</style><label>IPv4 Addresses</label><ul>" % (style)

for x in results:
	print "<li>%s</li>" % (x)
	
print "</ul>"