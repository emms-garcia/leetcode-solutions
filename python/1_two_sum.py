class Solution:
    """
    1. Two Sum

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            remainder = target - num
            j = num_to_index.get(remainder)
            if j is not None and i != j:
                return [i, j]
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
    assert Solution().twoSum([3,2,4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    print("Success!")
