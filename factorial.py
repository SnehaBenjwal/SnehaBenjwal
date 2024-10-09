num=int(input("enter a number: "))
fact=1
a=1
while a<=num:
    fact=fact*a
    a+=1
print("factorial of", num, "is", fact)