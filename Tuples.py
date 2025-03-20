#tuples
#Tuples are used to store multiple items in a single variable
#a tuple is a collection which is ordered and unchangeable.
#tuples are writen with round braxkets
#tuples are unchangable, meaning that we can not change ,add or remove items after the tuple has  been created
# we can use the tuple () constrCTOR to make a tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#access tuple items
# we use idex number to acces items in a tuple
# the index number starts from 0
#example
my_tuple1 = ("cow","goat","sheep")
print (my_tuple1[0])
print (my_tuple1[1])
print(my_tuple1[2])

#negative indexindg
# we can acess tuple items by negative indexing
#example
my_tuple2 =("dog","cat","rat")
print(my_tuple2[-1])
print(my_tuple2[-2])
print(my_tuple2[-3])

#range of indexes
#it is possible to specify a range of indexes by specifyng where to start and wher to end the range
# example
my_tuple3 = ("red", "blue", "green", "yellow", "purple")
print(my_tuple3[1:4])  # Outputs items from index 1 to 3 (excluding index 4)
print(my_tuple3[:3])   # Outputs items from the start to index 2
print(my_tuple3[2:])   # Outputs items from index 2 to the end

#to update a tuple
#to update a tuple we  convet it into a list and the convert it back to a tuple
#example
my_tuple4 = ("read", "blue", "green","yellow","purpple")
x = list(my_tuple4)
x[0] = "black"
my_tuple4 = tuple(x)
print(my_tuple4)
