def create_user():
    print('Enter a username')
    username = input()
    print('Enter your full name')
    full_name = input()
    print('Enter your password')
    password = input()
    print('Re-enter your password')
    confirm_password = input()

    if password != confirm_password:
        print('The passwords don\'t match')
        return
    
    if len(password) < 8:
        print('Password must be at least 8 characters in length')
        return
    
    # Encrypt the password (just reverse it, should be secure)
    array = password[::-1]

    print(f'Saving Details for User ({username}, {full_name}, {array})')

create_user()