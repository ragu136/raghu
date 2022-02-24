cart_items = {
               "watch" : 1,
               "phone": 1,
               "earphones": 1,
               "shoes": 1,
               "shirt" :1,
               "pant": 1,
               "perfume":1,
               "python_book":1,
               "apple":1,
               "custard_apple":1,
               "magic_moments":1,
               "mansion_house":1,
               "volleyball":1,
               "chairs":1,
             }




def print_output(operation_message, cart_items_length):

    print(operation_message)
    print_list_items()
    print(cart_items_length)

    
def print_list_items():
    print("items in the cart: ", len(cart_items))
    for key,val in cart_items.items():
        print("{}: {}".format(key,val))
  

def delete_item_from_cart():
    user_response = input("Enter item to delete from cart: ")
    if user_response in cart_items.keys():
             cart_items.pop(user_response)
             cart_items[user_response] = cart_items[user_response]- 1        
    else:
        print(" please enter a valid item ")
    
    print_output("\nAfter deleting item in the cart\n", len(cart_items))
    

def add_item_to_cart():
    user_response = input("Enter item to add to cart: ")
    if user_response not in cart_items.keys():
        cart_items[user_response]=1
    else:
        cart_items[user_response] = cart_items[user_response]+ 1    

    print_output("\nAfter adding item in the cart\n", len(cart_items))


print_list_items()
add_item_to_cart()
delete_item_from_cart() 

#add_item_to_cart()
#add_item_to_cart()
#add_item_to_cart()
#delete_item_from_cart()
#delete_item_from_cart()
#delete_item_from_cart()
#delete_item_from_cart()


