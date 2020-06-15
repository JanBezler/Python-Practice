import math

print(math.dist((2, 5), (1, 6)))  # odległość w 2 wymiarach
print(math.dist((1, 0), (6, 0)))  # odległość w 1 wymiarze
# rel_tol=0,5 - ile razy mniejsza #  abs_tol=5 - o ile mniejsza
print(math.isclose(5, 10, abs_tol=5))

print(math.fabs(-3))  # bezwzględna float
print(abs(-2))  # bezwzględna int

print(math.factorial(5))  # silnia
print(math.fsum([2, 5.3, 1.4]))  # suma float
print(math.gcd(9, 6))  # Największy wspólny dzielnik NWD
