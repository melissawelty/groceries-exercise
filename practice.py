books = [
    {"id":1, "title":"Book A", "color":"blue", "year":1901},
    {"id":2, "title":"Book B", "color":"red", "year":1957},
    {"id":3, "title":"Book C", "color":"blue", "year":1988},
    {"id":4, "title":"Book D", "color":"green", "year":1923},
    {"id":5, "title":"Book E", "color":"yellow", "year":2017},
]


# print title of book whose id is 4 
print([b["title"] for b in books if b["id"] == 4][0])

#print number of books whose color is blue 
blue_books = len([b for b in books if b["color"] == "blue"])
print(blue_books)

# number books published after year 1950
new_books = len([b for b in books if float(b["year"]) > float("1950")])
print(new_books)



delivery = {
    "sender": "Charlie",
    "recipient": "Anika",
    "price": 16.99,
    "status": "In Transit",
    "stops": ["New York", "Denver", "San Francisco"]
}

# print "A delivery from Charlie to Anika"
s_name = delivery['sender']
t_name = delivery['recipient']
print("A delivery from " + str(s_name) + "to " + str(t_name))

# print number stops delivery makes

print(len(delivery['stops']))


# # print first stop
print(delivery['stops'][0])

# # print last stop
print(delivery['stops'][-1])

# # loop through delivery stop and print each stop one at a time
for x in delivery['stops']:
    print(x)