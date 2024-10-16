product={"code":123,"name":"plum","category":"tonner","price":345,"offer":390}
# print(product["name"])
# product["color"]="green"
# print(product)
# product["price"]=340
# print(product)


#chk offer key present in product


# print("offer" in product)

if "offer" in product:
#     product["offer"]=250
# else:
#     product["offer"]=300
# print(product)
print(product.get("name"))
product.update({"price":340})
print(product)

#q 
lst=[100,200,300,150]
#total_max pair(200,300) add two number print max pair