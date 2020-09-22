from app_submarino import *

sub1 = create_submarine()

sub1.get_current_position()

print(f'''
{sub1.get_previous_direction()}
{sub1.direction}
{sub1.get_next_direction()}
''')

sub1.direction = direction_list[3]
sub1.x, sub1.y, sub1.z = 2,2,2

sub1.get_current_position()

command = 'LLRR'

command = split_command(command)
print(f'command = {command}')

do_command(command, sub1)
