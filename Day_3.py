1. Series Calculation Program
# Calculate the series: 1 + (x^1)/1 + (x^2)/2 + ... + (x^(n-1))/(n-1)

n = int(input("Enter n: "))
x = int(input("Enter x: "))

sum = 1

for i in range(1, n):
    sum = sum + (x**i)/i

print("Result =", sum)

Example
Input: n = 3 , x = 2
Output: 4

2. Number Pattern (Repeated Row Pattern)
# Print pattern where each row contains the same number

for i in range(1, 5):        # Outer loop for rows
    for j in range(1, 5):    # Inner loop for columns
        print(i, end="")
    print()

Output

1111
2222
3333
4444
3. Sequential Number Pattern (1–16 Grid)
# Print numbers from 1 to 16 in a 4x4 grid

n = 1

for i in range(1, 5):
    for j in range(1, 5):
        print(n, end="\t")
        n = n + 1
    print()

Output

1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
4. Alphabet Pattern (A–P Grid)
# Print alphabets from A to P in a 4x4 grid

n = 65

for i in range(1, 5):
    for j in range(1, 5):
        print(chr(n), end="\t")
        n = n + 1
    print()

Output

A   B   C   D
E   F   G   H
I   J   K   L
M   N   O   P
5. Increasing Number Pattern
# Print pattern with increasing number repetition

for i in range(1, 5):
    for j in range(1, i + 1):
        print(i, end="")
    print()

Output

1
22
333
4444
6. Star Pattern (Decreasing)
# Print decreasing star pattern

for i in range(1, 5):
    for j in range(5 - i):
        print("*", end="\t")
    print()

Output

* * * *
* * *
* *
*
----HOMEWORK----
# 1. Write a program to check whether a number is even or odd.
no=int(input("enter the no :- "))
if no%2==0:
   print("the number is even")
else:
   print("the number is odd ")

# 2. Write a program to find the largest of three numbers.
a = float(input("enter first numbers "))
b = float(input("enter second numbers "))
c= float(input("enter thrid numbers "))
if a> b:
   if a>c:
      print(f"{a} is he largest number")
elif b>a:
    if b>c:
        print(f"{b} is the largest number")
else:
    print("{c} is the largest number ")

# 3. Check whether a number is positive, negative, or zero.
no=int(input("enter the no :- "))
if no> 0:
   
      print(f"{no} is the positive  number")
elif no==0:
   
        print(f"{no} is zero")
else:
    print(f"{no} is the negative number ")

# 4. Write a program to check whether a number is divisible by both 3 and 5.
no=float(input("enter the no :- "))
if no%3== 0 and no%5==0 :
   print(f"{no} is divisble by 3 and 5 ")

# 5. Write a program to print numbers from 1 to N.
no=int(input("enter the no :- "))
for x in range (1, no+1):
    print(x)

# 6. Write a program to print all even numbers from 1 to N.
no=int(input("enter the no :- "))
for x in range (0, no+1, 2):
    print(x)

# 7. Write a program to calculate the sum of first N natural numbers.
no=int(input("enter the no :- "))
sum=0
for x in range (0, no+1, 1):
  sum+=x
print(f"sum of first {no} naturanl number is {sum}")

# 8. Write a program to calculate the factorial of a number.
no=int(input("enter the no :- "))
factorial = 1

if no < 0:
    print("Factorial does not exist for negative numbers.")
elif no == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, no+ 1):
        factorial *= i
    print(f"The factorial of {no} is {factorial}")

# 9. Write a program to print the multiplication table of a number.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 10. Write a program to count the number of digits in a number.
no=int(input("eneter no: "))
count=0
while(no>0):
  
    no=no//10
    count=count + 1
print("count  is ",count)