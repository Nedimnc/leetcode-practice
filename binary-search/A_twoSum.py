"""
Problem: Two Sum (Binary Search Approach)
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Binary Search

Approach:
- Store each number with its original index, then sort the list by value.
- For each number, calculate what we need: (target - number).
- Use binary search on the rest of the array to find that needed value.
- Searching only to the right ensures we never use the same index twice.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    # we pair each number with its starting position so we don't lose where it came from, then sort lowest to highest
    indexed_nums = sorted((num, i) for i, num in enumerate(nums)) 
    n = len(indexed_nums)                                         # total count of items in the list

    for i in range(n):                                            # pick each number one by one
        complement = target - indexed_nums[i][0]                  # the missing value we need to hit target (target - current)
        left = i + 1                                              # only look at items to the right so we don't reuse the same element
        right = n - 1                                             # the end boundary of our search space

        while left <= right:                                      # keep cutting the search space in half until boundaries cross
            mid = (left + right) // 2                             # find the middle position
            
            if indexed_nums[mid][0] == complement:                # did we hit the exact number we were looking for?
                return [indexed_nums[i][1], indexed_nums[mid][1]] # if yes, return both original starting indices
            elif indexed_nums[mid][0] < complement:               # if the middle number is too small...
                left = mid + 1                                    # throw away the left half and shift search right
            else:                                                 # if the middle number is too big...
                right = mid - 1                                   # throw away the right half and shift search left

    return []                                                     # if no two numbers add up to target, return empty list


if __name__ == "__main__":                                        # quick manual test in terminal
    print(two_sum([2, 7, 11, 15], 9))                             # expected [0, 1]
    print(two_sum([3, 2, 4], 6))                                  # expected [1, 2]
    print(two_sum([3, 5, 8, 9], 17))                              # expected [2, 3]