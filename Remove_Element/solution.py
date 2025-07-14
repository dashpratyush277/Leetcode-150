def removeElement(nums, val):
    k = 0  # Pointer for the next position to place a valid element

    for i in range(len(nums)):  # Loop through each element in nums
        if nums[i] != val:  # If the element is NOT equal to val
            nums[k] = nums[i]  # Move it to index k
            k += 1  # Move k to the next position
    
    return k  # Return count of elements that are not equal to val

# Example usage:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

k = removeElement(nums, val)
print("Output k:", k)  # Number of elements not equal to val
print("Modified nums:", nums[:k])  # First k elements are valid
