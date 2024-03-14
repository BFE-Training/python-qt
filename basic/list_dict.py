


address_book = [
    {
    "id": 0,
    "name": "Touhid",
    "mobile": "123456789",
    "email": "hmtmcse.com@gmail.com",
},
    {
    "id": 0,
    "name": "Mia",
    "mobile": "98765321",
    "email": "test@gmail.com",
}
]



for address in address_book:
    print("\n")
    for key in address:
        print(address[key])