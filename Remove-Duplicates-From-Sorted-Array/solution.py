def removeDuplicates(nums):
    if not nums:  # Edge case: empty array
        return 0  

    k = 1  # Start from the first element (always unique)
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Found a unique element
            nums[k] = nums[i]  # Move it to the next position
            k += 1  # Increment the unique count
            
    return k  # Number of unique elements

# Example usage
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)

# Printing the result
print(f"Unique elements count: {k}")
print(f"Modified array: {nums[:k]}")  # Only first k elements matter
