def carryOperations(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    len1 = len(num1)
    len2 = len(num2)

    if len1 > len2:
        num2 = num2.zfill(len1)
    else:
        num1 = num1.zfill(len2)
    carry = 0
    count = 0

    for i in range(len(num1)-1, -1,-1):
        sum = int(num1[i]) + int (num2[i]) + carry
        if sum >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

    if carry > 0:
        count += 1
    return count

print(carryOperations(123,456)) # 0
print(carryOperations(555,555)) # 3
print(carryOperations(123,594)) # 1
