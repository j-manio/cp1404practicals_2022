"""
Randoms
"""

import random

help(random.randint)

help(random.randrange)

"""
What did you see on line 1?
    145
    
What was the smallest number you could have seen, what was the largest?
    5 would be the smallest and 199 will be the highest.

What did you see on line 2?
    7
    
What was the smallest number you could have seen, what was the largest?
    Smallest would be 3 and largest would be 9.
    
Could line 2 have produced a 4? 
    No, because it would skip 2.

What did you see on line 3?
    3.5559037438586807 - number with decimals
What was the smallest number you could have seen, what was the largest?
    2.5 would be the smallest and 5.4 would be the highest.
    
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

print(f'This is the random number: {random.randrange(1, 101)}')
