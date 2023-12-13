from termcolor import colored
print_col = False
screen = True
while screen:
    print(colored('^ python version tester ^ ^', 'light_magenta', 'on_blue'))
    print(colored('if this software can run correctly on the terminal.' '\n' 'it means your version of python is running correctly.' '\n' 'which means that you can type whatever you want and the program will close itself. leading you to your main terminal' '\n'))
    print(colored('how to test: type [print_colors] and then press \'enter\' for printing rainbow infinite text', 'blue'))
    print(colored('bonus tip for python terminal-based programs: use the module \'termcolor\' for colored text and background in text' '\n', 'light_magenta'))
    keyb = input('> ')
    if keyb == 'print_colors':
        screen = False
        print_col = True
    elif keyb:
        quit()
    while print_col:
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'red'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'yellow'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'blue'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'cyan'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'green'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!', 'magenta'))
        print(colored('hewwo welcome to python, please enjoy programming happily!!' '\n', 'light_magenta'))
        keybtest = input('type [1] to quit, or [4] to repeat: ')
        if keybtest == '1':
            quit()
        if keybtest == '4':
            pass
        elif keybtest:
            quit()