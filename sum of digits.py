import math
some=int(input(""))
n=0
while(some!=0):
    n=n+(some%10)
    some=some//10
print(math.floor(n))
