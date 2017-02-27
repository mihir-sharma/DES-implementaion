y= input("enter 8 letter key")
key=[1,2,3,4,5,6,7,8]
z=[1,2,3,4,5,6,7,8]
for i in range(0,8):
    z[i]=ord(y[i])
    key[i]=int(bin(z[i])[2:])
print(key)
for i in range(0,8):
    ctr=0
    checker=str(key[i])
    for j in range(0,7):
        if checker[j] is '1':
            ctr = ctr+1
    if ctr%2 is 0:
        key[i]= 10*key[i] + 0
    else:
        key[i]=10*key[i] + 1
print(key)