command: "python uptime/getUptime.py"

refreshFrequency: 50000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 200px;
	margin-left: 360px;
	"""