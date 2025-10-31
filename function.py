def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)



"""def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c =7, d= 8)"""



"""def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
"""


"""def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana","Cherry"]
my_function(fruits)
"""


"""def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")"""


