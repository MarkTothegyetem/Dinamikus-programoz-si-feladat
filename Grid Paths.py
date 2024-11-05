def count_paths(n, grid):
    MOD = 10**9 + 7
    dp = [[0] * n for _ in range(n)]
    
    if grid[0][0] == '.':
        dp[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
    
    return dp[n - 1][n - 1]


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    grid = data[1:n + 1]
    
    result = count_paths(n, grid)
    print(result)

if __name__ == "__main__":
    main()
