#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#example
group_a ={"name":"john"}
print(group_a)

#accesing items in a dictionary
# use squrae brackets to acces items in a dictionary
#eample
group_b = {"maina":"carpenter","age":25}
x = group_b['age']
print(x)
print("my name is "+group_b["maina"]+" and i am "+str(group_b["age"])+" years old")

#change values in a dictionary
#example
group_c = {"ken":"engineer","age":30}
group_c["age"] = 24
print(group_c)

#loop through a dictioary
#example
group_d = {"teacher":"jane","maths teacher":"john","science_teacher":"peter"}
for z in group_d:
   print (z)

#loop throough values in a dictionary
#example
for value in group_d.values():
    print(value)