n=int(input("Enter number of values needed="))
f1=0
f2=1
count=0
if n<=0:
    print("No values")
elif n<=1:
    print("FIBANOCCI SERIES")
    print(f1)
else:
    print("FIBANOCCI SERIES")
    while count<=n:
        print(f1)
        fth=f1+f2
        f1=f2
        f2=fth
        count+=1