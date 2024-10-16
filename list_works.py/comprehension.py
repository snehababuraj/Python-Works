# lst=[1,2,3,4,5,7]
# squares=[num**2 for num in lst]
# print(squares)

languages=["python","java","c++","javascript","typescript"]
# new_list=[]
# for lang in languages:
#     new_list.append(lang.upper())
# print(new_list)

new_list=[lang.upper() for lang in languages]
print(new_list)

len_filter=[lang for lang in languages if len(lang)>5]
print(len_filter)

lst=[2,4,6,3,1]
maps_nums=[num+1 if num>5 else num-1 for num in lst]
print(maps_nums)


lst=["-","+","-","-","+","-","+","+"]
map_symbols=[1 if sym=="+" else 0 for sym in lst]
print(map_symbols)