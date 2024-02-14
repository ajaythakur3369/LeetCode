'''
Task:- 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

'''
Example 1:-
Input: nums = [3,2,3]
Output: 3
'''

'''
Example 2:-
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

'''
Constraints:-
 n == nums.length
 1 <= n <= 5 * 10^4
 -10^9 <= nums[i] <= 10^9
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = m = 0
        for v in nums:
            if cnt == 0:
                m, cnt = v, 1
            else:
                cnt += 1 if m == v else -1
        return m if nums.count(m) > len(nums) // 2 else -1