"""base=int(input(""))
exp=int(input(""))
print(base**exp)"""

base=int(input(""))
exp=int(input(""))
final=1
for i in range(exp):
    final=final*base
print(final)
        
