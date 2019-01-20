# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
pheptinh = input("Your answer")
def eval(x, y,pheptinh):
    result = 0
    if pheptinh == "+":
        equ = x + y
    elif pheptinh == "-":
        equ = x - y
    elif pheptinh == "*":
        equ = x*y
    else:
        equ == x/y
    return result

# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op= ")

# r = eval(4, 5, "*")
# print(r)


# # def sayHi(n):
# #     print("Hi")
# #     print("Hi", n)
# #     print("Bye")
# # sayHi("Quan")
# # sayHi("Minh")

# # def add(x, y):
# #     r = x+y
# #     return r
# # s = add(1, 2)
# # print(s)

# # t = add(6,7)
# # print(t)