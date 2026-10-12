#Binary Search 
def search(nums: list[int], target: int) -> int:
    low = 0 
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2 
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target: 
            high = mid - 1 
        else: 
            return mid
    return -1 




#Search a 2D Matrix 
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    s_list = []
    for lists in matrix:
        if lists[-1] < target: 
            continue 
        s_list = lists
        break
    if search(s_list, target) == -1:
        return False
    return True

