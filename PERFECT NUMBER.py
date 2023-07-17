n=int(input(""))
final=0
for i in range(1,n):
    if(n%i==0):
       final=final+i;
if(n==final):
    print(final,"is perfect not")
else:
    print(n,"is not perfect number")
    
