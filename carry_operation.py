def carryOperations(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    carry = 0
    carry_count = 0
    
    len_diff = len(num1) - len(num2)
    if len_diff > 0:
        num2 = '0' * len_diff + num2
    elif len_diff < 0:
        num1 = '0' * -len_diff + num1
        
    for i in range(len(num1)-1, -1,-1):
        total = int(num1[i]) + int(num2[i]) + carry
        if total > 9:
            carry = 1
            carry_count += 1
        else:
            carry = 0
            
    return carry_count

def test_carryOperations():
    assert carryOperations(123, 456) == 0
    assert carryOperations(555, 555) == 3
    assert carryOperations(123, 594) == 1
    assert carryOperations(555, 545) == 3
    assert carryOperations(1, 20000) == 0
    assert carryOperations(1, 2) == 0
    print("All tests passed.")

test_carryOperations()
