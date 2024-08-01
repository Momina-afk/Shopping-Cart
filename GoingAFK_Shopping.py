#importing functions required to run this program
from my_functions import show_welcome_and_website
from my_functions import *

if __name__ == "__main__":
    show_welcome_and_website()
#main code
print('Welcome to GoingAFK')

while True:
    print('1. Log-in\n2. Log-in as admin\n3. Quit')
    choice = input("Enter your Choice: ")

    if choice == '1':
           user_id=Login()
           login_menu(user_id)
    elif choice == '2':
        if admin_login():
           admin_menu()
    elif choice=='3':
        print('Thanku for shopping with GoingAFK.Have a great day!')
        break
    else:
        print('Invalid choice. Please try again.')

