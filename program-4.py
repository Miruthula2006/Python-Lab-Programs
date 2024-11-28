n=int(input())
a=0
b=1
count=0
if n<=0:
    print("Enter a positive number")
elif n==1:
    print(a)
else:
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
