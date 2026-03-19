#sum of two number
a=int(input("Enter any value:"))
b=int(input("Enter any value:"))
res=a+b
print(res)

n=int(input("Enter any value:"))
res=n%10
print(res)

no=int(input("Enter any value:"))
n1=no%10
n2=no//10
res=n1+n2
print(res)

#sum of three digit number
no=int(input("Enter any value:")) #12
n1=no%10 #3
no=no//10 #12
n2=no%10 #2
n3=no//10 #1
res=n1+n2+n3
print(res)

#sum of 5 digit
no=int(input("Enter any value:")) 
n1=no%10 
no=no//10 
n2=no%10 
n3=no%10 
n4=no%10
n5=no%10
res=n1+n2+n3+n4+n5
print(res)

#reverse number 3 digit
no=int(input("Enter any value:"))
n1=no%10
no=no//10
n2=no%10
n3=no//10
res=n1*100+n2*10+n3*1
print(res)

#accept 9 digit number find sum of first and last number in three step
no = 123456789
n1 = no % 10        # last digit
n2 = no // 100000000  # first digit (for 9-digit number)
res = n1 + n2
print("Sum =", res)