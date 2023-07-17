N=str(input("check:"))
if N in ("aeiouAEIOU"):
    print("it is vowels")
elif N in("BCDFGHJKLMNPQRSTUVWXYZbcdfghijklmnpqrstuvwxyz"):
    print("it is consonents")
else:
    print("Give a correct inputs")
