def SocksPairs(meias):
    pares = 0;
    tipo_de_meias =set(meias)
    for meia in tipo_de_meias:
        pares += meias.count(meia) // 2
    return pares

print(SocksPairs("AA"))
print(SocksPairs("ABABC"))
print(SocksPairs("CABBACCC"))