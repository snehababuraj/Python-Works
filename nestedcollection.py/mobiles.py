products=[
    {"code":100,"name":"redminote13","brand":"redmi","price":30000,"network":"5g"},
    {"code":101,"name":"iphone15","brand":"apple","price":130000,"network":"5g"},
    {"code":102,"name":"samsunga18","brand":"samsung","price":20000,"network":"4g"},
    {"code":103,"name":"redminote12","brand":"redmi","price":30000,"network":"4g"},
    {"code":104,"name":"s23ultra","brand":"samsung","price":150000,"network":"5g"},
    {"code":105,"name":"motoedge","brand":"motorola","price":24000,"network":"5g"},
    {"code":106,"name":"oneplus9r","brand":"oneplus","price":30000,"network":"5g"},
 
    
]
#q1 total num of products
print(len(products))

#q2 apple products price
#for dictionary in products:
 #   if dictionary.get("brand")=="apple":
 #       print(dictionary.get("price"))
                 #or
apple_price=[p.get("price") for p in products if p.get("brand")=="apple"]
print(apple_price)


#q3 mobile available under 20k-25k    

price_product=[p.get("name") for p in products if p.get("price") in range(20000,25001)]
print(price_product)

#q4 costly brand

def get_price(dictionary):
   return dictionary.get("price")
costly_brand=max(products,key=get_price)
print(costly_brand.get("brand"))

#cheap_brand=min(products,key=get_price)
#print(cheap_brand)

#q5 print all 5g network
#for p in products:
 #   if p.get("network")=="5g":
  #      print(p.get("brand"))
network=[ p.get("name") for p in products if p.get("network")=="5g"]
print(network)

#q6 brand:3,redmi:3
all_brand=[p.get("brand")for p in products]
wc={brand:all_brand.count(brand) for brand in set(all_brand)}
print(wc)


