"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Pattern: Arrays & Hashing / Frequency Count

Approach: The brute way is to sort both strings and compare them — works, but sorting costs O(n log n). Since an anagram is just the same letters with the same counts, we can use a hash map to track how many times each character appears.

-- Length check: If s and t aren't the same length, they can't be anagrams — bail out early.
-- Count up: Walk through s and increment the count for each character in the map.
-- Count down: Walk through t and decrement the same keys. If a char in t isn't in the map (or goes negative), it's not an anagram.
-- All zeros: If every count in the map is 0, both strings used exactly the same letters.

Time Complexity: O(n) -> three linear passes (length check + two loops), hash map ops are O(1) average.
Space Complexity: O(1) -> at most 26 keys for lowercase English letters (O(k) if we count distinct charset size).
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):                #different lengths -> can't be anagrams
            return False

        count = {}                          #char -> how many times we've seen it (net balance s vs t)

        for c in s:                         #build counts from the first string
            count[c] = count.get(c, 0) + 1

        for c in t:                         #cancel out with the second string
            if c not in count:              #t has a letter s never had
                return False
            count[c] -= 1
            if count[c] < 0:                #t used that letter more times than s had
                return False

        return True                         #every count should be 0 if we never returned early


if __name__ == "__main__":                  #quick manual test in terminal
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # expected True
    print(solution.isAnagram("rat", "car"))          # expected False
    print(solution.isAnagram("a", "ab"))             # expected False
