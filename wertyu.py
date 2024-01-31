def keyboardMistakeFix(input):
    keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
    output = ''
    for char in input:
        if char == ' ':
            output += ' '
        else:
            output += keyboard[keyboard.index(char) - 1]
    return output
def test_keyboardMistakeFix():
    result = keyboardMistakeFix("O S, GOMR YPFSU/")
    print(result)  # print the result
    assert result == "I AM FINE TODAY."
    # rest of the tests...


test_keyboardMistakeFix()