'''
1. 2A11, 2D13, 4G17, ?
Answer:- 12J23
'''

'''
2. What will be the output of the following statement?
'''

I = [1, 2, 3, 4, 5]
ans = 3 in I
print(ans)

'''
Output:- True
'''

'''
3. fenplac means filmy holiday
Placston means holiday beach 
Stonrum means beach perform 
Rumfen means perform filmy 
Which word means "holiday"?
Answer:- plac
'''

'''
4. What will be the output of the following Python code?
'''

class ZeroDenominatorError(Exception):
    try:
        a = 10
        b = 0
        if b == 0:
            raise ZeroDivisionError()
        c = a / b
    except ZeroDivisionError:
        print('Zero Division Error occurred')

z = ZeroDenominatorError()

'''
Output:- Zero Division Error occurred 
'''

'''
5. A word and number arrangement machine when given an input line of words and numbers rearranges them by following a particular rule in each step. The following is an illustration of input and rearrangement. 
Input: british 32 71 greece firangi Spanish 65 84 
Step I spanish british 32 71 greece firangi 65 84 
Step II spanish 84 british 32 71 greece firangi 65 
Step III spanish 84 greece british 32 71 firangi 65
Step IV spanish 84 greece 71 british 32 firangi 65
Step V spanish 84 greece 71 firangi british 32 65 
Step VI spanish 84 greece 71 firangi 65 british 32 
and Step VI is the last step of the rearrangement. As per the rules followed in the above steps, find out in the following question the appropriate step for the given input. Input: ‘angry happy 49 24 fussy winky 34 69’. Which of the following steps will be the last but one? 
Answer:- V
'''
















