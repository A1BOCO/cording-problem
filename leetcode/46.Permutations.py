from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(pos, tmp):

        if len(tmp) == len(nums):
            ans.append(tmp.copy())
            return

        for i in range(0, len(nums)):
            if not nums[i] in tmp:
                tmp.append(nums[i])
                backtrack(i, tmp)
                tmp.pop()

    ans = []
    backtrack(0, [])
    return ans

print(permute([1,2,3]))