import json
data={"name":"sukanya","education":"BA","age":20}
newdata=json.dumps(data)
print(newdata)
print(type(newdata))