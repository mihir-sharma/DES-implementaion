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

def recombiner(left,right):
    recomb=[2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
    recomb = left + right
    return recomb

def PC2_permutator(rotkey):
    subkey = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
    PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    for i in range(0,48):
        index = PC2[i]
        subkey[i] = rotkey[index-1]
    return subkey

yi = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
leftkey=[2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
rightkey=[2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
recombkey = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
subkey = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
rotator = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
y = input("enter permuted key")
left,right =key_splitter(y)
for h in range(0,16):
    leftkey[h],rightkey[h]=key_rotator(left,right,rotator[h])
    recombkey[h] = recombiner(leftkey[h],rightkey[h])
    subkey[h] = PC2_permutator(recombkey[h])
    print(recombkey[h])

# 00100111111111111111111100000000100110101100111000100001    ---    sample input
