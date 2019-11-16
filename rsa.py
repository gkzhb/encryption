# RSA 加密算法

import random

primeTestRound = 32 # Miller-Rabin 检测轮数

def fastExpMod(b, e, m):
    '''
    快速幂取模
    '''
    result = 1
    while e != 0:
        if e & 1:
            result = (result * b) % m
        e >>= 1
        b = (b * b) % m
    return result

def extGCD(n, b):
    '''
    Extended Euclidean Algorithm
    n > b, b^{-1} = t (mod n)
    '''
    t = 0  # t_{j - 1}
    tt = 1 # t_{j}
    s = 1  # s_{j - 1}
    ss = 0 # s_{j}
    r = n  # r_{j - 1}
    rr = b # r_{j}
    while rr:
        q = r // rr
        tmp = rr
        rr = r % rr
        r = tmp
        
        tmp = tt
        tt = t - q * tt
        t = tmp
        
        tmp = ss
        ss = s - q * ss
        s = tmp
    return (r, t, s)


def testPrime(n):
    '''
    Miller-Rabin 检测质数
    '''
    m = n - 1
    k = 0
    
    while 0 == m & 1:
        k += 1
        m >>= 1
    
    a = random.randint(2, n-2)
    b = fastExpMod(a, m, n)
    if 1 == b:
        return True
    for j in range(k):
        if n - 1 == b:
            return True
        b = b * b % n
    return False

def testPrimeRound(n):
    '''
    多次执行 Miller-Rabin 检测质数
    '''
    for i in range(primeTestRound):
        if not testPrime(n):
            return False
    return True

def getPrime(length):
    '''
    获得一个 length 位的质数
    '''
    flag = False
    while not flag:
        x = random.randint(1 << (length - 1), 1 << length)
        flag = testPrimeRound(x)
    return x

def generateKeys(length=128):
    '''
    生成公钥和私钥
    '''
    if length < 10:
        length = 10
    p = getPrime(length)
    q = getPrime(length)
    n = p * q
    phi = (p - 1) * (q - 1)
    gcd = 2
    while 1 != gcd:
        e = getPrime(16) # e 取 16 位素数
        _, d, _ = extGCD(phi, e)
        gcd, _, _ = extGCD(phi, d)
    print(p, q)
    return (n, e, d)

def encryptRSA(m, n, e):
    '''
    RSA 加密
    '''
    return fastExpMod(m, e, n)

def decryptRSA(c, n, d):
    '''
    RSA 解密
    '''
    return fastExpMod(c, d, n)


