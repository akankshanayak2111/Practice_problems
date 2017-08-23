def lucky_nums(n):

    list_nums = []

    nums = range(1, 11)

    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        list_nums.append(num)
    return list_nums
    