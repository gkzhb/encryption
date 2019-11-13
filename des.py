# DES

IP = [57,49,41,33,25,17, 9,1,
        59,51,43,35,27,19,11,3,
        61,53,45,37,29,21,13,5,
        63,55,47,39,31,23,15,7,
        56,48,40,32,24,16,8,0,
        58,50,42,34,26,18,10,2,
        60,52,44,36,28,20,12,4,
        62,54,46,38,30,22,14,6]
rIP = [39,7,47,15,55,23,63,31,
        38,6,46,14,54,22,62,30,
        37,5,45,13,53,21,61,29,
        36,4,44,12,52,20,60,28,
        35,3,43,11,51,19,59,27,
        34,2,42,10,50,18,58,26,
        33,1,41, 9,49,17,57,25,
        32,0,40,8,48,16,56,24]
IPC = [56,48,40,32,24,16,8,0,
        57,49,41,33,25,17,9,1,
        58,50,42,34,26,18,10,2,
        59,51,43,35,62,54,46,38,
        30,22,14,6,61,53,45,37,
        29,21,13,5,60,52,44,36,
        28,20,12,4,27,19,11,3]
LS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,0]
PC = [13,16,10,23,0,4,
        2,27,14,5,20,9,
        22,18,11,3,25,7,
        15,6,26,19,12,1,
        40,51,30,36,46,54,
        29,39,50,44,32,47,
        43,48,38,55,33,52,
        45,41,49,35,28,31]
E = [31,0,1,2,3,4,
        3,4,5,6,7,8,
        7,8,9,10,11,12,
        11,12,13,14,15,16,
        15,16,17,18,19,20,
        19,20,21,22,23,24,
        23,24,25,26,27,28,
        27,28,29,30,31,0]
