#list

sayak = ["B.Tech", "CSE", 8.0, "Tata Communications", "Agartala Tripura", "India", 799001, True]
'''print(sayak)

print(type(sayak))

print(len(sayak))

print(sayak[-1])

sayak.append("Ai Infrastructure and Automation Engineer")

print(sayak)

for item in sayak:
    print(item)

for item in sayak:
    print(f"Item: {item}, Type: {type(item)}")

for item in sayak:
    if item == True:
        print(f"{item} is of type Boolean")
    elif item == 8.0:
        print(f"{item} is of type Float")
    else:
        print(f"{item} is of type {type(item)}")

print(dir(sayak))

print(sayak.count("CSE"))
print(sayak.index("India"))
print(sayak.pop())
print(sayak)
sayak.append("Ai Infrastructure and Automation Engineer")
print(sayak)

for sayak in sayak:
    print(sayak)   '''

items = {
    "B.Tech":"SRM Institute of Science and Technology",
    "Branch":"CSE",
    "GPA":8.0,
    "1st job":"Tata Communications",
    "clity":"Agartala, Tripura",
    "country":"India",
    "pin":799001,
    "bool":True,
    "more_info": sayak
}

'''print(items)

print(type(items))'''

print("i live in ",items["clity"],",",items["country"])
print("my first job was at ",items["1st job"])
print("my GPA is ",items["GPA"])


