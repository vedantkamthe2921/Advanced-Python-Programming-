#9. 0/1 Knapsack Problem
#Develop a Python program to determine the maximum value that can be carried in a bag of limited capacity.

weights = list(map(int, input("Enter item weights: ").split()))
values = list(map(int, input("Enter item values: ").split()))
capacity = int(input("Enter bag capacity: "))
n = len(weights)
dp = [[0] * (capacity + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
for w in range(1, capacity + 1):
if weights[i - 1] <= w:
dp[i][w] = max(
values[i - 1] + dp[i - 1][w - weights[i - 1]],
dp[i - 1][w]
)
else:
dp[i][w] = dp[i - 1][w]
print("Maximum obtainable value:", dp[n][capacity])
