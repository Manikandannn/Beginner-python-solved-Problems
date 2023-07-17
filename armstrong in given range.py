lower=int(input(""))
upper=int(input(""))
for n in range(lower,upper+1):
    
    x=0
    temp=n
    while(temp>0):
        a=temp%10
        x=x+a**3
        temp=int(temp/10)
    if(n==x):
        print(x)
