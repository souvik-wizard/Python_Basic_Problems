#  Leetcode Problem Number 69                 
# 1
num = float(input('Enter a number: ')) 
            #  **means num is multiplying 0.5(here) times
root=num**0.5
print("The square root of {0} is: {1} ".format(num,root))



# 2        Printing 2 decimal places for float value
import math
num = float(input('Enter a number: '))  
root=math.sqrt(num)
float_val="{:.2f}".format(root)
print("The square root of {0} is: {1} ".format(num,float_val))



# 3 

import math
num = float(input('Enter a number: ')) 
root=math.sqrt(num)
print(math.floor(root))
print("The square root of {0} is: {1} ".format(num,root))
