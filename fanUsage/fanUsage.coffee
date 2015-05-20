command: "python fanUsage/getFan.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 50px;
	margin-left: 50px;
	"""