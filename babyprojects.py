#1. Create a dictionary of three books with author and price in a list. Print it
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





#2. Display the price of 'Keyboard' from the product dictionary.

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



#3.Display the course code of 'Python' from the course dictionary.

course = {
    "Python": {"instructor": "DIddy", "duration": "8 weeks"},
    "JAVA": {"instructor": "TRump", "duration": "9 months"},
    "C++": {"instructor": "A red indian", "duration": "5 seconds"}

}
print(course["Python"])



#4. Update the quantity of 'Pens' to 50 and print the updated record.
dict = {
    "Pens": {"quantity": 20, "price": "$2"},
    "pencils": {"quantity": 30, "price": "$1"}
}
print(f"Before update: Pens = {dict['Pens']}")
dict["Pens"]["quantity"] = 50 
#or dict.update({"Pens": {"quantity": 50, "price": "$2"}})
print(f"After update: Pens: {dict['Pens']}")
for i in range(1, 2):
    print(f"-" * 20)




#5. Add a new employee (ID and department in a list) using direct assignment
employees = {
    "Fatima" : {"ID": "E001", "department": "HR"},
    "Rohan" : {"ID": "E002", "department": "Finance"},
    "Aisha" : {"ID": "E003", "department": "IT"}
}

print(f"Before update = {employees}")
employees["ali"] = {"ID": "E004", "department": "Marketing"}
print(f"After update = {employees}")
for i in range(1, 2):
    print(f"-" * 20)



