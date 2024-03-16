def trap(height):
    if not height:
        return 0

    ans = 0
    size = len(height)
    left_max = [0]*size
    right_max = [0]*size
    left_max[0] = height[0] # alterado aqui
    right_max[size - 1] = height[size - 1]

    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i - 1])

    for i in reversed(range(size - 1)):
        right_max[i] = max(height[i], right_max[i + 1])

    for i in range(1, size - 1):
        ans += min(left_max[i], right_max[i]) - height[i]

    return ans

height = [4,2,0,3,2,5]
result = trap(height)

print(result)