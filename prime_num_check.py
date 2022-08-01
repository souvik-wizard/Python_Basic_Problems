# num=int(input("Enter the number:"))
# if num>1 :
#     for i in range(2,num):
#        if num%i==0:
#                 print("This is not a prime number, because ",i,"times",num//i,"is",num)
#                 break
#     else:
#         print(num," is a prime number.")
# else:
#     print("If input number is less than or equal to 1, it is not prime!")

# # -----------------------------

# c=0
# for i in range(1,20):
#     for j in range(2,i):
#         if i%j==0:
#             c+=1
#             break
            
# print(c)


# -----------------------------
# nums=499979
# # print("Prime numbers between", lower, "and", upper, "are:")

# c=0
# for i in range(nums):
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
                
#                 break
#         else:
#             c+=1
# print(c)

    

    # Python program to print all
# prime number in an interval

def prime(n):
	prime_list = []
	for i in range(n):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

# Driver program
n=4999799
lst = prime(n)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", len(lst))
