import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]
list5=["name","Designation","Age","salary"]
dic1={}
dic2={}
dic3={}
dic4={}
maindict={}
i=0
while i<len(list1):
    var=list5[i]
    dic1[var]=list1[i]
    dic2[var]=list2[i]
    dic3[var]=list3[i]
    dic4[var]=list4[i]
    i+=1
maindict["emp1"]=dic1
maindict["emp2"]=dic2
maindict["emp3"]=dic3
maindict["emp4"]=dic4
print(maindict)