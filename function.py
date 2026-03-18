# task 2 create a function to check if a number is even or odd 

num = int(input("Enter a number: "))

def check_even_odd(num):
     if num % 2 == 0:
         return "Even"
     else:
         return "Odd"
result = check_even_odd(num)
print(result)


#Task 3:create a function to find the factorial of a number.

def factorial(n):
   if n == 0 or n == 1: 
       return 1
   return n * factorial(n - 1)

# Example
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))



#task 4 create the function to find the maximum number of three
def maximum(a, b, c):
    if a >= b and a >= c:
         return a 
    elif b >= a and b >= c:
         return b
    else:
         return c

 # User input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Maximum number is:", maximum(x, y, z))

# task 5 create a function to check is a string is palindrome

def is_palindrome(s):
     return s == s[::-1]

text = input("Enter string: ")
if is_palindrome(text):
     print("Palindrome")
else:
     print("Not Palindrome")

#Task 6:Create a function to calculate the area of circle
def area_of_circle(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))
print("Area of circle:", area_of_circle(r))