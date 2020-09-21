from app_submarino import *

submarine1 = create_submarine()
submarine1.get_current_position()

submarine1.get_current_position()

submarine1.get_previous_direction (direction_list, submarine1.direction_list)

submarine1.et_next_direction(direction_list, submarine1.direction_list)

########
class Submarino:
    def __init__(self, x=False, y=False, z=False, direction=False):
        direction_list = ['NORTE','LESTE','SUL','OESTE']
        self.x, self.y, self.z, self.direction = int(x),int(y), int(z), str(direction)
        self.x, self.y, self.z = 0, 0, 0, 
        self.direction = direction_list[0]

    # def set_direction_list():
    #     direction_list = ['NORTE','LESTE','SUL','OESTE']
    #     return direction_list

    def get_current_position(Submarino):
        print(f'Current submarine position: {Submarino.x} {Submarino.y} {Submarino.z} {Submarino.direction}')

    def get_previous_direction(Submarino):
        direction_list = ['NORTE','LESTE','SUL','OESTE']
        current_direction_position = Submarino.direction
        i = direction_list.index(current_direction_position)
        return [direction_list[i - 1]]

    def get_next_direction(direction_list, current_direction_position):
        i = direction_list.index(current_direction_position)
        return[direction_list[(i + 1) % len(direction_list)]]

    direction_list = ['NORTE','LESTE','SUL','OESTE']


direction_list = Submarino().direction_list

def create_submarine():
    print('Your submarine is initialized!')
    return Submarino()


submarine1 = create_submarine()

submarine1.get_current_position()

submarine1.get_previous_direction()

submarine1.et_next_direction(direction_list, submarine1.direction_list)
