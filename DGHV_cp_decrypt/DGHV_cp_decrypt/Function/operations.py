# coding = utf-8

def quotient(dividend,divisor):
    if dividend % divisor > divisor/2.0:
        quotient = (dividend / divisor) + 1
    else:
        quotient = dividend / divisor

    return quotient

def residue(z, p):
    res = z - quotient(z, p) * p
    return res