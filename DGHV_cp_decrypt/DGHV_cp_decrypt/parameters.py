# coding = UTF-8

from math import *

class Par:
    def __init__(self, lbda):
        '''生成密钥时所用的所有参数

        rho：噪音的bit-length
        eta：私钥的bit-length
        gamma：公钥中元素的bit-length
        tau：公钥中元素个数

        在压缩解密电路所用参数
        k : 
        ltheta : 
        utheta : 
        '''
        #生成密钥时所用的所有参数
        self.rho = (int)(lbda)
        self.eta = (int)(lbda**2 * log(lbda, 2))
        self.gamma = int(lbda**5 * log(lbda, 2))
        # self.tau = int(self.gamma + lbda) # in theory
        self.tau = 2 # in practice

        #在压缩解密电路所用参数
        # self.k = self.gamma * self.eta / (2 * self.rho) # in theory
        self.k = self.gamma + 2 # in practice
        self.ltheta = lbda
        self.utheta = self.k * lbda

        print u"************* 参数 **************"
        print u"安全参数为 (lambda)：", lbda
        print u"公钥元素个数 (tau)：", self.tau
        print u"公钥元素的bit-length (gamma)：", self.gamma
        print u"私钥的bit-length (eta)：", self.eta
        print u"噪音的bit-length (rho)：", self.rho
        print u"k : ", self.k
        print u"l theta : ", self.ltheta
        print u"u theta : ", self.utheta

    def clean(self):
        del self.gamma
        del self.rho
        del self.tau
        del self.eta