#GUI for intro tab
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from datetime import datetime
def show_welcome_and_website():
    # Create the main window
    root = tk.Tk()
    root.title("Click Here")


    # Set window size
    root.geometry("700x400")# Width x Height
    root.resizable(False,False)
    # Load and display background image
    background_image = Image.open("afk.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=-120, y=0, relwidth=1, relheight=1)
   

    # Function to handle button click
    def on_button_click():
        user_name = simpledialog.askstring("Input", "Enter your name:")
        welcome_label.config(text=f"Welcome,{user_name}!\n To GOING AFK")
    
    # Create a button
    button = tk.Button(root, text="Click Here", command=on_button_click,bg="light blue",fg="midnight blue")
    button.pack(pady=40)

    # Create labels to display the welcome message and website name
    welcome_label = tk.Label(root, text="", font=("Times New Roman", 16), fg="black",bg="steelblue1")
    welcome_label.pack(pady=10)
    welcome_label.place(x=490,y=0,width=220,height=400)


    # Run the main loop
    root.mainloop()
#loading files
file1 = open('Games.txt', 'r')
file2 = open('Consoles.txt', 'r')
file3 = open('Accessories.txt', 'r')
file4 = open('Controllers.txt','r')
file5 = open('Virtual Gift Cards.txt','r')
f = open('IDndpwd.txt', "r+")
#placing them in dictionary
my_dict = {}
Games = {'category_name': 'Games', 'items': {}}
Consoles = {'category_name': 'Consoles', 'items': {}}
Accessories = {'category_name': 'Accessories', 'items': {}}
Controllers = {'category_name': 'Controllers', 'items': {}}
Virtual_Gift_Cards = {'category_name': 'Virtual Gift Cards', 'items': {}}
for line in f:
    key, value = line.strip().split(',')
    my_dict[key] = value

for line in file1:
    key, value = line.strip().split(',', 1)
    Games['items'][key] = {'price': float(value)}

for line in file2:
    key, value = line.strip().split(',', 1)
    Consoles['items'][key] = {'price': float(value)}

for line in file3:
    key, value = line.strip().split(',', 1)
    Accessories['items'][key] = {'price': float(value)}
for line in file4:
    key, value = line.strip().split(',', 1)
    Controllers['items'][key] = {'price': float(value)}
for line in file5:
    key, value = line.strip().split(',', 1)
    Virtual_Gift_Cards['items'][key] = {'price': float(value)}
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
cart_items = []
cart_total = 0
#function for log_in 
def Login():
    while True:
        print('Press "s" to sign up if you don\'t have an account')
        user_id_input = input('Enter your user ID: ')

        if user_id_input.lower() != 's':
            if user_id_input in my_dict.keys():
                password = input('Enter your password: ')
                if my_dict[user_id_input] == password:
                    print('Login successful!')
                    return user_id_input
                else:
                    print('Invalid password. Please try again.')
            else:
                print('Invalid user ID. Please try again.')
        else:
            print('Sign-up process...')
            while True:
                new_id = input('Enter your new user ID: ')
                if new_id not in my_dict.keys():
                    break
                else:
                    print('This user ID is already in use. Please use a different one.')

            new_pwd = input('Enter your new password: ')
            f.write(new_id + ',' + new_pwd + '\n')
            f.close()
            print("Thank you for signing up! Please rerun the program to log in with your new credentials.")

            return new_id
#function for cart program      
def add_to_cart(choice,cart_items, cart_total):
    while True:
        print("press 'r' to remove, or press 'b' to go back:")
        for item, details in choice['items'].items():
             print(f"{item}: ${details['price']}")

        cart_item = input('Your choice: ')

        if cart_item == 'b':
             break
        elif cart_item == 'r':
             remove_item = input('Enter the name of the item to remove: ')
             remove_item_from_cart(cart_items, remove_item)
        elif cart_item in choice['items']:
             quantity = input('Enter the quantity: ')
             if quantity.isdigit() and quantity!='0':
                total_price = int(quantity) * float(choice['items'][cart_item]['price'])
                cart_total += total_price
                cart_items.append({'item': cart_item, 'quantity': quantity, 'total_price': total_price})
             else:
                print('quantity is required')
        else:
             print('Invalid item')

    return cart_total

#function to remove items from cart
def remove_item_from_cart(cart_items, remove_item):
    for item in cart_items:
        if item['item'] == remove_item:
            cart_items.remove(item)
            print(f"{remove_item} removed from the cart.")
            return
    print(f"{remove_item} not found in the cart.")
#function to save history
def save_history_to_file(user_id, cart_items, cart_total):
    filename = f'{user_id}_history.txt'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, 'a') as file:
        file.write(f'Transaction Time: {timestamp}\n')
        file.write(f'Total: ${cart_total:.2f}\n')
        for item in cart_items:
            file.write(f"{item['quantity']} {item['item']} at ${item['total_price']:.2f} each\n")
        file.write('\n')
        file.close()
