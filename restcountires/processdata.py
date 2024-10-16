from json import load
f=open("C:\\Users\\LENOVO\\Desktop\\python\\restcountires\\data.json","r",encoding="UTF-8")
data=load(f)
#q1print(len(data))
all_name=[n.get("name")for n in data]
#print(all_name)
all_capital=[n.get("capital")for n in data]
#q3print(all_capital)
region=[d.get("name")for d in data if d.get("region")=="Asia"]
#q4print(region)
#q5 high population
population_filter=[c.get("name") for c in data if c.get("population")==40218234]
#print(population_filter)
#q6 sub regions of country Argentina
sub_region=[c.get("subregion")for c in data if "Argentina" in c.get("name")]
#print(sub_region)


#q7 high population
def get_population(dict):
   return dict.get("population")
largest_population=max(data,key=get_population)
#print(largest_population.get("name"))

largest_population=max(data,key=lambda dict:dict.get("population"))
#print(population.get("name"))

#q8 smallest population
def get_population(dict):
    return dict.get("population")
smallest_population=min(data,key=get_population)
#print(smallest_population.get("name"))

#q9 print language of American Samoa
lang=[c.get("languages")for c in data if "American Samoa" in c.get("name")]
#print(lang)

#q9 print language of American Samoa
translation=[c.get("translations")for c in data if "American Samoa" in c.get("name")]
#print(translation)

#q10 print all independent countries
independent_countries=[c.get("name")for c in data if c.get("independent")==True]
#print(independent_countries)
#q11 no of independent countries
#print(len(independent_countries))

#q12 non independent
non_independent=[c.get("name")for c in data if c.get("independent")==False]
#print(non_independent)

#q13 print allcountires with timezone of "UTC+40:30"
timezone=[c.get("name")for c in data if "UTC-04:00" in c.get("timezones")]
#print(timezone)

#q14 print all  polar regions and total number
#polar_regions=[c.get("name")for c in data if c.get("Polar") in c.get("region")]
#print(polar_regions)

#q15 high area
#def get_area(dict):
#    return dict.get("area")
#high_area=max(data,key=get_area)
#print(high_area.get("name"))

#q16 calling code of Argentina
calling_code=[c.get("callingCodes")for c in data if "Argentina" in c.get("name")]
#print(calling_code)

#q17 borders of specific country
country_borders=[c.get("borders")for c in data if c.get("name")=="India"]
#print(country_borders)

#q18 countries with india border
border_filter=[c.get("name") for c in data if "borders" in c and "IND" in c.get("borders")]
#print(border_filter)

#q19 country with language
values={}
for c in data:
    lang_list=[]
    if "languages" in c:
        for l in c.get("languages"):
            lang_list.append(l.get("name"))
        values[c.get("name")]=lang_list
#print(values.get("Argentina"))

#20 currencies
#for c in data:
#    if "currencies" in c:
#        for cur in c.get("currencies"):
#            if cur.get("name")=="Indian rupee":
#                print(c.get("name"))

#q21 countries with multpile tymzone

#q23 Asia: region count
reg=[i.get("region")for i in data]
wc={r:reg.count(r) for r in set(reg)}
#print(wc)


#q1 tme zone ahead or behind
indian_timezone=[ c.get("timezones") for c in data if c.get("name")=="India"]
print(indian_timezone[0][0])
time_zone_india=indian_timezone[0][0]
afg_timezone=[ c.get("timezones") for c in data if c.get("name")=="Afghanistan"]
print(indian_timezone[0][0])
time_zone_agf=afg_timezone[0][0]
indian_offset=time_zone_india.lstrip("UTC").replace(":",".")
print(indian_offset)
afg_offset=time_zone_agf.lstrip("UTC").replace(":",".")

from datetime import datetime,timedelta
offset_india=timedelta(hours=float(indian_offset))
print("india offset",offset_india)
offset_usa=timedelta(hours=float(afg_offset))
print("usa offset",offset_usa)

time_country1=datetime.utcnow()+offset_india
print("first",time_country1)
time_country2=datetime.utcnow()+offset_usa
print("second",time_country2)
time_diff=time_country1-time_country2
print("time difference",time_diff.total_seconds())
if(time_diff.total_seconds()>0):
    print("time zone ahead")
else:
    print("time zone behind")
