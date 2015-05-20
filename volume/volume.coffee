command: "python volume/getVolume.py"

refreshFrequency: 5000

render: (output) ->
	"<div>#{output}</div>"
	
style: """
	margin-top: 170px;
	margin-left: 50px;
	"""