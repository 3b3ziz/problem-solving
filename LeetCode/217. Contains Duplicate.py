from __future__ import annotations

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurs = {}
        for n in nums:
            if n in occurs:
                return True
            else:
                occurs[n] = True
        return False

s = Solution()
print(s.containsDuplicate())