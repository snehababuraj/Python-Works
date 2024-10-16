arr=[25,70,35,678,90]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("largest element in the array ", max)