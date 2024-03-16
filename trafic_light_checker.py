def check_sequence(sequence):
    valid_codes =['R', 'G', 'Y', 'P', 'C', 'X']
    last_code = None
    if len (sequence) > 15 or len(sequence) < 1:
        return 'Erro'
    if sequence[0] != 'R':
        return 'Reject'
    for code in sequence:
        if code not in valid_codes:
            return 'ERROR'
        if last_code == code:
            return 'Reject'
        if last_code == 'P' and code != 'R':
            return 'Reject'
        if last_code == 'C' and code != 'R':
            return 'Reject'
        last_code = code
    return 'Accept'

# Exemplo 1: Sequência válida
print(check_sequence('R G Y R C R G Y R'.split()))

# Exemplo 2: Sequência inválida - não começa com R
print(check_sequence('G Y R G Y R'.split()))

# Exemplo 3: Sequência inválida - sequência inválida
print(check_sequence('R Y G P'.split()))

# Exemplo 4: Sequência inválida - código indefinido
print(check_sequence('X 8 S'.split()))

# Exemplo 5: Sequência inválida - muito longa
print(check_sequence('R G Y R C R P R G Y R G Y R G Y R'.split()))
