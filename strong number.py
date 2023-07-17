n=int(input(""))
add=0
temp=n
while(n):
    i=1
    factorial=1
    rem=n%10
    while(i<=rem):
        factorial=factorial*i
        i=i+1
    add=add+factorial
    n=n//10
if(add==temp):
    print("the number is Strong number")
else:
    print("the number is not a strong nummber")
    
    
