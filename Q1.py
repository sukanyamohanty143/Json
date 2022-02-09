import json
data="{name:kanya,classs:X,age:20}"
new=json.loads(data)
print("key","  ","value")
for i in new:
    print(i,"  ",new[i])



