x = "ABCDGH"
y = "AEDFHR"
m, n = len(x), len(y)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
lcs = []
i, j = m, n
while i > 0 and j > 0:
    if x[i - 1] == y[j - 1]:
        lcs.append(x[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
print("Longest common subsequence:", ''.join(reversed(lcs)))
