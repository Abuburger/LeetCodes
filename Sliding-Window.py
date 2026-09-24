# Best Time to Buy and Sell Stock 

def maxProfit(prices: list[int]) -> int: 
    maxval = 0
    buy_price = prices[0]
    for i in range(len(prices)-1):
        if sellday > prices[i+1]:
            sellday = prices[i + 1]
        else:
            maxval = max(maxval, prices[i + 1] - sellday)
    return maxval


#Longest SubString Without Repeating Characters
 
def lengthOfLongestSubstring(s: str) -> int: 
    return 0