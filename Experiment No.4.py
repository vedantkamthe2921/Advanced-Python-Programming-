# Fibonacci using Memoization (Top-Down)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    # Base cases
    if n <= 1:
        return n

    # Return already calculated value
    if n in memo:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# Fibonacci using Tabulation (Bottom-Up)

def fibonacci_tab(n):
    if n <= 1:
        return n

    # Create DP table
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    # Fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main program
n = int(input("Enter n: "))

print("Fibonacci using Memoization:", fibonacci_memo(n))
print("Fibonacci using Tabulation:", fibonacci_tab(n))
