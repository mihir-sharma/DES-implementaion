def key_splitter(y):
    L = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
    R = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
    strxl = ''
    strxr = ''
    for i in range(0,56):
        yi[i]=int(y[i])
    for i in range(0,56):
        if i <28:
            L[i]=yi[i]
            strxil = str(L[i])
            strxl = strxl + strxil
        else:
            R[i-28]=yi[i]
            strxir = str(R[i-28])
            strxr = strxr + strxir
    return strxl, strxr

def key_rotator(L,R,keyno):
    LN=[9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4]
    RN=[9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4]
    while keyno>0:
        keyno = keyno - 1
        for i in range(0,28):
            if i%7 is 6:
                templ = L[i]
                tempr = R[i]
                for j in range(0,7):
                    index = i-j
                    LN[index]=L[index-1]
                    RN[index]=R[index-1]
                LN[index+1]= templ
                RN[index+1]=tempr
        if keyno>0:
            keyno = keyno -1
            LN,RN = key_rotator(LN,RN,keyno+1)
    return LN, RN

yi = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
leftkey=[2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
rightkey=[2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
rotator = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
y = input("enter permuted key")
left,right =key_splitter(y)
for h in range(0,16):
    leftkey[h],rightkey[h]=key_rotator(left,right,rotator[h])
    print(leftkey[h])
    print(rightkey[h])
    print("\n\n")

