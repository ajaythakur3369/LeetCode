'''
Task:-  
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

 answer[0] is a list of all players that have not lost any matches.
 answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
'''

'''
Example 1:-
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
'''

'''
Example 2:-
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
'''

'''
Constraints:-
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are unique.
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for a, b in matches:
            if a not in cnt:
                cnt[a] = 0
            cnt[b] += 1
        ans = [[], []]
        for u, v in cnt.items():
            if v < 2:
                ans[v].append(u)
        ans[0].sort()
        ans[1].sort()
        return ans
        