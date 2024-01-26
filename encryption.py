def Encrypty(input_string):

    reversed_string = input_string[::-1]

    tranlation_table = str.maketrans('aeiou','01223')
    replaced_string = reversed_string.translate(tranlation_table)

    encrypted_string = replaced_string + 'aca'

    return encrypted_string


print(Encrypty("banana"))

