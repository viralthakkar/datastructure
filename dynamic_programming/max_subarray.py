def max_subarray(nums):
    max_ending_here = 0
    max_so_far = float("-inf")
    start = 0
    end = 0
    window_index = 0
    for i in range(len(nums)):
        max_so_far += nums[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = window_index
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            window_index = i + 1

    return max_so_far, [start, end]


