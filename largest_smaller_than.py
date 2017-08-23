def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    if nums[0] > xnumber:
        return None
    for i in range(len(nums)):
        if nums[i] > xnumber:
            return i-1
            
            