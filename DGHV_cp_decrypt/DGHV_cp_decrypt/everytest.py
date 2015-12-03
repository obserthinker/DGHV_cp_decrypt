# coding = utf-8

import random

class A:
    a = 1
    b = [2,3,4]

    def __del__(self):
        del self.a
        del self.b

D = A()
print D.a, D.b



