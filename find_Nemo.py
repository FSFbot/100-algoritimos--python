def findNemo(sentence):
    words = sentence.split()
    if 'Nemo' in words:
        position = words.index('Nemo') + 1
        return f'Eu encontrei o Nemo na posição {position} !'
    else:
        return 'Eu não consegui encontrar o nemo :('


print(findNemo('Eu estou procurando Nemo'))
print(findNemo('Ainda estou procurando  o tal do Nemo'))

