command: "python externalNetworkAddresses/getExtNetAddr.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 200px;
	margin-left: 200px;
	"""