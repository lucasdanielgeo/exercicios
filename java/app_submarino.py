class Submarino:
    def __init__(self, x=0, y=0, z=0, direction='NORTE'):
        self.x, self.y, self.z, self.direction = x, y, z, direction
        self.direction_list = ['NORTE','LESTE','SUL','OESTE']

    def get_current_position(self):
        print(f'Current submarine position: {self.x} {self.y} {self.z} {self.direction}')

    def get_previous_direction(self):
        direction_idx_direction_list = self.direction_list.index(self.direction)
        return self.direction_list[direction_idx_direction_list - 1]

    def get_next_direction(self):
        direction_idx_direction_list = self.direction_list.index(self.direction)
        return self.direction_list[(direction_idx_direction_list + 1) % len(self.direction_list)]

sub = Submarino()

direction = sub.direction_list

# def create_submarine():
#     print('Your submarine is initialized!')
#     return Submarino()

# sub = create_submarine()

# Essa função retorna o comando
def split_command(command):
    command = command.upper()
    return [char for char in command]

def send_command(command):
    command = split_command(command)
    return command


command = send_command('RMMLMMMDDLL')

def do_command(command, Submarino):
    for i in command:
        if i == 'M' and Submarino.direction == 'NORTE':
            Submarino.y += 1
        elif i == 'M' and Submarino.direction == 'SUL':
            Submarino.y -= 1
        elif i == 'M' and Submarino.direction == 'LESTE':
            Submarino.x += 1
        elif i == 'M' and Submarino.direction == 'OESTE':
            Submarino.x -= 1
        elif i == 'L':
            Submarino.direction = Submarino.get_previous_direction()
        elif i == 'R':
            Submarino.direction = Submarino.get_next_direction()
        elif i == 'U':
            Submarino.z += 1
        elif i == 'D':
            Submarino.z -= 1
        else:
            pass
    return Submarino

do_command(command, sub)
print (sub.get_current_position())
