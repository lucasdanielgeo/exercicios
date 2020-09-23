from app_submarino import *

sub1 = Submarino()

sub1.get_current_position()

command = input('Insira o comando: ')
command = split_command(command)

move_submarine(command, sub1)

sub1.get_current_position()

sub2 = Submarino()


command = input('Insira o comando: ')
command = split_command(command)

move_submarine(command, sub2)
print()
sub2.get_current_position()
