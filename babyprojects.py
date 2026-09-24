books = {
    "Cold": {"author": "Amily", "price": "$48"},
    "HOSTEL": {"author": "Adison Nelson", "price": "$24"},
    "MIkai": {"author": "Juiney", "price": "$32"}
}

for title, info in books.items():
    print(f"Title: {title}")   #uheh
    print(f"Author: {info['author']}")
    print(f"Price: {info['price']}")
    print("-" * 20)         #line seperaahter

#done mammraaa


products = {
    "Laptop" : ("Dell", "$800"),
    "Smartphone" : ("bhaiya", "$600"),
    "Headphones" : ("wawste", "$150"),
    "keyboard" : ("maiya", "$100")
}
for poducts, (brand, price) in products.items():
    print(f"Product: {poducts}")
    print(f"Brand: {brand}")
    print(f"Price: {price}")
    print("-" * 20)         #line seperaahter


#m the moggerr
#raarrr


course = {
    "Python": {"instructor": "DIddy", "duration": "8 weeks"},
    "JAVA": {"instructor": "TRump", "duration": "9 months"},
    "C++": {"instructor": "A red indian", "duration": "5 seconds"}
    
}
