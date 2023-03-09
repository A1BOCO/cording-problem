class Solution:
    def findKthLargest(self, nums,  k ) -> int:

        def partition(nums, start, end):

            i = start
            pivot_index = end
            pivot = nums[pivot_index]

            for j in range(start, end):

                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[end] = nums[end], nums[i]

            return i

        def quick_select(nums, start, end):

            partition_index = partition(nums, start, end)

            if partition_index == k - 1:
                return nums[partition_index]

            elif partition_index < k:
                return quick_select(nums, partition_index + 1, end)

            else:
                return quick_select(nums, start, partition_index - 1)

        return quick_select(nums, 0, len(nums) - 1)


solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))


