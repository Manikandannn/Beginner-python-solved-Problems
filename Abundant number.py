num=int(input("enter number:"))
m=0
for i in range(1,num+1):
    if(num%i==0):
        m=m+i
        print(m)
if(num<m):
    print("it is abundant number")
else:
    print("it is not abundant number")
