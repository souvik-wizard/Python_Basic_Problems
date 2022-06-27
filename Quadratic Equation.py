# Quadratic Equation (ax^2 + bx + c = 0)
import math

a=int(input("Enter the value of 'a':"))
b=int(input("Enter the value of 'b':"))
c=int(input("Enter the value of 'c':"))

    
calc_pos= (-b+(math.sqrt(b**2-4*a*c)))/2*a

calc_neg= (-b-(math.sqrt(b**2-4*a*c)))/2*a


print("The solutions are {0} and {1} : ".format(calc_pos,calc_neg) ) 

