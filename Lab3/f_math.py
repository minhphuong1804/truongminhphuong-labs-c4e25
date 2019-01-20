from random import randint, choice
from calc import eval

x = randint(1, 10)
y = randint(1, 10)
op = choice(["+", "-", "*", "/"])
error = randint(-1,1)
r = eval(x,y,op) + error

print(x, op, y,"=", sum)

result = input("(Y/N)")
if result == "Y":
    if result == sum:
        print("Yay")
    else:
        print("Wrong :(")
else: 
    if result == sum:
        print("Wrong :(")
    else:
        print("Yay")