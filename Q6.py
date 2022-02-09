import json
data='{"a":  1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}'
newdata=json.loads(data)
print(type(newdata))
newdict={}
for i in newdata:
    a=i
    b=newdata[i]
    newdict[a]=b
print(newdict)