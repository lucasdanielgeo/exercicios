class Submarino:
    def __init__(self, x=False, y=False, z=False, direction=False):
        self.x, self.y, self.z, self.direction = int(x),int(y), int(z), str(direction)
        self.x, self.y, self.z, self.direction = 0, 0, 0, 'NORTE'

def command_function():
    def split(command):
        return [char for char in command]
    command = input('Send a commmand to the submarine: ')
    command = split(command)
    return command

# command_function()
submarine = Submarino()
print('Your submarine is initialized!')


# Essa função retorna o valor correspondente a direção do submarino
## 1 = NORTE
## 2 = LESTE
## 3 = SUL
## 4 = OESTE
def direction_mov_condition(direction):
    direction = int(direction)
    if direction <= 4:
        direction
    if direction >= 100:
        direction = str(direction)
        def split(direction):
            return [char for char in direction]
        direction_list = split(direction)
        direction_list = direction_list[-2]+direction_list[-1]
        direction = int(direction_list)
    if direction > 4:
        while direction > 4:
            direction -= 4
        else:
            pass
    ## Se a soma da diração for menor que 100, pegue apenas os dois ultimos digítos
    if direction <= -100:
        direction = str(direction)
        def split(direction):
            return [char for char in direction]
        direction_list = split(direction)
        direction_list = direction_list[0]+direction_list[-2]+direction_list[-1]
        direction = int(direction_list)
    ## Se a soma da direção for menor que 1, some 4
        while direction < 1:
    if direction < 1:
            direction += 4
        else:
            pass
    return direction




def menu():
    # 1. Create submarine
    # 2. Print initial position
    # 3. Send a command
    # 4. Print actual position
    command_menu = input('''Choose an option:
    1. Print initial position
    2. Send a command
    3. Print actual position
    ''')
    # if command_menu == 1:
    #     submarine = Submarino()
    #     print('Submarine succefuly created!')
    #     menu()
    if command_menu == '1':
        print(f'Submarine initial position: {submarine.x} {submarine.y} {submarine.z} {submarine.direction}')
        menu()
    elif command_menu == '2':
        command = command_function()
        menu()     
    elif command_menu == '3':
        if submarine == Submarino():
            print(f'Submarine initial position: {submarine.x} {submarine.y} {submarine.z} {submarine.direction}')
        else:
            print(f'Actual submarine position: {submarine.x} {submarine.y} {submarine.z} {submarine.direction}')
    else:
        print('Can\'t find command, please  follow next instructions')
        menu()
#menu()
        