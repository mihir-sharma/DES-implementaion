def initial_permutation():
    IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40,
          32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63,
          55, 47, 39, 31, 23, 15, 7]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5,
         6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    op = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5,
          6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    strip=''
    y = input("enter input bits (64)")
    for i in range(0, 64):
        x[i] = y[i]
    for j in range(0, 64):
        index = IP[j]
        op[j] = x[index - 1]
        strip = strip + op[j]
    return strip

def keygen():
    y = input("enter 8 letter key")
    key = [1, 2, 3, 4, 5, 6, 7, 8]
    z = [1, 2, 3, 4, 5, 6, 7, 8]
    keyfull = ''
    for i in range(0, 8):
        z[i] = ord(y[i])
        key[i] = int(bin(z[i])[2:])
    for i in range(0, 8):
        ctr = 0
        checker = str(key[i])
        for j in range(0, 7):
            if checker[j] is '1':
                ctr = ctr + 1
        if ctr % 2 is 0:
            key[i] = 10 * key[i] + 0
        else:
            key[i] = 10 * key[i] + 1
        keyfull = keyfull + str(key[i])

    return keyfull

def PC1(keyin):
    k56 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4,
           5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    yi = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5,
          6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    strx = ''
    for i in range(0, 64):
        yi[i] = int(keyin[i])
    for i in range(0, 56):
        index = PC1[i] - 1
        k56[i] = yi[index - 1]
        strxi = str(k56[i])
        strx = strx + strxi
    return strx

def subkey_generation(permkey):
    def key_splitter(y):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
        R = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
        strxl = ''
        strxr = ''
        for i in range(0, 56):
            yi[i] = int(y[i])
        for i in range(0, 56):
            if i < 28:
                L[i] = yi[i]
                strxil = str(L[i])
                strxl = strxl + strxil
            else:
                R[i - 28] = yi[i]
                strxir = str(R[i - 28])
                strxr = strxr + strxir
        return strxl, strxr

    def key_rotator(L, R, keyno):
        LN = [9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4]
        RN = [9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4]
        while keyno > 0:
            keyno = keyno - 1
            for i in range(0, 28):
                if i % 7 is 6:
                    templ = L[i]
                    tempr = R[i]
                    for j in range(0, 7):
                        index = i - j
                        LN[index] = L[index - 1]
                        RN[index] = R[index - 1]
                    LN[index + 1] = templ
                    RN[index + 1] = tempr
            if keyno > 0:
                keyno = keyno - 1
                LN, RN = key_rotator(LN, RN, keyno + 1)
        return LN, RN

    def recombiner(left, right):
        recomb = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3,
                  4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
        recomb = left + right
        return recomb

    def PC2_permutator(rotkey):
        subkey = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5,
                  6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
        PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
               47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        for i in range(0, 48):
            index = PC2[i]
            subkey[i] = rotkey[index - 1]
        return subkey

    yi = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5,
          6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    leftkey = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    rightkey = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    recombkey = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3,
                 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    subkey = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6,
              7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
    substr3 = ''
    substr = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
    rotator = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    left, right = key_splitter(permkey)
    for h in range(0, 16):
        leftkey[h], rightkey[h] = key_rotator(left, right, rotator[h])
        recombkey[h] = recombiner(leftkey[h], rightkey[h])
        subkey[h] = PC2_permutator(recombkey[h])
        substr3 = ''
        for i in range(0,48):
            substr2 = subkey[h]
            substr3 = substr3 + str(substr2[i])
        substr[h] = substr3
    return substr

def splitip(perminput):
    y= perminput
    l0= ''
    r0= ''
    for i in range(0,32):
        l0 = l0 + y[i]
    for i in range(32,64):
        r0 = r0 + y[i]
    return l0, r0

