arr=[1,5,4,2,3,6] 
#[1,2,3,4,5]
# arr.sort()
# left=0
# while(left<len(arr)-1):
#     right=left+1
#     right_element=arr[right]
#     left_element=arr[left]
#     if right_element-left_element!=1:
#         print(left_element+1,"is missing")
#         break
#     else:
#         left=left+1
# else:
#     print(right_element+1,"is missing")


arr.sort()
left=0
while(left<len(arr)-1):
    right=left+1
    right_element=arr[right]
    left_element=arr[left]
    if right_element-left_element!=1:
        print(left_element+1,"is missing")
        break
    else:
        left=left+1
else:
    print(right_element+1,"is missing")