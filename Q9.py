import json
dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        }   
}
file=json.dumps(dict,indent=2)
jsfile=open("text2.json","w")
json.dump(dict, jsfile, indent = 4, sort_keys = False)
jsfile.close()
print(file)
userchoice=input("what you want?")
newdict=json.loads(file)
for items in newdict: