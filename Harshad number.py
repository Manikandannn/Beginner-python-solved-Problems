n=int(input(""))
s=0
while(n!=0):
    s=s+(n%10)
    n=n//10
if(n%s==0):
    print("It is harshad number")
else:
    print("It is not harshad number")
