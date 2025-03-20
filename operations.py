#operation in python
# > means greater than
#  < means less than
# >= greater than or equal to
# == means equal to
# != means not equal to
# and means logical and
# or means logical or
# not means logical not
# in means in the list
# not in means not in the list

# example
a = 10
b= 20
if a > b:
    print("a is greater than b")
else:
    ("b is greater than a")

#example 2
# to calculate the discount of a product
price = 100
discount = 10
final_price = price -discount
print ("the fial price is ",final_price)

#example 3
# to find out if a number is postive or negative and old
number = -7
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")
    if number %2 == 0:
        print("the number is even")
    else:
        print("the number is old")

# example 4
# to demonstrate the use of "and" and "or"
x = 5
y = 10
z = 15

if x < y and y < z:
    print("x is less than y and y is less than z")

if x > y or y < z:
    print("Either x is greater than y or y is less than z")

# example 5
# to find out if a certain elemnt is in the list
top_four = ["manchester city","newcastle united","arsenal","liverpool"]
if "manchester united"in top_four:
    print("chelsea is in the top four")
else:
    print("manchester united wil not finish in the top four")

