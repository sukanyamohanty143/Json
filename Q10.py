dict={"a":1,"b":2,"a":3,"b":4,"c":5,"c":6,"a":7}
newdict={}
for i in dict:
    if i not in newdict:
        newdict[i]=dict[i]
print(newdict)

import json
dict={"a":1,"b":2,"a":3,"b":4,"c":5,"c":6,"a":7}
new_var=json.dumps(dict)
print(new_var)