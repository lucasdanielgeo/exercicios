from app_submarino import *

submarine1 = create_submarine()
name = 'sub1'
name = create_submarine()
submarine1.get_current_position()

print(f'''
{submarine1.get_previous_direction()}
{submarine1.direction}
{submarine1.get_next_direction()}
''')

submarine1.direction = direction_list[3]

submarine1.get_current_position()

command = 'LLRR'

command = split_command(command)

print(command)