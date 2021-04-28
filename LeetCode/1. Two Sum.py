from __future__ import annotations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [idx, dic[diff]]
            else:
                dic[n] = idx

s = Solution()
print(s.twoSum([2,7,11,15], 9))
