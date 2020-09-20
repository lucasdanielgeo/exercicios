class Submarino:
    def __init__(self, x=False, y=False, z=False, direction=False):
        direction_list = ['NORTE','LESTE','SUL','OESTE']
        self.x, self.y, self.z, self.direction = int(x),int(y), int(z), str(direction)
        self.x, self.y, self.z = 0, 0, 0, 
        self.direction = direction_list[0]
    
    def get_current_position(Submarino):
        print(f'Current submarine position: {Submarino.x} {Submarino.y} {Submarino.z} {Submarino.direction}')


    direction_list = ['NORTE','LESTE','SUL','OESTE']
    
direction_list = Submarino().direction_list

def get_current_position(Submarino):
    print(f'Submarine initial position: {Submarino.x} {Submarino.y} {Submarino.z} {Submarino.direction}')

def get_last_position(Submarino):
    print(f'Actual submarine position: {submarine.x} {submarine.y} {submarine.z} {submarine.direction}')


# input_command_string_parser()

def create_submarine():
    print('Your submarine is initialized!')
    return Submarino()



def get_previous_direction(direction_list, current_direction_position):
    i = direction_list.index(current_direction_position)
    return [direction_list[i - 1]]

def get_next_direction(direction_list, current_direction_position):
    i = direction_list.index(current_direction_position)
    return[direction_list[(i + 1) % len(direction_list)]]

# get_previous_direction(direction_list, sub.direction)

# Essa função retorna o comando
def input_command_string_parser():
    def split(command):
        return [char for char in command]
    command = input('Send a commmand to the submarine: ')
    command = command.upper()
    command = split(command)
    return command

def do_command(command, Submarino):
    for commands in command:
        if command[commands] == 'M' and Submarino.direction == 'NORTE':
            Submarino.y += 1
        elif command[commands] == 'M' and Submarino.direction == 'SUL':
            Submarino.y -= 1
        elif command[commands] == 'M' and Submarino.direction == 'LESTE':
            Submarino.x += 1
        elif command[commands] == 'M' and Submarino.direction == 'OESTE':
            Submarino.x -= 1
        elif command[commands] == 'L':
            Submarino.direction = Submarino.get_previous_direction()
        elif command[commands] == 'R':
            Submarino = Submarino.get_next_direction()
        else:
            pass
    return Submarino

def set_new_command_value(command):
    command = input_command_string_parser()
    return command


#sub = do_command(command, sub)
#print(f'Submarine initial position: {sub.x} {sub.y} {sub.z} {sub.direction}')


# input_command_string_parser()
#submarine = Submarino()
#print('Your submarine is initialized!')

# Menu da aplicação
def menu():
    # 1. Create submarine
    # 2. Print initial position
    # 3. Send a command
    # 4. Print actual position
    command_menu = input('''Choose an option and enter the number:
    1. Create Submarine 
    2. Print initial position
    3. Send a command
    4. Print actual position
    5. Reset submarine position
    ''')
    # if command_menu == 1:
    #     submarine = Submarino()
    #     print('Submarine succefuly created!')
    #     menu()
    if command_menu == '1':
        return create_submarine()
        menu()
    elif command_menu == '2':
        return get_current_position()
        menu()
    elif command_menu == '3':
        command = input_command_string_parser()
        menu()     
    elif command_menu == '4':
        if submarine == Submarino():
            return get_current_position()
        else:
            print(f'Actual submarine position: {submarine.x} {submarine.y} {submarine.z} {submarine.direction}')
            menu()
    else:
        print('Can\'t find this option, please  follow next instructions')
        menu()

        