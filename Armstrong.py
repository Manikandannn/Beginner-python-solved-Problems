n=int(input(""))
x=0
temp=n
while(temp>0):
    a=temp%10
    x=x+a**3
    temp=int(temp/10)
if(n==x):
    print("It is armstrong number")
else:
    print("it is not armstrong number")
    
