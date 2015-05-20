command: "python cpuUsage/getCPU.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 110px;
	margin-left: 50px;
	"""