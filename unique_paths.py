def uniquePaths(m,n):
    dp = [[1]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(3, 3))