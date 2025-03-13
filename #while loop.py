#while loop.py
i = 0
while i< 10:
    print(i)
    i +=1

#break statement in while loop
i = 5
while i < 20:
    print(i)
    if i == 10:
        break
    i += 1

#continue statement in while loop
i = 5
while i < 20:
    i +=1
    if i == 10:
        continue
    print(i)

#else statement in while loop
i = 1
while i < 10:
    print(i)
    if i == -10:
        break
    i -=1
else:
    print("i is greater tha 7")