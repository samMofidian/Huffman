import sys


def start():
    """
    start program
    """
    # check user decision
    print('do you want to continue?(y/n): ', end='')
    user_respond = input()
    if user_respond == 'y':
        pass
    elif user_respond == 'n':
        sys.exit('Goodbye Friend')
    else:
        # call recursive to receive valid input(y/n)
        print('Invalid Input')
        return start()
