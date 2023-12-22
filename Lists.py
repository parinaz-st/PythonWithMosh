names = ["parinaz", "behnam", "parisa"]
print("the first element (1): " + names[1])
print("the last element (-1): " + names[-1])
print("the  second last element (-2): " + names[-2])

names[1] = "pehnam"
print(names[1])

print("the first 2 item of the list: ")
print(names[0:2])

names.append("parsa")
print(names)
names.insert(1, "alieh")
print(names)
names.remove("parsa")
print(names)
print('alieh' in names)
print(len(names))
names.clear();
print(names)

