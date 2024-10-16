from json import load
f=open("C:\\Users\\LENOVO\\Desktop\\python\\products\\data.json","r",encoding="UTF-8")
data=load(f)
#print(len(data))
product_name=[p.get("title")for p in data]
#print(product_name)
all_categories=[p.get("category")for p in data]
#print(set(all_categories))
price=[p.get("title") for p in data if p.get("price")<=50]
#print(price)
jewelery=[p.get("title")for p in data if p.get("category")=="jewelery"]
#print(jewelery)
def get_price(dictionary):
    return dictionary.get("price")
costly_product=max(data,key=get_price)
#print(costly_product.get("title"),costly_product.get("price"))

def get_price(dictionary):
    return dictionary.get("price")
cheap_product=min(data,key=get_price)
#print(cheap_product.get("title"),cheap_product.get("price"))

rate_count=[(p.get("title"),p.get("rating").get("count"))for p in data]
#print(rate_count)

def get_rate(dictionary):
    return dictionary.get("rating").get("count")
high_rate=max(data,key=get_rate)
#print(high_rate.get("title"),high_rate.get("rating").get("count"))

