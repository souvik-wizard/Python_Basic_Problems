
array=[10,22,5,2,0,100,50]


n=len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if array[i]>array[j]:
             temp=array[i]
             array[i]=array[j]
             array[j]=temp
print(array)

