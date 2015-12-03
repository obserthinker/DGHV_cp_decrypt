# coding = utf-8

import random
from Function.operations import *

class Cipher:

    noise = 0
    m = 0
    c = 0
    sum = 0
    x0 = 0

    def clean(self):
        del self.noise
        del self.m
        del self.c
        del self.sum
        del self.x0


def encrypt(m, public_key, Par, secret_key):
    # get the m
    cipher = Cipher()
    cipher.m = m

    #get the sum part
    pk = public_key.seq_pk
    p = secret_key.sk
    #Subset_norm = random.randrange(1, len(pk))
    #Subset = random.sample(pk, Subset_norm)
    Subset = public_key.seq_pk
    cipher.sum = sum(Subset)

    # get the r 
    rho_ = Par.rho * 2
    noise = random.randrange(-(2 ** rho_), 2 ** rho_)
    cipher.noise = noise

    x0 = public_key.x0
    cipher.c = residue(( m + 2 * noise + 2 * sum(Subset) ), x0)
    cipher.x0 = x0

    #print "\n******************* Encrypt ********************"
    #print "noise = ", noise, 2*noise
    #print "sum(Subset) = ", sum(Subset), 2*sum(Subset)
    #print "m + 2 * noise = ", m + 2 * noise
    #print "x0 = ", x0
    #check_c = m + 2*noise + residue( 2*( p * sum(public_key.seq_q) + sum(public_key.seq_r) ), x0)
    #print "2*sum(Subset) % x0 = ", residue( 2 * sum(Subset),  x0)
    #cipher.sum = residue( 2 * sum(Subset),  x0)
    
    #print u"密文为：", cipher.c
    return cipher