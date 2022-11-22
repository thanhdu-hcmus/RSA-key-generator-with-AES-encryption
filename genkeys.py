import os, random, sys

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def rabinMiller(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True

def isPrime(num):
    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num)

def Random(bits):
	a = random.getrandbits(bits)
	a = a | (1 << (bits-1))
	a = a | 1
	return a;

def generateLargePrime(keysize = 1024):
    while True:
        # num = random.randrange(2**(keysize-1), 2**(keysize))
        num = Random(keysize)
        if isPrime(num):
            return num

def generateKey(keySize):
    p = generateLargePrime(keySize)
    q = generateLargePrime(keySize)
    n = p * q
    t = (p - 1) * (q - 1)

    while True:
        # e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        d = random.getrandbits(keySize)
        d = d | (1 << (round(keySize/4)-1))
        d = d | 1
        if gcd(d, t) == 1:
            break

    e = findModInverse(d, t)
    publicKey = (n, e)
    privateKey = (n, d)
    #print('Public key:', publicKey)
    #print('Private key:', privateKey)
    print(f"Total bits in n: {count_bits(p)}")
    print(f"Total bits in p: {count_bits(p)}")
    print(f"Total bits in q: {count_bits(q)}")
    print(f"Total bits in d: {count_bits(e)}")
    print(f"Total bits in e: {count_bits(d)}")

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    publicKey, privateKey = generateKey(keySize)

    pubFile = open('%s.pub' % (name), 'w+')
    pubFile.write('%s,%s' % (publicKey[0], publicKey[1]))
    pubFile.close()

    prvKey = open('%s.prv' % (name), 'w+')
    prvKey.write('%s,%s' % (privateKey[0], privateKey[1]))
    prvKey.close()

# function to count the number of bits in a number n
def count_bits(n):
  # bin(n) returns a binary string representation of n preceded by '0b' in python
  binary = bin(n)

  # we did -2 from length of binary string to ignore '0b'
  return len(binary)-2

if __name__ == '__main__':
    size = 1024
    # name = 'alice'
    name = sys.argv[1]
    makeKeyFiles(name, size)
