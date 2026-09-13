# Best Time to Buy and Sell Stock 

prices=[5,1,5,6,7,1,10]
def maxProfit(prices: list[int]) -> int: 
    maxval = 0
    sellday = prices[0]
    for i in range(len(prices)-1):
        if sellday > prices[i+1]:
            sellday = prices[i + 1]
        else:
            maxval = max(maxval, prices[i + 1] - sellday)
    return maxval 
        


print(maxProfit(prices)) 
        
