def prisioneiros_liberados(celulas):
    if celulas[0] == 0:
        return 0

    prisioneiros_liberados = 1
    for i in range(1, len(celulas)):
        if celulas[i] == 0:
            break
        prisioneiros_liberados += 1
        celulas = [1 - celula for celula in celulas]

    return prisioneiros_liberados


print(prisioneiros_liberados([1, 1, 0, 0, 0, 1, 0]))  # Deve retornar 4
print(prisioneiros_liberados([1, 1, 1]))  # Deve retornar 1
print(prisioneiros_liberados([0, 0, 0]))  # Deve retornar 0
print(prisioneiros_liberados([0, 1, 1, 1]))  # Deve retornar 0