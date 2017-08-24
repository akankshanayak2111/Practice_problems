def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    indices = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indices.append(i)

    return indices
