'''
Task:- 
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''

'''
Example 1:-
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

'''
Example 2:-
Input: nums = [0,1,0,3,2,3]
Output: 4
'''

'''
Example 3:-
Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

'''
Constraints:-
 1 <= nums.length <= 2500
 -10^4 <= nums[i] <= 10^4
'''

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left = bisect.bisect_left(LIS, target)
            
            '''
            If not found, append the target.
            '''
            
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target
    
        for num in nums:
            insert(num)
        return len(LIS)