# 1. Create a function with variable length of arguments..







# 2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.


# def outer(a,b):
#     def inner(a,b):
#         z=a+b
#         print(z)
#     inner(2,3)
# outer(a,b)



# 2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.

# def a():
#     x=int(input("enter 1st no : "))
#     y=int(input("enter 2nd no : "))
#     def b():
#         nonlocal x
#         nonlocal y
#         s=x+y
#         print("sum is :",s)
#         def c():
#             nonlocal s
#             z=s+5
#             print("final value after adding 5 is :",z)
#         c()
#     b()
# a()


# 3. Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

#
# def display_student(name="shreejan",age=20):
#     print(f"Your name is {name},and your age is {age}")
# display_student(name="Ram")



# 5. What is the difference between 10 / 3 and 10 // 3?

# a=10/3                                # returns all decimal values (float)      3.3333333333335
# b=10//3                               # returns point ko agadi ko value (int)   3                 i.e floor value
# print("a=",a,"b=",b)



# 6. What about two asterisks (**)?

# x=3*2                                   # multiply 3*2=6
# y=3**2                                  # square   3^2=9
# print("x=",x,"y=",y)



# 7. What is the difference between local and global variables?
# -->Those variable that are declared outside the function are called global variables.
# -->Those variable that are declarde inside the function are called local variables.



# 8. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
#
# def fizz_buzz():
#     a=int(input("Enter a number :"))
#     if(a%3==0):
#         if(a%5==0):
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif(a%5==0):
#         print("Buzz")
#     else:
#         print("returned value:",a)
# fizz_buzz()




# 9. Write a function for checking the speed of drivers.
# If speed is less than 70, it should print “Ok”.
# if the speed is 80, it should print: “Warning”.

# def speed():
#     if n<70:
#         print("OK")
#     elif n>80:
#         print("Warning!!!")
# n=int(input("Enter the speed:"))
# speed()



# 10. Write a program that prompts the user to input a positive integer.
#  It should then print the multiplication table of that number.


# n=int(input("Enter a positive number :"))
# for i in range(1,11):
#     print( n,"*",i,"=",n*i)




# 11. Write a program that prompts the user to input an integer and then
# outputs the number with the digits reversed.
#  For example, if the input is 12345, the output should be 54321.

# n= int(input("Enter the number:"))
# print("number before reversing:",n)
# rev=number_string[::-1]
# print("number after reversing:",rev)



# 12. Write a python program that return the number of
# characters in a string.
# myList = "Parameter"

# myList="Paramater"
# n=len(myList)
# print(n)



# 13. Write a Python program to multiply all the numbers in a list using while and for loop.
# Sample list = [8,2,3,-1,7]

# list=[8,2,3,-1,7]
# total=1
# for i in list:
#     total= total*i
# print("Multiplication of list is:",total)



# 14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# Sample list : [8, 2, 3, 0, 7]
# list=[8,2,3,0,7]
# total=0
# for i in list:
#     total=total+i
# print(total)



# 15. Accept string from the user and display only those characters which are
# present at an even index.

# n = input("Enter a string:")
# modified_str= n[::2]
# print(modified_str)



# 16. Accept string from the user and display only those characters which are
# present at an odd index.
# n = input("Enter a string:")
# modified_str= n[::2]
# print(modified_str)



# 17. Sum : 1 to 10 (or any number) using while loop.
# num = 15
# sum = 0
# while num > 0:
#     sum += num
#     num -= 1
# print("The sum is", sum)




# 18. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list=[0,1,2,3,4,5,6,7,8,9]
# modified_num=list[0:9:2]
# print(modified_num)



# 19. Write a Python program to print the odd numbers from a given list.
# Sample List : [12,13,14,15,16,17,18,19]
# list=[12,13,14,15,16,17,18,19]
# odd=list[1:8:2]
# print(odd)



# 20. Write a program to accept percentage and display the Category according to the  following criteria :
# Percentage	Category
# < 41	                     Failed
# >=41 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent


percentage=int(input("Enter your percentage:"))
if percentage>=65:
    print("Excellent")
elif percentage>=55:
    print("Good")
elif percentage>=40:
    print("Fair.")
else:
    print("Failed")