attemps = 0

while attemps < 3:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'affan' and password == '123':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials.')
        attemps += 1
        continue