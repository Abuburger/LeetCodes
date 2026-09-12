# Container With Most Water
def maxArea(heights: list[int]) -> int: 
    low = 0
    high = len(heights) - 1
    maximum = 0
    while low < high:
        height = min(heights[low], heights[high])
        area = (high - low) * height
        maximum = max(maximum, area)
        if heights[low] <= heights[high]:
            low += 1
        else:
            high -= 1
        
    return maximum

print(maxArea([2, 2, 2]))
