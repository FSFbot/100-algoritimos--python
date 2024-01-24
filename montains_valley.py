def landscapeType(lst):
    if len(lst) < 3:
        return 'neither'

    difs = [a - b for a, b in zip(lst[1:], lst[:-1])]
    peaks = [i for i in range(1, len(difs)) if difs[i-1] * difs[i] < 0]

    if len(peaks) != 1 or peaks[0] in {0, len(difs) - 1}:
        return 'neither'
    elif all(dif < 0 for dif in difs[:peaks[0]]) and all(dif > 0 for dif in difs[peaks[0]:]):
        return 'valley'  # corrigindo aqui
    elif all(dif > 0 for dif in difs[:peaks[0]]) and all(dif < 0 for dif in difs[peaks[0]:]):
        return 'mountain'  # corrigindo aqui
    else:
        return 'neither'

print(landscapeType([3,4,5,4,3]))
print(landscapeType([9,8,7,8,9]))

