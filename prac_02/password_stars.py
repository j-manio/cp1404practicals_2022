'''
Password Checker
'''

PASSWORD_LENGTH = 10


def main():
    get_password()
    print_password()


def get_password():
    """ Will check for password length"""
    user_password = input('Password: ')
    while len(user_password) != PASSWORD_LENGTH:
        print('Does not meet the requirement')
        user_password = input('Password: ')


def print_password():
    """ Will print stars """
    print('*' * 10)


main()
