def progressDays (treinos):
    dias_de_progresso = 0
    for i in range(len(treinos) -1):
        if treinos[i] < treinos[i + 1]:
            dias_de_progresso += 1
    return dias_de_progresso

print(progressDays([3,4,1,2]))