#!/usr/bin/env python

import hashlib
import base64

from Crypto import Random
from Crypto.Cipher import AES


key = hashlib.sha256('SOME_KEY'.encode()).digest()


def pad(v):
    bs = 32
    return v + (bs - len(v) % bs) * chr(bs - len(v) % bs)


def unpad(s: str) -> str:
    return s[:-ord(s[len(s) - 1:])]


def encrypt(value):
    value = pad(value)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = base64.b64encode(iv + cipher.encrypt(value.encode('utf-8'))).decode('utf-8')
    return encrypted


def decrypt(value):
    value = base64.b64decode(value)
    iv = value[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(value[AES.block_size:])).decode('utf-8')


def format_output_string(value):
    return f'PYCRYPTO: {value}\n'


if __name__ == '__main__':
    val = encrypt("value")
    with open('/files/encryption.txt', 'a') as file:
        file.write(format_output_string(f'encryption of "value": {val}'))
        file.write(format_output_string(f'decryption: {decrypt(val)}'))
        file.write(format_output_string(f'decryption of pycrypto encrypted value: {decrypt("ARtvLBk1r51F8k4Y6SEDMEBwPRsRG0TmXz5rkd8ofB1/FRDl1/pCCY3gKpC5Jt0I")}'))
