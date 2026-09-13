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


#Trapping rain water - Hard

def trap(height: list[int]) -> int:
    left = [0] * len(height)
    right = [0] * len(height) 
    lm = 0
    rm = 0
    res = 0
    for i in range(len(height)): 
        lm = max(lm, height[i])
        left[i] = lm
    for i in range(len(height) - 1, -1, -1):
        rm = max(rm, height[i])
        right[i] = rm
    for i in range(len(height)): 
        res += min(left[i], right[i]) - height[i]
    return res
        

print(trap([0,2,0,3,1,0,1,3,2,1]))