def E_table(etip):
    ip = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    op = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5,
          6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    etop=''
    for i in range(0, 32):
        ip[i] = etip[i]
    jmpctr = 1
    j = 0
    for i in range(1, 31):
        if i % 4 is 3:
            j = j + 1
            op[i + jmpctr] = ip[i]
            jmpctr = jmpctr + 2
            op[i + jmpctr] = ip[i]
        elif i % 4 is 0:
            j = j + 1
            op[i + jmpctr] = ip[i]
            op[i + jmpctr - 2] = ip[i]
        else:
            op[i + jmpctr] = ip[i]
    op[1] = op[47] = ip[0]
    op[0] = op[46] = ip[31]
    for i in range(0,48):
        etop = etop + op[i]
    return etop

def box_creator(right0,skey):
    skeyi = int(skey, 2)
    right0i = int(right0, 2)
    xor= bin(skeyi ^ right0i)[2:]
    box = str(xor.zfill(48))
    return box

def s_box(box):
    class s1():
        r1 = [12, 3, 5, 9, 0, 11, 15, 7, 13, 4, 1, 14, 2, 10, 6, 8]
        r2 = [9, 5, 10, 8, 4, 1, 3, 12, 0, 11, 13, 6, 14, 2, 15, 7]
        r3 = [8, 0, 11, 2, 9, 10, 3, 4, 15, 6, 13, 1, 12, 5, 14, 7]
        r4 = [5, 0, 9, 10, 4, 6, 1, 14, 11, 8, 3, 2, 13, 15, 7, 12]

    class s2():
        r1 = [10, 6, 8, 0, 4, 2, 5, 9, 13, 12, 7, 3, 15, 1, 11, 14]
        r2 = [0, 4, 2, 7, 3, 12, 14, 11, 1, 10, 8, 6, 15, 9, 13, 5]
        r3 = [13, 0, 7, 12, 10, 15, 11, 1, 14, 5, 9, 6, 8, 3, 2, 4]
        r4 = [11, 5, 9, 6, 4, 2, 3, 8, 0, 7, 10, 15, 13, 12, 1, 14]

    class s3():
        r1 = [5, 0, 9, 10, 4, 6, 1, 14, 11, 8, 3, 2, 13, 15, 7, 12]
        r2 = [12, 3, 5, 9, 0, 11, 15, 7, 13, 4, 1, 14, 2, 10, 6, 8]
        r3 = [8, 0, 11, 2, 9, 10, 3, 4, 15, 6, 13, 1, 12, 5, 14, 7]
        r4 = [9, 5, 10, 8, 4, 1, 3, 12, 0, 11, 13, 6, 14, 2, 15, 7]

    class s4():
        r1 = [11, 5, 9, 6, 4, 2, 3, 8, 0, 7, 10, 15, 13, 12, 1, 14]
        r2 = [13, 0, 7, 12, 10, 15, 11, 1, 14, 5, 9, 6, 8, 3, 2, 4]
        r3 = [0, 4, 2, 7, 3, 12, 14, 11, 1, 10, 8, 6, 15, 9, 13, 5]
        r4 = [10, 6, 8, 0, 4, 2, 5, 9, 13, 12, 7, 3, 15, 1, 11, 14]

    class s5():
        r1 = [0, 11, 13, 6, 14, 2, 15, 7, 9, 5, 10, 8, 4, 1, 3, 12]
        r2 = [12, 3, 5, 9, 0, 11, 15, 7, 13, 4, 1, 14, 2, 10, 6, 8]
        r3 = [4, 15, 6, 13, 1, 12, 5, 14, 7, 8, 0, 11, 2, 9, 10, 3]
        r4 = [8, 3, 2, 13, 15, 7, 12, 5, 0, 9, 10, 4, 6, 1, 14, 11]

    class s6():
        r1 = [10, 6, 8, 0, 4, 2, 5, 9, 13, 12, 7, 3, 15, 1, 11, 14]
        r2 = [6, 15, 9, 13, 5, 7, 3, 12, 14, 11, 1, 10, 8, 0, 4, 2]
        r3 = [1, 14, 5, 9, 6, 8, 3, 2, 4, 13, 0, 7, 12, 10, 15, 11]
        r4 = [11, 5, 9, 6, 4, 2, 3, 8, 0, 7, 10, 15, 13, 12, 1, 14]

    class s7():
        r1 = [5, 0, 9, 10, 4, 6, 1, 14, 11, 8, 3, 2, 13, 15, 7, 12]
        r2 = [12, 3, 5, 9, 0, 11, 15, 7, 13, 4, 1, 14, 2, 10, 6, 8]
        r3 = [15, 6, 13, 1, 12, 5, 14, 7, 8, 0, 11, 2, 9, 10, 3, 4]
        r4 = [0, 11, 13, 6, 14, 2, 15, 7, 9, 5, 10, 8, 4, 1, 3, 12]

    class s8():
        r1 = [7, 10, 15, 13, 12, 1, 14, 11, 5, 9, 6, 4, 2, 3, 8, 0]
        r2 = [11, 1, 14, 5, 9, 6, 8, 3, 2, 4, 13, 0, 7, 12, 10, 15]
        r3 = [0, 4, 2, 7, 3, 12, 14, 11, 1, 10, 8, 6, 15, 9, 13, 5]
        r4 = [12, 7, 3, 15, 1, 11, 14, 10, 6, 8, 0, 4, 2, 5, 9, 13]


    parti = [1, 2, 3, 4, 5, 6, 7, 8]
    sboxop = ''
    parts = [box[i:i + 6] for i in range(0, len(box), 6)]
    for i in range(0, 8):
        parti[i] = int(parts[i])
    x = [0, 1, 2, 3, 4, 5]
    op = [0, 1, 2, 3, 4, 5, 6, 7]
    for j in range(0, 8):
        seg = parts[j]
        for i in range(0, 6):
            x[i] = int(seg[i])
        checkr1 = x[0]
        checkr2 = x[5]
        checkc = [x[1], x[2], x[3], x[4]]
        if j is 0:
            sbox = s1
        elif j is 1:
            sbox = s2
        elif j is 2:
            sbox = s3
        elif j is 3:
            sbox = s4
        elif j is 4:
            sbox = s5
        elif j is 5:
            sbox = s6
        elif j is 6:
            sbox = s7
        elif j is 7:
            sbox = s8
        u = 8 * checkc[0] + 4 * checkc[1] + 2 * checkc[2] + 1 * checkc[3]
        if checkr1 is 0 and checkr2 is 0:
            rd = sbox.r1[u]
        if checkr1 is 0 and checkr2 is 1:
            rd = sbox.r2[u]
        if checkr1 is 1 and checkr2 is 0:
            rd = sbox.r3[u]
        if checkr1 is 1 and checkr2 is 1:
            rd = sbox.r4[u]
        replace = bin(rd)[2:]
        repint = int(replace)
        sboxop = sboxop + str(replace.zfill(4))
    return sboxop

