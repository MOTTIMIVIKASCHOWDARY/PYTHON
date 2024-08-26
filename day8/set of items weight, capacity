def knapsack(items, capacity):
  dp=[0]*(capacity+1)
  for weight, value in items:
    for Win range(capacity, weight -1,-1):
       dp[W]= max(dp[W], dp[W-weight]+value)
    return dp[-1]
items=[(2,3),(3,4),(4,5),(5,6)]
capacity=5
print(knapsack(items, capacity))
