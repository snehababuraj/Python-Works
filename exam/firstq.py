arr1=[1,2,3,4,5]
arr2=[3,4,5,6]
#def common_sum(arr1,arr2):
#    sum=0
 #   for num in arr2:
  #      if  num in arr1:
   #         sum=sum+num
    #return sum
#print(common_sum(arr1,arr2))

def common_sum(arr1,arr2):
    wc={num:arr1.count(num)for num in arr2}
    total=sum([k for k,v in wc.items() if v>0])
    return total
print(common_sum(arr1,arr22))