def sbox_permutator(smat):
    P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
    y = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
    permsmat = ''
    for i in range(0,32):
        index = P[i]
        y[i] = smat[index -1]
        permsmat = permsmat + y[i]
    return permsmat

def xorfl(f, l):
    fi = int(f, 2)
    li = int(l, 2)
    xor = bin(li ^ fi)[2:]
    r1 = str(xor.zfill(32))
    return r1

def IP_inverse(preop):
    IPinv = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
    y = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    finalop = ''
    for i in range(0, 64):
        index = IPinv[i]
        y[i] = preop[index - 1]
        finalop = finalop + y[i]
    return finalop

#----------------------*--------------------------*-----------------------------*--------------------------*------------------------*

x=initial_permutation()
key = keygen()
subin= PC1(key)
subout = subkey_generation(subin)
ipl0, ipr0 = splitip(x)
for i in range(0,16):
    ipl1 = ipr0
    ER=E_table(ipr0)
    box = box_creator(ER, subout[i])
    smat = s_box(box)
    f = sbox_permutator(smat)
    ipr1 = xorfl(f,ipl0)
    ipr0 = ipr1
    ipl0 = ipl1

temp = ipl0
ipl0 = ipr0
ipr0 = temp

preoutput = ipl0 + ipr0
DESencryptop = IP_inverse(preoutput)
print(DESencryptop)





#1011101111110000101110111111000010111011111100001011101111110000   ---------->  sample input (remove#)
