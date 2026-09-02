"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Arrays & Hashing

Approach:
- Use a hashmap to store each number's index as we iterate.
- For each number, check if (target - number) has already been seen.
- If yes, we found the pair. If no, store the current number and move on.
- This avoids the O(n^2) brute force of checking every pair.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # expected [0, 1]
    print(two_sum([3, 2, 4], 6))       # expected [1, 2]
