#Write a code for optimal selection of items to maximize value within a weight constraint using bottom-up and top-down approaches.

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = len(weights)




def knapsack_bottom_up():
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    print("Bottom-Up DP Table:")
    for row in dp:
        print(row)

    print("Maximum Value (Bottom-Up):", dp[n][capacity])


memo = [[-1] * (capacity + 1) for _ in range(n + 1)]


def knapsack_top_down(i, w):

    
    if i == 0 or w == 0:
        return 0

    
    if memo[i][w] != -1:
        return memo[i][w]

   
    if weights[i - 1] > w:
        memo[i][w] = knapsack_top_down(i - 1, w)

    else:
        include = values[i - 1] + knapsack_top_down(
            i - 1, w - weights[i - 1]
        )

        exclude = knapsack_top_down(i - 1, w)

        memo[i][w] = max(include, exclude)

    return memo[i][w]




knapsack_bottom_up()

maximum_value = knapsack_top_down(n, capacity)

print("Maximum Value (Top-Down):", maximum_value)
