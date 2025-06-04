# operadores aritmeticos / // % * + - 

# operadores de comparacion relacionales
# > < >= <= == != # retorna un bool

# Operadores Logicos # retorna un bool
# and Si primer valor Y(and) segundo son verdaderos resultado verdadero
print(True and True)
print(False and True)
print(True and False)
print(False and False)

print(True or True)
print(False or True)
print(True or False)
print(False or False)

# or
# not

print(not True)

print(not 10 > 5 and 4 < 3)

print(3 == 3 and 4 < 7 and 10 == 10)

# Operadores pertenecia: in / not in
# Solo es aplicable en iterable
# retorna un bool

saludo = "Hola"

print("i" in saludo)

# Truthy y Falsy

print(bool(6))
print(bool(""))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(()))
print(bool(set()))


