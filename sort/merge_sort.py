
def merge_sort(nums):

    def sort(nums):

        if len(nums) <=1:
            return nums

        mid = len(nums) // 2
        left = sort(nums[:mid])
        right = sort(nums[mid:])
        return merge(left, right)

    def merge(left, right):

        arr = []
        i = 0
        j = 0
        while i <=len(left) or j <=len(right):
            if i >=len(left):
                arr += right[j:]
                break
            if j >=len(right):
                arr += left[i:]
                break
            if left[i] <= right[j]:
                arr.append(left[i])
                i+=1
            elif right[j] < left[i]:
                arr.append(right[j])
                j+=1
        return arr
    return sort(nums)


arr = [4,6,8,345,23,78,7,8,25,21,451,35]

print(merge_sort(arr))