S = [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7, # S-0
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10, # S-1
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8, # S-2
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15, # S-3
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9, # S-4
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11, # S-5
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1, # S-6
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7, # S-7
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
P = [15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,
        1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]

def printList(ls):
    print(''.join([str(i) for i in ls]))

def intToBinary(n):
    dt = bin(n)[2:]
    ret = []
    for i in range((4 - (len(dt) % 4)) % 4):
        ret.append(0)
    for i in dt:
        ret.append(int(i))
    assert(len(ret) % 4 == 0)
    return ret

def convert(data, cvt):
    ret = [0 for i in range(len(cvt))]
    for i in range(len(cvt)):
        ret[i] = data[cvt[i]]
    return ret

def SBox(seq, i):
    # get binary string which is the index in the S Box
    l = "{}{}{}{}{}{}".format(seq[0], seq[5], seq[1], seq[2], seq[3], seq[4])
    assert(len(l) == 6)
    n = int(l, 2)
    ret = intToBinary(S[i][n])
    assert(len(ret) == 4)
    return ret

def F(x, k):
    assert(len(x) == 32)
    assert(len(k) == 48)
    t = convert(x, E)
    assert(len(t) == 48)
    # print("r0 extend with E in F")
    # printList(t)
    t = [t[i] ^ k[i] for i in range(len(t))]
    # print("Xor with key")
    # printList(t)
    ret = []
    for i in range(8):
        l = SBox(t[i * 6 : (i + 1) * 6], i)
        ret.extend(l)
    # print("SBox:")
    # printList(ret)
    ret = convert(ret, P)
    # print("P convert")
    # printList(ret)
    assert(len(ret) == 32)
    return ret

def round(ln, rn, workingkey):
    f_result = F(rn, workingkey)
    assert(len(f_result) == 32)
    assert(len(ln) == 32)
    assert(len(workingkey) == 48)
    assert(len(rn) == 32)
    rnn = [(ln[i] ^ f_result[i]) for i in range(len(ln))]
    assert(len(rnn) == 32)
    # print("round:")
    # print()
    return rn, rnn


def leftShift(data, n):
    l = len(data)
    if n == l:
        return data
    ret = data[n:]
    ret.extend(data[:n])
    assert(len(data) == len(ret))
    return ret


def getNextRoundKey(l, r, time, mode):
    if (0 == mode):
        shift = LS[time]
    else:
        shift = 28 - LS[16 - time]
    ln = leftShift(l, shift)
    rn = leftShift(r, shift)
    return ln, rn


def encryptOrDecrypt(text, cipher, mode):
    data = convert(text, IP)
    # print("convert text:")
    # printList(data)
    assert(len(data) == 64)
    if mode == 0:
        l0 = data[:32]
        r0 = data[32:]
    else:
        l0 = data[32:]
        r0 = data[:32]
    # print('l0 & r0:')
    # printList(l0)
    # printList(r0)
    key = convert(cipher, IPC)
    # print("convert key")
    # printList(key)
    assert(len(key) == 56)
    kl = key[:28]
    kr = key[28:]

    for i in range(16):
        kl, kr = getNextRoundKey(kl, kr, i, mode)
        # print(i + 1)
        # printList(kl)
        # printList(kr)
        assert(len(kl) == 28 and len(kr) == 28)
        tmp = kl[:]
        tmp.extend(kr)
        workingkey = convert(tmp, PC)
        # printList(workingkey)
        assert(len(workingkey) == 48)
        l0, r0 = round(l0, r0, workingkey)
    if 0 == mode:
        for i in range(28):
            assert(key[i] == kl[i])
        for i in range(28):
            assert(key[28 + i] == kr[i])
    if (0 == mode):
        data = l0[:]
        data.extend(r0)
    else:
        data = r0[:]
        data.extend(l0)
    assert(len(data) == 64)
    return convert(data, rIP)


def runDES(text, cipher, mode):
    '''
    input:
        text: bit(int) array with 64 bits
        cipher: bit(int) array with 64 bits
        mode: 0 encrypt or 1 decrypt
    output:
        output text: bit(int) array with 64 bits
    '''
    assert(len(text) == 64)
    assert(len(cipher) == 64)
    assert(mode == 0 or mode == 1)
    return encryptOrDecrypt(text, cipher, mode)



def strToList(eg):
    eg_list = []
    for i in eg:
        if not i.isdigit():
            continue
        eg_list.append(int(i))
    return eg_list

def listToStr(ls):
    return ''.join([str(i) for i in ls])


################# example of runDES function
# M = "0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111"
# K = "00010011 00110100 01010111 01111001 10011011 10111100 11011111 11110001"
# m_list = strToList(M)
# k_list = strToList(K)
# ciphertext = runDES(m_list, k_list, 0)
# decrypt_result = runDES(ciphertext, k_list, 1)

def encryptOrDecryptwithCBC(text, cipher, mode, IV):
    last = IV
    ret = []
    for i in range(0, len(text), 64):
        intext = text[i : i + 64]
        if 0 == mode:
            intext = [intext[j] ^ last[j] for j in range(64)]
        result = runDES(intext, cipher, mode)
        if 1 == mode:
            result = [result[j] ^ last[j] for j in range(64)]
            last = intext
        else:
            last = result[:]
        ret.extend(result)
    return ret

def runDESwithCBC(text, cipher, mode, IV):
    if 1 == mode:
        assert(0 == len(text) % 64)
    else:
        # Add zero paddings
        for i in range((64 - len(text) % 64) % 64):
            text.append(0)
    assert(len(IV) == 64)
    assert(len(cipher) == 64)
    return processListToStr(encryptOrDecryptwithCBC(text, cipher, mode, IV))

def processListToStr(ls):
    ret = ''
    for i in range(0, len(ls), 8):
        ret += ''.join([str(ls[i + j]) for j in range(8)])
        ret += ' '
    return ret

def getDESResult(text, cipher, mode, IV):
    text = strToList(text)
    cipher = strToList(cipher)
    IV = strToList(IV)
    status = 0
    result = ""
    if (len(cipher) != 64):
        status |= 1
        result += "密钥不是64位\n"
    if (len(IV) != 64):
        status |= 2
        result += "偏移量不是64位\n"
    if (1 == mode and 0 != len(text) % 64):
        status |= 4
        result += "密文内容错误，没有对齐64位\n"
    if 0 != status:
        return status, result
    return status, runDESwithCBC(text, cipher, mode, IV)
