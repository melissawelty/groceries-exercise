


# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

# for i in my_numbers:
#     print(i)
print("--------------")
# MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
mapped_list = [i *100 for i in my_numbers]
print("MAPPED LIST:", mapped_list)

print("--------------")
# FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
filtered_list = [i for i in my_numbers if i > 3]
print("FILTERED LIST W/ MATCHES:", filtered_list)


print("--------------")
# FILTERED LIST W/O MATCHES: []
no_matches = [i for i in my_numbers if i > 8]
print("FILTERED LIST W/O MATCHES:", no_matches)

print("--------------")
# MAPPED AND FILTERED LIST: [400, 500, 600, 700]
mapped_and_filtered = [i * 100 for i in my_numbers if i > 3]
print("MAPPED AND FILTERED LIST:", mapped_and_filtered)