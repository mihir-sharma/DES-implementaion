ip = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
op =  [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
y = input("enter the 32 bit input")
print(len(y))
for i in range(0,32):
    ip[i]= int(y[i])
jmpctr=1
j=0
for i in range(1,31):
    if i%4 is 3:
        j=j+1
        op[i + jmpctr]=ip[i]
        jmpctr= jmpctr + 2
        op[i + jmpctr]= ip[i]
    elif i%4 is 0:
        j = j + 1
        op[i + jmpctr] = ip[i]
        op[i + jmpctr - 2] = ip[i]
    else:
        op[i+jmpctr]=ip[i]
op[1]=op[47]=ip[0]
op[0]=op[46]=ip[31]
print(op)
