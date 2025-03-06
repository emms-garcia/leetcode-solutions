class Solution:
    """
    238. Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == "__main__":
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    print("Success!")
