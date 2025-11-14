from fractions import Fraction
def get_fractions():
    a=int(input("Enter number of values needed="))
    f=[]
    for i in range(0,a):
        b=Fraction(input("Enter fraction="))
        f.append(b)
        pairs = [(x.numerator, x.denominator) for x in f]
    return pairs