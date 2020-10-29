import pandas as pd

dataset1 = pd.read_csv('/users/mustafaaliaykon/Downloads/sales.csv')
dataset2 = pd.read_csv('/users/mustafaaliaykon/Downloads/product.csv')
dataset3 = pd.read_csv('/users/mustafaaliaykon/Downloads/store.csv')




dataset3 = dataset3.drop(columns = "name")
dataset3["store"] = [1,2,3,4,5,6,7]
# print(dataset3)
dataset2 = dataset2.drop(columns = "name")
dataset2["product"] = [101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110 , 111 , 112 , 113 , 114 , 115]
# print(dataset2)

store_sales = pd.merge(dataset3,dataset1, on = "store")
# print(store_product)


result = pd.merge(store_sales,dataset2,on = "product")


result = result.drop(columns="id_x",axis = 1)
result = result.drop(columns= "id_y",axis = 1)
result["date"] = pd.to_datetime(result["date"])
start_date = input("format of start date : YYYY-MM-DD: ")
end_date = input("format of end date : YYYY-MM-DD: ")
mask = (result['date']>=start_date) & (result["date"]<= end_date)
result = result.loc[mask]
print(result)

########################### 1 #######################
print("---- TOP SELLER PRODUCT----")
product_list = result["product"].unique()
sum_list1  =list()
for item in product_list:
    x1 = result["quantity"][result["product"]==item]
    ratio1 = sum(x1)
    sum_list1.append(ratio1)


data1 = pd.DataFrame({"product":product_list , "quantity": sum_list1})

new_index1 = (data1["quantity"].sort_values(ascending = False)).index.values

sorted_data_2 = data1.reindex(new_index1)


print(sorted_data_2.head(3))

########################### 2 #######################
print("----TOP SELLER STORE------")
store_list = result["store"].unique()
sum_list2 = list()
for a in store_list:
    x2 = result["quantity"][result["store"]==a]
    ratio2 = sum(x2)
    sum_list2.append(ratio2)

data2 = pd.DataFrame({"store":store_list , "quantity": sum_list2})

new_index2 = (data2["quantity"].sort_values(ascending = False)).index.values
sorted_data_3 = data2.reindex(new_index2)


print(sorted_data_3.head(3))

########################### 3 ########################
print("----- TOP SELLER BRAND-----")
brand_list = result["brand"].unique()
sum_list3 = list()
for b in brand_list:
    x3 = result["quantity"][result["brand"]==b]
    ratio3 = sum(x3)
    sum_list3.append(ratio3)

data3 = pd.DataFrame({"brand":brand_list , "quantity": sum_list3})

new_index3 = (data3["quantity"].sort_values(ascending = False)).index.values
sorted_data_4 = data3.reindex(new_index3)


print(sorted_data_4.head(3))

############################ 4 ####################
print("---- TOP SELLER CITY ------")
city_list = result["city"].unique()

sum_list = list()

for i in city_list:
    x = result["quantity"][result["city"] == i]
    ratio = sum(x)
    sum_list.append(ratio)

data = pd.DataFrame({"city" : city_list , "quantity" : sum_list})

new_index = (data["quantity"].sort_values(ascending = False)).index.values

sorted_data1 = data.reindex(new_index)
print(sorted_data1)
