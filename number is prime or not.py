flag=0
n=int(input(""))
for i in range (1,n+1):
    if(n%i==0):
        flag=flag+1
if(flag==2):
    print("number is prime number")
else:
    print("number is not prime number")
    