#function to view history
def view_history(user_id):
    filename = f'{user_id}_history.txt'
    try:
        with open(filename, 'r') as file:
            print(f"\nTransaction History for {user_id}:")
            print(file.read())
    except FileNotFoundError:
        print('No transaction history yet.')
#function to view users feedback
def view_feedback(user_id):
    file6=f'{user_id}_feedback.txt'
    try:
        with open(file6, 'r') as file6:
            print(f"\nTransaction History for {user_id}:")
            print(file6.read())
    except FileNotFoundError:
        print('No transaction history yet.')
#function for admin log-in
def admin_login():
    admin_id = input('Enter admin ID: ')
    admin_pwd = input('Enter admin password: ')

    # Replace 'admin' and 'adminpass' with actual admin credentials
    if admin_id == 'mominhaf' and admin_pwd == '2005':
        print('Admin login successful!')
        return True
    else:
        print('Invalid admin credentials. Access denied.')
        return False
#function to show admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View User Information")
        print("2. View Transaction History")
        print("3. Review Feedbacks")
        print("4. Logout")

        admin_choice = input('Your choice: ')
        if admin_choice =='1':
            print('User Credentials:')
            if my_dict!={}:
                for key, value in my_dict.items():
                   print(f"user_id:{key}, password:{value}")
            else:
                print("No Users Found")
        elif admin_choice =='2':
            user_id=input('Enter the Username whose history you want to see: ')
            view_history(user_id)
        elif admin_choice =='3':
            user_id=input('Enter the Username whose feedback you want to see: ')
            view_feedback(user_id)
   
        elif admin_choice == '4':
            print('Admin logout successful!')
            break
        else:
            print('Invalid choice. Please try again.')
#function to show user menu      
def login_menu(user_id):
    cart_total=0
    while True:
       print("Select a category:")
       print("1. Games")
       print("2. Consoles")
       print("3. Accessories")
       print("4. Controllers")
       print("5. Virtual Gift Cards")
       print("6. Checkout")
       print("7. View History")
       print("8. Write Feedback")
       print("9. Log out")
       choice = input('Your choice: ')

       if choice == '1':
          cart_total = add_to_cart(Games, cart_items, cart_total)
       elif choice == '2':
          cart_total = add_to_cart(Consoles, cart_items, cart_total)
       elif choice == '3':
          cart_total = add_to_cart(Accessories, cart_items, cart_total)
       elif choice == '4':
           cart_total = add_to_cart(Controllers, cart_items, cart_total)
       elif choice == '5':
           cart_total = add_to_cart(Virtual_Gift_Cards, cart_items, cart_total)
       elif choice == '6':
          save_history_to_file(user_id, cart_items, cart_total)
          break
       elif choice == '7':
          view_history(user_id)
       elif choice == '8':
           print("We want to hear from you! Your feedback helps us improve.")  
           feedback=input("Share your Experience: ")
           print("Thank you for being a valued part of our GoingAFK Community")
           file6 = f'{user_id}_feedback.txt'
           with open(file6, 'w') as file:
              file.write(feedback)
              file.close()
       elif choice=='9':
          print('User log-out successful')
          break
       else:
          print('Invalid choice. Please try again.')
    print(f'Your cart is: {cart_items}\nYour total bill is: ${cart_total:.2f}')

      
