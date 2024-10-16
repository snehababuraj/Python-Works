#find missing least positive int in list always staring from 1
arr=[1,5,4,3] 
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
    print(right_element+1,"is  missing")

# lst=[1,2,3,4,5,7,8,8,10]
# srch_element=6
# for num in lst:
#     if num==srch_element:
#         print("element found")
#         break
# else:
#     print("elemnet not found")

#lst=[1,3,4,5,4,5,5,5,5,6,7]
#most frequent number

#two pair sum
#arr=[2,3,5,4]
#arr.sort()
#sum=5
#l=0
#r=len(arr)-1
#is_present=False
#while(l<r):
 #   left_element=arr[l]
  #  right_element=arr[r]
   ##if sum==current_sum:
        #print("paris",left_element,right_element)
        #is_present=True
        #break
    #elif sum>current_sum:
    #    l=l+1
    #elif sum<current_sum:
     #   r=r-1
#if is_present==False:
 #   print("paris does not exsist")    
    


#binary searching
arr=[3,2,4,6,11,8,76]
element=int(input("enter a number"))
arr.sort()
l=0
r=len(arr)-1
while(l<=r):
    mid=(l+r)//2
    if element==arr[mid]:
        print("element is found")
        break
    elif element>arr[mid]:
        l=mid+1
    elif element<arr[mid]:
        r=mid-1
else:
    print("element not found")
   
