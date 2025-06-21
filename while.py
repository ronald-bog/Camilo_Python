contador = 1
while contador <= 6:
    print(contador)

    # contador = contador + 1
    contador += 1

# break
count = 1
while count <= 6:
    print(count)
    break
    count += 1

countA = 0
while countA < 6:
    countA += 1
    if countA == 3:
        continue
    print(countA)
