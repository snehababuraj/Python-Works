# vehicle_numbers=["KL-08-4970","KL-01-9078","KL-23-9999","TN-01-7864","TN-23-4563","KT-04-5634","KT-39-8744","KL-04-7623"]
# path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\vehicle_num.txt"
# fw=open(path,"w")
# for num in vehicle_numbers:
#     if num.startswith("KL"):
#         fw.write(num+"\n")


#phone number=["phone numbers"] give valid and invalid numbers write valid numbers into phone.txt


phn_num=["96561189175","8181101806","9447562780","9873627000","87xx234576","85462792901"]
path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\phn_num.txt"
fw=open(path,"w")
for num in phn_num:
    if len(num)==10 and num.isdigit():
        fw.write(num+"\n")
