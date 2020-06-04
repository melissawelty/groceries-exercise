# price 

import os
import pandas


# csv_filepath = "data/products.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

# .. goes up one directory to root repository, then down into data diretory, then products.csv 
 #references current file, askig what directory is this file in?




df = pandas.read_csv(csv_filepath)
print(type(df))
print(df.head()) # < prints first few rows

products = df.to_dict("records")



# use OS module when constructing a file path
