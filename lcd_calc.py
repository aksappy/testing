from lcd_inp import get_fractions
import math
c=get_fractions()
deno = [d for (_, d) in c]
print("List of fractions=",c)
print("List of denominators",deno)
lcd = deno[0]
for d in deno[1:]:
    lcd = lcd * d // math.gcd(lcd, d)
print("Least Common Denominator =",lcd)