#no equal to sum of all its factors except given no
n=int(input())
sum=0
for i in range(1, n):
     if n%i==0:
         print(i,end=" ")
         sum=sum+i
    
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")