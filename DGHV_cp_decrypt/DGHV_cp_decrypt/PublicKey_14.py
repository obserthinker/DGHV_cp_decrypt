# -*- coding: utf-8 -*-

import random
from parameters import *
from Function.operations import residue

class Public_Key:
    """Generate the public key"""

    x0 = 0
    seq_pk = []
    seq_q = []
    seq_r = []
    def __init__(self, Par, SK):
        tau = Par.tau
        gamma = Par.gamma
        rho = Par.rho
        eta = Par.eta
        p = SK.sk
        # seq_q = range( 0, int((2 ** gamma) / p) ) # 这是q取值的理论范围。但是该范围太大以至于程序不能生成该序列
        init_q = range( 2 ** eta, 2 ** (eta + 1)) # q取值的实际范围，比p大即可
        init_r = range( - 2 ** rho + 1, 2 ** rho )
        
        self.seq_r = random.sample(init_r, tau)

        running = True
        while running:
            self.seq_q = random.sample(init_q, tau+1)
            
            max_q = max(self.seq_q)
            self.x0 = max_q * p
            if self.x0 % 2 == 1:
                running = False
                self.seq_q.remove(max_q)
            else:
                del self.seq_q[:]

        for i in range(0, tau):
            self.seq_pk.append(self.seq_q[i] * p + self.seq_r[i])
           
        #print u"公钥：\n", self.seq_pk
        #print "q[] = ", self.seq_q
        #print "r[] = ", self.seq_r
        #print "x0 = ", self.x0

    def clean(self):
        del self.seq_pk[:]
        del self.seq_q[:]
        del self.seq_r[:]
        del self.x0