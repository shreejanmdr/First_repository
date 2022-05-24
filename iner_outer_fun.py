# 2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.


def a():
    x=int(input("enter 1st no : "))
    y=int(input("enter 2nd no : "))
    def b():
        nonlocal x
        nonlocal y
        s=x+y
        print("sum is :",s)
        def c():
            nonlocal s
            z=s+5
            print("final value after adding 5 is :",z)
        c()
    b()
a()
