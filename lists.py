#list
# list is used to store data or elements
#list are stored in []brackets
list_of_fruits =['banna, mangos,pinaple']
print("my mother bought the following fruits",list_of_fruits)

#to add element in list we use "apped"
#example to add elemment tomatoes in the list above:
list_of_fruits.append('tomatoes')
print("my mother bought the following fruits",list_of_fruits)

#to add element at specific position
list001 =["apple, banana, watermelon"]
list001.insert(0,"mango")
print('this are the fruits i bought',list001)

#to add element from one list to another list
list01 = [1, 3, 6, 8]
list02 = ["cow, goat, sheep"]
list01.extend(list02)
print(list01)
#TO delete element in a list
class_list =["caleb", "alex", "dennis","christine","janet"]
del class_list[1]
print(class_list)

#to empty element in list 
#use clear()method
class_list =["caleb", "alex", "dennis","christine","janet"]
class_list.clear()
print(class_list)

#To acess the an element in a list
school_prefects =["john","kelvin","joseph","maina","kamau"]
print("he is our school captain",school_prefects[1])

# example two
form_four_south =["john","kelvin","joseph","maina","kamau","dennis","telvin"]
print("best three students in previous exam were",form_four_south[1:4])


