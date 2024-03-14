

# Define a dictionary
string_dictionary = {}

# Assign value to a dictionary
string_dictionary = {
    "name": "Touhid Mia",
    "country": "Bangladesh",
    "age": 28,
}


print(string_dictionary["name"])
print(string_dictionary["country"])
print(string_dictionary["age"])


# Print each element of dictionary by loop
for key in string_dictionary:
    print(key)
    print(string_dictionary[key])


print("\n\n\n")


address_book = {
    "id": 0,
    "name": "Touhid Mia",
    "mobile": "123456789",
    "email": "hmtmcse.com@gmail.com",
}

for key in address_book:
    print(key)
    print(address_book[key])