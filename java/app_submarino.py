class Submarino:
    def __init__(self, x=0, y=0, z=0, direction='NORTE'):
        self.x, self.y, self.z, self.direction = x, y, z, direction
        self.direction_list = ['NORTE','LESTE','SUL','OESTE']

    def get_current_position(self):
        print(f'Current submarine position: {self.x} {self.y} {self.z} {self.direction}')

    def get_previous_direction(self):
        i = self.direction_list.index(self.direction)
        return [self.direction_list[i - 1]]

    def get_next_direction(self):
        i = self.direction_list.index(self.direction)
        return[self.direction_list[(i + 1) % len(self.direction_list)]]

sub = Submarino()

direction = sub.direction_list

def create_submarine():
    print('Your submarine is initialized!')
    return Submarino()

sub = create_submarine()

# Essa função retorna o comando
def split_command(command: str) -> list:
    command = command.upper()
    return [char for char in command]

def send_command(command):
    command = split_command(command)
    return command


command = send_command('LLMRRMUU')

def do_command(command, Submarino):
    for i in command:
        if i == 'M' and Submarino.direction == direction_list[0]:
            Submarino.y += 1
        elif i == 'M' and Submarino.direction == direction_list[2]:
            Submarino.y -= 1
        elif i == 'M' and Submarino.direction == direction_list[1]:
            Submarino.x += 1
        elif i == 'M' and Submarino.direction == direction_list[3]:
            Submarino.x -= 1
        elif i == 'L':
            Submarino.direction = Submarino.get_previous_direction()
        elif i == 'R':
            Submarino = Submarino.get_next_direction()
        else:
            pass
    return Submarino

do_command(command, sub)
