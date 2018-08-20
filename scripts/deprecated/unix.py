#! python 3
#  unix.py - authentication app

import os

username = input('What\'s your username? ')
password = input('What\'s your password? ')


david = {
    'power' : 'superuser',
    'loggedin' : 0



}



try:

    def interp(inpvars):
        i = 0
        funcToCall = ''
        print(inpvars.count(' '))
        inpa,inpb = inpvars.split(' ')
        cmdList[inpa](inpb)
        

    def helpF():
        print(' '.join(cmdList))

    def power(user):
        print(user['power'])

    def ls():
        print('placeholder\n')

    def cd():
        print('placeholder\n')

    def logout(): 
        user = currentUser
#        user['loggedin'] = 0


    cmdList = {
        'power' : power,
        'help' : helpF,
        'cd' : cd,
        'ls' : ls,
        'logout' : logout}


    if username == 'david':
        if password == 'yo':
            currentUser = 'david'
            david['loggedin'] = 1
            print('Hello, administrator.\n')
            print('Type \'help\' for help.\n')
            while david['loggedin'] == 1:
                cmd1 = input()

    elif username == 'camical':
        if password == 'idon\'tcare03':
            cmd1 = input('Type \'help\' for help.\n')
            interp(cmd1)
        else:
            print('Fuck off, loser.\n')
    else:
        print('User doesn\'t exist.\n')

except KeyboardInterrupt:
    clear = lambda: os.system('clear')
    clear()
    print('Fuck off cunt.')
