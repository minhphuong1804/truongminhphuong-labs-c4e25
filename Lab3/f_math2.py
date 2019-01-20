from random import randint
x = randint(1, 10)
y = randint(1, 10)
error = randint(-1,1)
print(x, "+", y,"=", sum)
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

# pip install pyqt5