def conta_espetos(grelha):
    vegetarianos = 0
    nao_vegetarianos = 0
    for espetos in grelha:
        if '-x' in espetos:
            nao_vegetarianos =+ 1
        else:
            vegetarianos += 1;
    return [vegetarianos, nao_vegetarianos]

