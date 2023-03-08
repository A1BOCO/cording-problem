import random


def quick_sort(arr):

    def partition(nums, start, end):

        i = start
        pivot_index = random.randint(start, end)
        pivot = nums[pivot_index]
        nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
        for j in range(start, end):

            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i],nums[end] = nums[end], nums[i]

        return i

    def sort_arr(nums, start, end):

        if start < end:

            partition_index = partition(nums, start, end)
            sort_arr(nums, start, partition_index - 1)
            sort_arr(nums,partition_index + 1, end)

    sort_arr(arr, 0, len(arr)-1)
    return arr

numbers = [3,6,4,9,1,5,3,3,12,56]

print(numbers)





