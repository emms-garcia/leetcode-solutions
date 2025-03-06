class Solution:
    """
    217. Contains Duplicate

    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


if __name__ == "__main__":
    assert not Solution().containsDuplicate([])
    assert Solution().containsDuplicate([1,2,3,1])
    assert not Solution().containsDuplicate([1,2,3,4])
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    print("Success!")
