def max_possible_value(N,D):
    is_negative = False
    if N < 0:
        is_negative = True
        N = -N

    N = str(N)
    D = str(D)

    for i in range(len(N)):
        if(not is_negative and N[i] < D) or (is_negative and N[i] > D):
            return int(N[:i] + D + N[i:]) * (-1 if is_negative else 1)

    return int (N+ D) * (-1 if is_negative else 1)

print(max_possible_value(276,3))
