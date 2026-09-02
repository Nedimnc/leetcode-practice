"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum
Difficulty: Easy
Pattern: Hash Map / Complment Lookup

Approach: The bruteway to force it would be to use a nested loop to check all the elements in the array. But keeping time complexity in mind,  we can use a hash table to store the elements and check for the required condition in O(n) time.

-- Complement: Instead of searching for 'x + y = target' we search for the complement 'x = target - y' and check if it exists in the hash table. If it does, we found our pair. Y is what we NEED.
-- Hash Map: I used a hashmap because lookup is O(1), compared to looking up an item in a list being O(n). In examples like these the difference is negligible, but in larger datasets it can be significant.
-- One-Pass trick: Instead of populating the whole hash table first and THEN checking the complement, its better to do it in one pass. This also prevents using the same index twice (not allowed in this problem).

Time Complexity: O(n) -> because for loop iterates through the array once and hash table lookups are O(1). Total Time = n iterations * O(1) per interation = O(n).
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}                           #value -> index (hashmap to store each number's index as we interate)
        for i, num in enumerate(nums):      #for each number
            complement = target - num       #check if the target - number
            if complement in seen:          #has already been seen -> if no, the current number is stored and we move on
                return[seen[complement], i] #if yes
            seen[num] = i
        return []                           #return the found pair


if __name__ == "__main__":                  #quick manual test in terminal
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # expected [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # expected [1, 2]
    print(solution.twoSum([3,5,8,9], 17))      # expected [2, 3]