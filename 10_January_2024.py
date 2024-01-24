'''
Task:-
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:
 The node is currently uninfected.
 The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
'''

'''
Example 1:- 
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
'''

'''
Example 2:- 
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
'''

'''
Constraints:- 
 The number of nodes in the tree is in the range [1, 10^5].
 1 <= Node.val <= 10^5
 Each node has a unique value.
 A node with a value of start exists in the tree.
'''

'''
Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
'''

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(root):
            if root is None:
                return
            if root.left:
                g[root.val].append(root.left.val)
                g[root.left.val].append(root.val)
            if root.right:
                g[root.val].append(root.right.val)
                g[root.right.val].append(root.val)
            dfs(root.left)
            dfs(root.right)

        g = defaultdict(list)
        dfs(root)
        vis = set()
        q = deque([start])
        ans = -1
        while q:
            ans += 1
            for _ in range(len(q)):
                i = q.popleft()
                vis.add(i)
                for j in g[i]:
                    if j not in vis:
                        q.append(j)
        return ans





