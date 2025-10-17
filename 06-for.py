# for
planeta = 'Saturno'
for i in planeta:
    print(i)

# generara Error
# numero = 10
# for x in numero:
#    print(x)

# funcion range con for
# inicio
# fin: no lo contiene
# paso

for var in range(1, 11, 3):
    print(var)

# continue

for i in range(10):
    if i == 4:
        continue
    print(i)

# else: solo se ejecuta si el loop temrina finalmente

for x in range(20):
    print(x)
else:
    print('El loop termino')

''' ENUMERATE (enumerate) : obtener elemento e indice de un iterable '''

nombre = 'Camilo'

for v1, v2 in enumerate(nombre):
    print(f'Indice: {v1} --- letra: {v2}')

''' ZIP (zip): Recorrer 2 colecciones y obtiene el elemento de cada coleccion'''

saludo1 = 'buenas tardes'
saludo2 = 'ilehoikwehrnnh'

for s1, s2 in zip(saludo1, saludo2):
    print(f'{s1} --- {s2}')


''' REVERSE (reversed): itera en orden inverso '''

# for i in range(1, 7):
#     print(i)

for i in reversed(range(1, 7)):
    print(i)

for char in reversed('abcde'):
    print(char)


''' SORTED (sorted): Devuleve ordenado el iterable'''

cadena = '86542'
# cadena = 'zaolhgfjk'

# print(type(cadena))

for j in sorted(cadena):
    print(j)
