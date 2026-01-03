from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # position for next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]   # test input

    obj = Solution()
    obj.moveZeroes(nums)     # function modifies list in-place

    print(nums)


# output:
# [1, 3, 12, 0, 0]