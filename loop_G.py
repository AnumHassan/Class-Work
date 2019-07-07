import random
arr=[]
(len(arr))
n=0
z=0
#len--length
#empty array,searching,sorting, sorting,traversing, operation,deletion
for i in range(1,9):
 arr.append(random.randint(10,100))
 num=arr
 n=n+1
 print("The " + str(n)+ " Random No is:" + str(num[z]))
 z=z+1
#for num in arr:
  #print("The" + str(n)+ "Random No is:" + str(num))
Sum_1 = sum(arr)
leng= len(arr)
Avg=float(Sum_1/leng)
Min_val=0
Min_idx=0
for i in range(len(arr)):
 if i==0:
  if arr[i] < arr[i+1]:
      Min_val=num[i]
      Min_idx= i
  else:
      Min_val=arr[i+1]
      Max_val=arr
else:
    if Min_val>arr[i]:
        Min_val=arr[i]
        Min_idx=i

#Min_1=min(arr)
#Max_1=max(arr)
print("The Sum Of Random No:" + str(Sum_1))
print("The length Of Random No:" + str(leng))
print("The Average Of Random No:" + str(Avg))
print("The Minimum Random No:" + str(Min_val))
print("The Minimum index Random No:" + str(Min_idx))
#print("The Maximum Random No:" + str(Max_))