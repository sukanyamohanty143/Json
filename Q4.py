import json
d={'4':5,'6':7,'1':3,'2':4}
d1={}
a=sorted(d.keys())
for i in a:
    for j in d.keys():
        if i==j:
            d1[i]=d[j]
b=json.dumps(d1)
print(b)