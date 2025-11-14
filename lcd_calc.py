from lcd_inp import get_fractions
import math
c=get_fractions()
deno = [d for (_, d) in c]
print("Fractions=",c)
print("Denominators=",deno)
lcd = deno[0]
for d in deno[1:]:
    lcd = lcd * d // math.gcd(lcd, d)
print("Least Common Denominator =",lcd)