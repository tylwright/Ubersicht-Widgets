command: "python ramUsage/getRAM.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 140px;
	margin-left: 50px;
	"""