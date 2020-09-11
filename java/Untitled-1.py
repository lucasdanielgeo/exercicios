def command_func():
    command = input('Insira o comando para o submarino: ')
    def split(command):
        return [char for char in command]
    split(command)
    return print(split(command))

command_func()

def menu():
    # 1. Create submarine
    # 2. Print initial position
    # 3. Send a command
    # 4. Print actual position
    command_menu = input('''Choose an option:
    1. Create submarine
    2. Print initial position
    3. Send a command
    4. Print actual position
    ''')
        if command_menu == '1':
            pass
        elif command_menu == '2':
            pass
        elif command_menu == '3':
            pass
        elif command_menu == '4':
            pass
        else:
            'Paaaaaaa'