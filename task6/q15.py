arr=[25,56,34,12,10]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("largest element in the array",max)