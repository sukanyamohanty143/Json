import json
a = [
	{
		"component": "text",
		"value": "Q.1 Json data ko <span style=\"\">python</span> object main convert karne ka program likho?."
	},
	{
		"component": "text",
		"value": "<b>Example:</b>"
	},
	{
		"component": "text",
		"value": "<span style=\"color: #eb9371; background-color: rgba(39, 41, 43, 0.83); box-shadow: 2px 2px 2px rgba(22, 9, 1, 0.6); border-radius: 2px; padding: 2px\">Input :-</span>"
	},
	{
		"component": "text",
		"value": "<span style=\"color: #eb9371; background-color: rgba(39, 41, 43, 0.83); box-shadow: 2px 2px 2px rgba(22, 9, 1, 0.6); border-radius: 2px; padding: 2px\">Output :-</span>"
	}
]

b = json.dumps(a)
print(type(b))
c=json.loads(b)
print(c)