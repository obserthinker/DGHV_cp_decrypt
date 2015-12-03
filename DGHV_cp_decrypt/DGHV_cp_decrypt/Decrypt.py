# -*- coding: utf-8 -*-

from Function.operations import *

def decrypt(cipher, secret_key):
    p = secret_key.sk
    #m = (c % p) % 2
    
    #print "************** Decrypt ***************"
    #print "c = ", cipher.c, "\t p = ", p, "\tx0 = ", cipher.x0
    m = residue( cipher.c, p)
    #print "c % p = ", m
    m = residue(m, 2)
    #print "c % p % 2 = ", m

    return m