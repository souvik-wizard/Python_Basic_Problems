
# printing in below order
# *
# **
# ***
# ****
# *****

for i in range(0,5):
    for j in range(i+1):
        print('*',end=" ")
        
    print()


# -----------------------
# 1
# 2 3
# 4 5 6
# 7 8 9 10


var=1
for i in range(0,5):
    for j in range(i+1):
        print(var,end=" ")
        var+=1
    print()