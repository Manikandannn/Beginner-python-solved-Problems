n=int(input(""))
if(n%4==0)and (n%100!=0) or (n%400==0):
    print(n,"it is leap year" )
else:
    print("it is not leap year")
