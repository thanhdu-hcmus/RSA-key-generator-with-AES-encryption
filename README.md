# RSA-key-generation-AES-encryption

DISCLAIMER: All the screenshots are based in a Windows OS environment, so instead of "cat" command, I have used "type" command to view the files on cmd.

# genkeys.py

In this file, a name is given as an argument from the command line along with the script to run the file. This name is used to generate two files, one for storing the public key and other for storing the private key generated from the RSA key generation technique. The program starts with the generation of 2 large random prime numbers, p and q, using the Miller-Rabin's primality test algorithm. With this, the values of n and totient, t are calculated. Using the variables above, GCD and MOD Inverse was calculated to generate the public key, e and the private key, d. The values (n, e) are written in the public key file and the values (n, d) are written in the private key file. The key size used is 1024.

Sample commands to run the file "genkeys.py" :-

    py genkeys.py alice
    py genkeys.py bob

# crypt.py

In this file, we have used an argument parser to run the functions according to the selection between the encryption and decryption of a file. In the beginning, a random 16 bytes key is generated for AES-128 encryption. Then, the plaintext from the specified text file is encrypted using this key and the AES Encryption algorithm imported from the pyaes module. The key used for AES is then encrypted using the RSA public key from the previous file. Both, the cipher text and the encrypted AES key is written into a .cip file. For decryption, the .cip file is accessed along with the RSA private key. Using the private key, the encrypted AES key is decrypted for use in AES Decryption algorithm. The resulting file is stored in another file.

Sample commands to run the file "crypt.py" :-

    type message.txt
    py crypt.py -e bob.pub message.txt message.cip# RSA-key-generation-AES-encryption

DISCLAIMER: All the screenshots are based in a Windows OS environment, so instead of "cat" command, I have used "type" command to view the files on cmd.

# genkeys.py

In this file, a name is given as an argument from the command line along with the script to run the file. This name is used to generate two files, one for storing the public key and other for storing the private key generated from the RSA key generation technique. The program starts with the generation of 2 large random prime numbers, p and q, using the Miller-Rabin's primality test algorithm. With this, the values of n and totient, t are calculated. Using the variables above, GCD and MOD Inverse was calculated to generate the public key, e and the private key, d. The values (n, e) are written in the public key file and the values (n, d) are written in the private key file. The key size used is 1024.

Sample commands to run the file "genkeys.py" :-

    py genkeys.py alice
    py genkeys.py bob

# crypt.py

In this file, we have used an argument parser to run the functions according to the selection between the encryption and decryption of a file. In the beginning, a random 16 bytes key is generated for AES-128 encryption. Then, the plaintext from the specified text file is encrypted using this key and the AES Encryption algorithm imported from the pyaes module. The key used for AES is then encrypted using the RSA public key from the previous file. Both, the cipher text and the encrypted AES key is written into a .cip file. For decryption, the .cip file is accessed along with the RSA private key. Using the private key, the encrypted AES key is decrypted for use in AES Decryption algorithm. The resulting file is stored in another file.

Sample commands to run the file "crypt.py" :-

    type message.txt
    py crypt.py -e bob.pub message.txt message.cip

    type message.cip
    py crypt.py -d bob.prv message.cip secret.txt
    type secret.txt


    type message1.txt
    py crypt.py -e alice.pub message1.txt message1.cip

    type message1.cip
    py crypt.py -d alice.prv message1.cip secret1.txt
    type secret1.txt
    # RSA-key-generation-AES-encryption

DISCLAIMER: All the screenshots are based in a Windows OS environment, so instead of "cat" command, I have used "type" command to view the files on cmd.

# genkeys.py

In this file, a name is given as an argument from the command line along with the script to run the file. This name is used to generate two files, one for storing the public key and other for storing the private key generated from the RSA key generation technique. The program starts with the generation of 2 large random prime numbers, p and q, using the Miller-Rabin's primality test algorithm. With this, the values of n and totient, t are calculated. Using the variables above, GCD and MOD Inverse was calculated to generate the public key, e and the private key, d. The values (n, e) are written in the public key file and the values (n, d) are written in the private key file. The key size used is 1024.

Sample commands to run the file "genkeys.py" :-

    py genkeys.py alice
    py genkeys.py bob

# crypt.py

In this file, we have used an argument parser to run the functions according to the selection between the encryption and decryption of a file. In the beginning, a random 16 bytes key is generated for AES-128 encryption. Then, the plaintext from the specified text file is encrypted using this key and the AES Encryption algorithm imported from the pyaes module. The key used for AES is then encrypted using the RSA public key from the previous file. Both, the cipher text and the encrypted AES key is written into a .cip file. For decryption, the .cip file is accessed along with the RSA private key. Using the private key, the encrypted AES key is decrypted for use in AES Decryption algorithm. The resulting file is stored in another file.

Sample commands to run the file "crypt.py" :-

    type message.txt
    py crypt.py -e bob.pub message.txt message.cip

    type message.cip
    py crypt.py -d bob.prv message.cip secret.txt
    type secret.txt


    type message1.txt
    py crypt.py -e alice.pub message1.txt message1.cip

    type message1.cip
    py crypt.py -d alice.prv message1.cip secret1.txt
    type secret1.txt


    type message.cip
    py crypt.py -d bob.prv message.cip secret.txt
    type secret.txt


    type message1.txt
    py crypt.py -e alice.pub message1.txt message1.cip

    type message1.cip
    py crypt.py -d alice.prv message1.cip secret1.txt
    type secret1.txt
