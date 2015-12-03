from parameters import *
from random import *

class Secret_Key:
    """Generate the secrec key"""

    def __init__(self, eta):
        seq = range(2 ** (eta - 1), 2 ** eta)
        # print seq
        #print "[", 2 ** (eta - 1), " ", 2 ** eta, "]"
        seq = [i for i in seq if i % 2 == 1]
        #print seq
        self.sk = choice(seq)
        #print u"私钥 p 为：", self.sk

    def clean(self):
        del self.sk


