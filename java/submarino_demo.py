from app_submarino import *

sub1 = Submarino()

sub1.get_current_position()

print('''
Os cientistas mandarão os comandos agrupados em uma única linha, como no exemplo:
```
LMRDDMMUU
```
A saída deverá conter a coordenada final do submarino junto com sua direção, como no exemplo:
```
-1 2 0 NORTE
```
''')
command = input('Insira o comando: ')
command = split_command(command)

do_command(command, sub1)

sub1.get_current_position()


print('''
#####################################################

Dado a seguinte entrada:

(Lembrando que a posição inicial do submarino é 0, 0, 0, NORTE)
```
RMMLMMMDDLL
```

A saída esperada é:
```
2 3 -2 SUL
```
''')
sub2 = Submarino()

sub2.get_current_position()


command = input('Insira o comando: ')
command = split_command(command)

do_command(command, sub2)

sub2.get_current_position()
