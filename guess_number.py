# name = raw_input('What is your name? >')
# print 'Hi ' + name
# print type(name)

secret_number = 5
secret_guessed = False
while(secret_guessed == False):
    users_guess = int(raw_input('Guess my number: '))
    if(users_guess == secret_number):
        print('Yep, it is %s' % secret_number)
        secret_guessed = True
    else:
        if users_guess < secret_number:
            print('Nope,  %s is too low.') % str(users_guess)
        else:
            print('Sorry, %s is too high.') % str(users_guess)
