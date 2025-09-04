def borrow_info():
    global borrow_counter
    borrow_counter += 1
    date_borrowed = input("Enter Date Borrowed (DD/MM/YYYY): ")
    member_id = input("Enter ID: ")
    member_name = input("Enter Name: ")
    borrow_id = 2000 + borrow_counter
    print("\nBorrow Details:")
    print(f"date Borrowed: {date_borrowed}")
    print(f"ID: {member_id}")
    print(f"Name: {member_name}")
    print(f"Borrow ID: {borrow_id}")
    return date_borrowed, member_id, member_name, borrow_id
    from borrow_1 import borrow_info
def Borrowed_books_total():
    date_borrowed, member_id, member_name, borrow_id = borrow_info()


    Number = int(input("how may books are you taking?:"))
    total_cost = 0
    while Number>0 :
        Name = ("what's name of the book?:")
        print(f"name of the boook:{Name}")
        daily_cost = int(input("give the cost:"))
        print(f"daily cost: {daily_cost}")
        total_cost = total_cost + daily_cost
        Number = Number-1 
        
    print(f"final price of books:{total_cost}")
            
    return total_cost,date_borrowed, member_id, member_name, borrow_id
    from borrow_2 import Borrowed_books_total
def rental_category():
    total_cost,date_borrowed, member_id, member_name, borrow_id = Borrowed_books_total()
    if total_cost < 5:
        category = "Light Reader"
    elif 5 <= total_cost <= 10:
        category = "Regular Reader"
    else:
        category = "Bookworm"
    category_code = member_id[:2] + str(borrow_id)[-2:]
    print(f"\nTotal daily cost: NZD{total_cost}")
    print(f"Category: {category}")
    print(f"Category Code: {category_code}")
    return total_cost, category, category_code, date_borrowed, member_id, member_name, borrow_id
    from borrow_3 import * 

def display_rentals():
    total_cost, category, category_code, date_borrowed, member_id, member_name, borrow_id = rental_category()
    
    print("\nRental Summary:")
    print(f"Date Borrowed: {date_borrowed}")
    print(f"Borrow ID: {borrow_id}")
    print(f"Member ID: {member_id}")
    print(f"Member Name: {member_name}")
    print(f"Total Daily Cost: ${total_cost}")
    print(f"Category: {category}")
    print(f"Category Code: {category_code}")

# To run the function
    if __name__ == "_main_":
        display_rentals()


































    f