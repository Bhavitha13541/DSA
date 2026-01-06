from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    obj = Solution()
    print(obj.missingNumber(nums))


# output:
# 2