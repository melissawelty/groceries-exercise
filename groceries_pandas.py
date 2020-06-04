# groceries.py

import operator


import pandas


csv_filepath = "products.csv"
df = pandas.read_csv(csv_filepath)
print(type(df))

# # APPROACH 1: 
# products = []

# for row in _____: # how to loop through each row in df
#     products.append({}) # how to convert each row to a dictionary


# APPROACH B:

products = df.to_dict("records")

# HOW TO CONVER PANDAS DATAFRAME TO LIST OF DICTIONARIES 



def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


print("--------------")
print("NUMBER OF PRODUCTS:", len(products))
print("--------------")

sorted_products = sorted(products, key=operator.itemgetter("name"))


for x in sorted_products:
    price_usd = to_usd(x["price"])
    print(f"+ {x['name']} ({price_usd})")










#
# Departments (part 2)
#
# --------------
# THERE ARE 10 DEPARTMENTS:
# --------------
#  + Babies (1 product)
#  + Beverages (5 products)
#  + Dairy Eggs (1 product)
#  + Dry Goods Pasta (1 product)
#  + Frozen (4 products)
#  + Household (1 product)
#  + Meat Seafood (1 product)
#  + Pantry (2 products)
#  + Personal Care (2 products)
#  + Snacks (2 products)

departments = []

for product in products:
    #print(product["department"])
    departments.append(product["department"])
    #if product["department"] not in departments:
    #   departments.append(product["department"])


    # conditional logic to only append an item into this empty list departments if
    #    it doesn't already exist in there 
    # otherwhise not worry about conditional logic when we append all departments and then remove duplicates 
        #seen below 

# other option to remove duplicates by set data types 
unique_departments = list(set(departments))

department_count = len(unique_departments)

print("--------------")
print("THERE ARE " + str(department_count) + " DEPARTMENTS:")
print("--------------") 

unique_departments.sort()

for d in unique_departments:
    matching_products = [product for product in products if product["department"] == d] #list comprehension approach 
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"
    print("+ " + d.title() + " (" + str(matching_products_count) + " " + label + ")")














