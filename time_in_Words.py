def timeInWords(h, m):
    words = {
        1: 'uma', 2: 'duas', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
        15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito',
        19: 'dezenove', 20: 'vinte', 21: 'vinte e uma', 22: 'vinte e duas',
        23: 'vinte e três', 24: 'vinte e quatro', 25: 'vinte e cinco',
        26: 'vinte e seis', 27: 'vinte e sete', 28: 'vinte e oito',
        29: 'vinte e nove', 30: 'trinta'
    }

    if m == 0:
        return f"{words[h]} em ponto"
    elif m == 15:
        return f"um quarto depois das {words[h]}"
    elif m == 30:
        return f"meia hora depois das {words[h]}"
    elif m == 45:
        return f"um quarto para as {words[(h % 12) + 1]}"
    elif m < 30:
        if m == 1:
            return f"um minuto depois das {words[h]}"
        else:
            return f"{words[m]} minutos depois das {words[h]}"
    else:
        if m == 59:
            return f"um minuto para as {words[(h % 12) + 1]}"
        else:
            return f"{words[60 - m]} minutos para as {words[(h % 12) + 1]}"


print(timeInWords(7, 22))
