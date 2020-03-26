import multiprocessing
import math

'''
This is more multiprocessed than multithreaded.
'''
def multi_merge_sort(input):
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes = processes)
    batch_size = math.ceil(len(input) / processes)
    batches = []

    for i in range(4):
        batch = input[i * batch_size : (i + 1) * batch_size]
        batches.append(batch)
    batches = pool.map(merge_sort, batches)

    while len(batches) > 1:
        new_batches = []
        for i in range(0, len(batches), 2):
            new_batches.append(helper(batches[i], batches[i + 1]))
        batches = new_batches

    return batches[0]

    def helper(left, right):
    left_i = 0
    right_i = 0
    out = []

    while left_i < len(left) and right_i < len(right):
        left_val = left[left_i]
        right_val = right[right_i]

        if left_val < right_val:
            out.append(left_val)
            left_i += 1
        else:
            out.append(right_val)
            right_i += 1

    if left_i < len(left):
        out += left[left_i:]
    else:
        out += right[right_i:]

    return out

def merge_sort(input):
    l = len(input)
    if l <= 1:
        return input

    mid = l // 2
    left = merge_sort(input[:mid])
    right = merge_sort(input[mid:])

    return helper(left, right)