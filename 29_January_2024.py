'''
Task:- 
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

 void push(int x) Pushes element x to the back of the queue.
 int pop() Removes the element from the front of the queue and returns it.
 int peek() Returns the element at the front of the queue.
 boolean empty() Returns true if the queue is empty, false otherwise.
'''

'''
Example 1:- 
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 1, 1, false]
Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''

'''
Constraints:- 
 1 <= x <= 9
 At most 100 calls will be made to push, pop, peek, and empty.
 All the calls to pop and peek are valid.
'''

class MyQueue:
    def __init__(self):
        
        '''
        Initialize your data structure here.
        '''
        
        self._s1, self._s2 = [], []

    def push(self, x: int) -> None:
        
        '''
        Push element x to the back of queue.
        '''
        
        self._s1.append(x)

    def pop(self) -> int:
        
        '''
        Removes the element from in front of queue and returns that element.
        '''
        
        if len(self._s2) == 0:
            while self._s1:
                self._s2.append(self._s1.pop())
        return self._s2.pop()

    def peek(self) -> int:
        
        '''
        Get the front element.
        '''
        
        if len(self._s2) == 0:
            while self._s1:
                self._s2.append(self._s1.pop())
        return self._s2[-1]

    def empty(self) -> bool:
        
        '''
        Returns whether the queue is empty.
        '''
        
        return len(self._s1) + len(self._s2) == 0
        
'''
Your MyQueue object will be instantiated and called as such:- 
 obj = MyQueue()
 obj.push(x)
 param_2 = obj.pop()
 param_3 = obj.peek()
 param_4 = obj.empty()
'''
