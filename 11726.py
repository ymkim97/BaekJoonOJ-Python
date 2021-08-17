import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2] + [0 for _ in range(n)]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)