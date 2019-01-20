def get_even_list(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
