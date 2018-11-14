# name = raw_input('What is your name? >')
# print 'Hi ' + name
# print type(name)


secret_guessed = False
while(secret_guessed == False):
    secret_number = raw_input('Guess my number: ')
    if(secret_number == "5"):
        print('Yep, it is 5')
        secret_guessed = True
    else:
        print(secret_number)
        print('Nope, not ' + secret_number)
