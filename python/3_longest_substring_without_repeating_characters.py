class Solution:
    """
    3. Longest Substring Without Repeating Characters

    Given a string s, find the length of the longest substring without duplicate characters.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        i = 0
        result = 0
        for j in range(len(s)):
            c = s[j]
            if c in char_to_index:
                i = max(char_to_index[c], i)

            result = max(result, j - i + 1)
            char_to_index[c] = j + 1

        return result


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    print("Success!")
