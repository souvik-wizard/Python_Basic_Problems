num=int(input("Enter the number:"))
if num>1 :
    for i in range(2,num):
       if num%i==0:
                print("This is not a prime number, because ",i,"times",num//i,"is",num)
                break
    else:
        print(num," is a prime number.")
else:
    print("If input number is less than or equal to 1, it is not prime!")

# -----------------------------


for i in range(1,20):
    for j in range(2,i):
        if i%j==0:
            break
    print(i)


# -----------------------------
lower = 0
upper = 20

# print("Prime numbers between", lower, "and", upper, "are:")


for i in range(lower, upper+1):
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

    