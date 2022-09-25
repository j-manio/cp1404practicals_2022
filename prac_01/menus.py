'''
Menu
'''

user_name = str(input('Enter name: '))
MENU = '''(H)ello
(G)oodbye
(Q)uit
'''
print(MENU, end='')
user_choice = str(input('>>>' )).upper()
while user_choice != "Q":
    print(MENU, end='')
    if user_choice == "H":
        print(f'Hello {user_name.capitalize()}')
    elif user_choice == "G":
        print(f'Goodbye {user_name.capitalize()}')
    else:
        print("Invalid choice")

    user_choice = str(input('>>>')).upper()
print('Finished')
