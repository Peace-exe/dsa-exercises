#lc121
'''
def maxProfit(prices: list[int])->int:
    
  minPrice=float('inf')
  maxProfit = 0

  for price in prices:

    if price<minPrice:
      minPrice=price
    
    profit=price-minPrice

    if profit>maxProfit:
      maxProfit=profit

  return maxProfit

'''

def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0

    minPrice = prices[0]
    maxProfit = 0

    for price in prices[1:]:
        if price < minPrice:
            minPrice = price
        else:
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit

print(maxProfit([2,4,1]))