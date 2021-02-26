n=input("Please Enter The number")
n=int(n)
val=1
i=0
while i==n:
    i=i+1
    val,n=val*(n-i),(n-i)
print(val)

