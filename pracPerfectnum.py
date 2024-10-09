n=int(input())
sum=0
for i in range(1, n):
    if n%i==0:
        print(i, end=" ")
        sum=sum+i
if sum==n:
    print("\nperfect number")
else:
    print("\nnot a perfect number")        