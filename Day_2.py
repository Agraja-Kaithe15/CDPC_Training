1. Take user's name and age and print message
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + ", you are", age, "years old.")

2. Calculate perimeter of rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("Perimeter of rectangle =", perimeter)

3. Convert kilometers into meters and centimeters
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print("Meters =", meters)
print("Centimeters =", centimeters)

4. Calculate total bill of 3 products
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
total = p1 + p2 + p3

5. Convert hours into minutes and seconds
hours = int(input("Enter hours: "))
minutes = hours * 60
seconds = hours * 3600
print("Minutes =", minutes)
print("Seconds =", seconds)

6. Area of triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = (base * height) / 2
print("Area of triangle =", area)

7. Print double and triple of a number
num = int(input("Enter a number: "))
double = num * 2
triple = num * 3
print("Double =", double)
print("Triple =", triple)

8. Total seconds in given number of days
days = int(input("Enter number of days: "))
seconds = days * 24 * 60 * 60
print("Total seconds =", seconds)

9. Convert rupees into paise
rupees = float(input("Enter rupees: "))
paise = rupees * 100
print("Paise =", paise)

10. Total number of students
boys = int(input("Enter number of boys: "))
girls = int(input("Enter number of girls: "))
total = boys + girls
print("Total students =", total)

Basic Logic Problems

1 Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

2 Write a program to find the largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

3 Check whether a number is positive, negative, or zero.
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

4 Write a program to check whether a number is divisible by both 3 and 5.
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

5 Write a program to print numbers from 1 to N.
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i)

6 Write a program to print all even numbers from 1 to N.
n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

7 Write a program to calculate the sum of first N natural numbers.
n = int(input("Enter N: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum =", sum)

8 Write a program to calculate the factorial of a number.
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial =", fact)

9 Write a program to print the multiplication table of a number.
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

10 Write a program to count the number of digits in a number.
num = int(input("Enter number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Digits =", count)

11 Write a program to reverse a number.
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print("Reverse =", rev)

12 Write a program to check whether a number is palindrome.
num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

13 Write a program to find the sum of digits of a number.
num = int(input("Enter number: "))
sum = 0
while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10
print("Sum of digits =", sum)

14 Write a program to check whether a number is an Armstrong number.
num = int(input("Enter number: "))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    sum = sum + rem**3
    num = num // 10
if sum == temp:
    print("Armstrong number")
else:
    print("Not Armstrong")

15 Write a program to print numbers divisible by 7 between 1 and N.
n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)


#resverse the number
no = int(input("Enter number: "))
rev = 0
while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10
print("Reverse number is", rev)

#count number
no = int(input("enter no:"))
count=0 
while no > 0:
   no = no//10
   count = count+1
print("number of count",count)    

#sum of digits
no = int(input("Enter number: "))
sum = 0
while no > 0:
    rem = no % 10
    sum = sum + rem
    no = no // 10
  print("Sum of digits:", sum)

#check number is palindrome
no = int(input("Enter number: "))
temp = no
rev = 0
while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10
if temp == rev:
   print("Number is Palindrome")
else:
   print("Number is not Palindrome")
 
#check no is armstrone
no = int(input("Enter number: "))
temp = no
count = 0
sum = 0
while no > 0:
    count == 1
    no = no // 10
    no=temp
while no> 0:
    rem = no%10
    sum = sum + rem ** count
    no= no // 10

# Check Armstrong
if temp == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
	