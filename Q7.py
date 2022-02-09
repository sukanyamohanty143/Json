import json
new_file="text.txt"
dict={}
with open(new_file) as f:
    for line in f:
        command, description = line.strip().split(None, 1)
        dict[command] = description.strip()
out_file = open("text1.json", "w")
json.dump(dict, out_file, indent = 4, sort_keys = False)
out_file.close()