def maxProfit(prices):
  minimum = 10000
  maximum = 0
  profit = 0
  max_profit = 0
  
  for i in range(len(prices)):
      if i + 1 < len(prices):
          profit = prices[i+1] - prices[i]
          if  profit > 0:
              maxi = max(prices[i+1],prices[i])
              mini = min(prices[i+1],prices[i])
              maximum = maxi
              if mini < minimum:
                  minimum = mini
              profit = maximum - minimum
              max_profit = max(max_profit,profit)
              
  return max_profit


print(maxProfit([7,1,5,3,6,4])) # 5