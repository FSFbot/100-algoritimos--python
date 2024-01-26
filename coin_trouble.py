def coinsDiv(coins):
    total = sum(coins)
    if total % 3 != 0:
        return False
    target = total // 3

    def helper(coins, n, target1, target2, target3):
        if target1 == 0 and target2 == 0 and target3 == 0:
            return True
        if n < 0:
            return False
        return (helper(coins, n - 1, target1 - coins[n], target2, target3) or
                helper(coins, n - 1, target1, target2 - coins[n], target3) or
                helper(coins, n - 1, target1, target2, target3 - coins[n]))

    return helper(coins, len(coins) - 1, target, target, target)

def test_coinsDiv():
    assert coinsDiv([1, 2, 3, 2, 2, 2, 3]) == True
    assert coinsDiv([5, 3, 10, 1, 2]) == False
    assert coinsDiv([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) == True
    assert coinsDiv([1, 1, 1, 2, 2, 2, 6]) == True
    assert coinsDiv([1, 1, 2, 2, 2, 2, 6]) == False
    assert coinsDiv([]) == True
    print("All tests passed.")

test_coinsDiv()