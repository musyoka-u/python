# if and if else ststement in python
#Equals: a == b
# Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a = 50
b = 50
if a > b:
    print("a is greater than b")
elif b == a:
    print("a and b are equal")
else:
    print("b is greater than a")
  #example 2
a = 200
b = 170
c = 170
if a > b and c < b:
   print("both conditions are True")
elif a < b or c > b:
     print("c is  greater tha b")
else:
     print("none of the above is true ")

#example 3
# Determine who arrives first based on the travel method
travel_method = "airplane"
if travel_method == "airplane":
    print("You will arrive at your destination first by airplane.")
elif travel_method == "motorcycle":
    print("You will arrive at your destination second by motorcycle.")
elif travel_method == "bus":
    print("You will arrive at your destination last by bus.")
else:
    print("Invalid travel method.")

# Check if you will arrive at the destination
if travel_method == "bus" or travel_method == "motorcycle" or travel_method == "airplane":
    print("You will arrive at your destination.")
else:
    print("you will not arive at your destination")

# Examole 3
#using keyword "not"to chek if specific name appers in the list
thislist = ["ken", "maina", "bonface", "janet"]
if "bonface" not in thislist:
    print("not true")
else:
    print("true")
