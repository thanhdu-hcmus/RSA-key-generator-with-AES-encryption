import os, sys, argparse
from time import time
from Crypto.Cipher import AES as KAES
from Crypto.Util import Counter as KCounter

def encrypt(pub_key, plain_text, secret_cip):

    n, e = open(pub_key, 'r').read().split(',')
    plain_text = open(plain_text, 'rb').read()

    aes_key = os.urandom(16)
    # cipher_text = pyaes.AESModeOfOperationCTR(aes_key).encrypt(plain_text)
    kaes = KAES.new(aes_key, KAES.MODE_CTR, counter = KCounter.new(128, initial_value = 0))
    cipher_text = kaes.encrypt(plain_text)

    p = int.from_bytes(aes_key, sys.byteorder)
    e, n = int(e), int(n)

    cipher_key = pow(p, e, n)
    cipher_key = bytes(str(cipher_key).encode())

    secret_file = open(secret_cip, 'wb')
    secret_file.write(b'%b %b' % (cipher_text, cipher_key))
    secret_file.close()
    #return plain_text

def decrypt(prv_key, secret_cip, plain_text):
    n, d = open(prv_key, 'r').read().split(',')
    c_items = open(secret_cip, 'rb').read().split(b' ')

    cipher_text = b' '.join(c_items[:-1])
    cipher_key = c_items[-1]
    cipher_key, d, n = int(cipher_key), int(d), int(n)

    aes_key = pow(cipher_key, d, n)
    # aes = pyaes.AESModeOfOperationCTR(aes_key.to_bytes(16, sys.byteorder))
    # decrypted = aes.decrypt(cipher_text)
    kaes2 = KAES.new(aes_key.to_bytes(16, sys.byteorder), KAES.MODE_CTR, counter = KCounter.new(128, initial_value = 0))
    decrypted = kaes2.decrypt(cipher_text)

    plain_text_file = open(plain_text, 'wb')
    plain_text_file.write(decrypted)
    plain_text_file.close()
    #return decrypted

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="My RSA Encryptor/Decryptor.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", help="Encrypt with public key")
    group.add_argument("-d", help="Decrypt with private key")

    parser.add_argument("source", help="Source File")
    parser.add_argument("destination", help="Destination File")

    args = parser.parse_args()

    if args.e:
        t0 = time()
        encrypt(args.e, args.source, args.destination)
        t_enc = time() - t0
        print(t_enc)
    elif args.d:
        t0 = time()
        decrypt(args.d, args.source, args.destination)
        t_dec = time() - t0
        print(t_dec)

