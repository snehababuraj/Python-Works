base_path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\"
yr_path=base_path+"years.txt"
leapyr_path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\leapyr.txt"
centuryyr_path=base_path+"centuryyr.txt"

yr_ref=open(yr_path,"r")
century_ref=open(centuryyr_path,"w")
leap_ref=open(leapyr_path,"w")

for line in yr_ref:
    years=int(line.strip("\n"))
    if years%100==0:
        century_ref.write(str(years)+"\n")
    if(years%100==0 and years%400==0) or (years%100!=0 and years%4==0):
        leap_ref.write(str(years)+"\n")


