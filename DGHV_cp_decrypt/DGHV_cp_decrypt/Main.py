# -*- coding: utf-8 -*- 

from parameters import *
from SecretKey import *
#from PublicKey import *
from PublicKey_14 import *
from __builtin__ import max
from Function.operations import residue
from Encrypt import *
from Decrypt import *


# 安全参数
lbda = 3

# 生成各个控制参数
parameters = Par(lbda)

# 生成私钥和公钥
secret_key = Secret_Key(parameters.eta)
# print bin(sk.sk)
public_key = Public_Key(parameters, secret_key)

A = 1
#B = 0

A_cipher = encrypt(A, public_key, parameters, secret_key)
#B_cipher = encrypt(A, public_key, parameters, secret_key)
#cipher = Cipher()
#cipher.c = A_cipher.c+B_cipher.c
result_decipher = decrypt(A_cipher, secret_key)
if result_decipher == A:
    print "Right!\t"

parameters.clean()
secret_key.clean()
public_key.clean()
