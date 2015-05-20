command: "python diskUsage/getDisk.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 80px;
	margin-left: 50px;
	"""