'''
Task:- 
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 10^9 + 7.
'''

'''
Example 1:- 
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
'''

'''
Example 2:- 
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
'''

'''
Constraints:- 
 1 <= n <= 1000
 0 <= k <= 1000
'''

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        f = [1] + [0] * k
        s = [0] * (k + 2)
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                f[j] = (s[j + 1] - s[max(0, j - (i - 1))]) % mod
            for j in range(1, k + 2):
                s[j] = (s[j - 1] + f[j - 1]) % mod
        return f[k]