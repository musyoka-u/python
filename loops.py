#loops
#for loops
numbers = (10, 26, 47, 70, 12)
for i in numbers:
    print(i)

#break statement in loops
#used to stop the loop at given point of the users requirement
domestic_animals = ["cow","goat","sheep","dog","cat"]
for i in domestic_animals:
    if i == "dog":
        break
    print(i)

#continue statement
#used to print element from a given point
domestic_animals = ["cow","goat","sheep","dog","cat","rabbit"]
for i in domestic_animals:
    if i == "dog":
        continue
    print(i)

#range() fanction in loops
prime_numbers = [2,3,5,7,11,17,19]
for i in range(2,19):
    print(i)