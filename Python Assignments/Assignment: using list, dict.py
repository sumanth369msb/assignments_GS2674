# Write a Python class Restaurant with attributes like menu_items, book_table, and 
# customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.

class Restaurent:
    def __init__(self,menu_items, book_table, customer_orders):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_orders=customer_orders
    
    def add_item_to_menu(self,new_items):
        self.menu_items.append(new_items)
    
    def book_tables(self,table_no,cust_name):
        self.book_table[table_no]=cust_name
    
    def customer_order(self,item):
        self.customer_orders=[menu_items[i] for i in range(len(menu_items)) if item in menu_items[i]]
    
menu_items=["dosa","idly","Bonda"]
book_table={1:"Pranay"}
customer_orders=[]

restaurent=Restaurent(menu_items,book_table,customer_orders)

restaurent.add_item_to_menu("puri")
restaurent.book_tables(2,"UDN")
restaurent.customer_order("dosa")
restaurent.menu_items
restaurent.book_table
restaurent.customer_orders
