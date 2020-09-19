# Criar objeto do submarino com atributos de posição:
# Criar movimentos
# Se movimento for igual a 'R', então some 1 ao x 
# movimento = input 
# movimento dividir por letras
# loop for letras com as funicções de movimento


#Class submarine, with position parameters
class Submarino:
    def __init__(self, x=False, y=False, z=False, direction=False):
        self.x, self.y, self.z, self.direction = int(x),int(y), int(z), str(direction)
        self.x, self.y, self.z, self.direction = 0, 0, 0, 'NORTE'

command = 'LLMLRMMUMUD'


direction_list = ['NORTE','LESTE','SUL','OESTE']

def getPrevNext(l,no):
    i = l.index(no)
    return[l[i - 1]]

print(getPrevNext(direction_list, 'NORTE'))



direction_list = ['NORTE','LESTE','SUL','OESTE']

def get_previous_direction(direction_list, current_direction_position):
    i = direction_list.index(current_direction_position)
    return [direction_list[i - 1]]

print(get_previous_direction(direction_list, 'NORTE'))

def get_next_direction(direction_list, current_direction_position):
    i = direction_list.index(current_direction_position)
    return[direction_list[(i + 1) % len(direction_list)]]

print (get_next_direction(direction_list, 'NORTE'))


# Receive command and split it into a list
def command_func():
    command = input('Insira o comando para o submarino: ')
    def split(command):
        return [char for char in command]
    split(command)
    return split(command)

command_func()
command = command_func()
command


split(command)

# Print Submarine class initial position
vars(Submarino())


# Print first submarine initial position
submarino = Submarino()
print(f'Posição inicial do submarino: {submarino.x} {submarino.y} {submarino.z} {submarino.direction}')


#############################################
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'
  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
de = DecoratorExample()
de.example_function()    
    
#     def moviment():
#         x_mov = x + x_mov
#         x_mov = x + x_mov 
#         x_mov = x + x_mov 
#         direction_mov = 

# x = 1
#############################################

#Split comand string into chars in a list
    def split(command):
        return [char for char in command]
    
        def movimento(command):
            command = split(command)
            for i in command:
                if i == 'R':
                    x = x+1
                    print(x)
                else:
                    print('no move')

    
    command = 'rsa'
    print(split(command)) 
    command = split(command)

    for char in command:
        if i == 'r'

#############################################
def split(command):
        return [char for char in command]

command = input()

command = split(command)
print(split(command)) 

list = ['L', 'R', 'R']
x=1
x, y, z = int(x), int(y), int(z), str(d_mov)
x, y, z, d_mov = 1, 2, 3, 'NORTE'






for i in list:
    if i == 'R':
        x = x+1
        print(x)
    elif i == 'L':
        x = x-1
    else:
        False

#############################################

# r_mov = 'R'
# l_mov = 'L'
# u_mov = 'U'
# d_mov = 'D'

r_mov, l_mov, u_mov, d_mov = 'R', 'L','U','D'

x = 1
if r_mov == 'R':
    x = x+1
else:
    print('no move')
    
    
    # def moviment(x, y_mov, z_mov, direction_mov):
    #     x_mov = x + x_mov
    #     x_mov = x + x_mov 
    #     x_mov = x + x_mov 
    #     direction_mov = 
    
    def left_mov():
        'R','L' = x-1, x+1


s1 = Submarino("Jubileu")


# right_mov = x+1
# right_mov = int(1)
# x = 0
# right_mov

for i in range (1, 5):
    print (i)
    if 1 + 1:

def sum(a=False, b=False):
    return a + b

sum(1,2)    

while  x <= 4:
    x
if x > 4:

direction = 16

# Essa função estabelece o valor correspondente a direção do submarino
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
    if direction <= -100:
        direction = str(direction)
        def split(direction):
            return [char for char in direction]
        direction_list = split(direction)
        direction_list = direction_list[0]+direction_list[-2]+direction_list[-1]
        direction = int(direction_list)
    if direction < 1:
        while direction < 1:
            direction += 4
        else:
            pass
    return direction

# teste para valores negativos
for i in range(-15, -0):
    direction_mov_condition(i)
    print(i)


#########################################################################
def direction_mov_condition(direction): # Essa função retorna o valor correspondente a direção do submarino
    ## 1 = NORTE
    ## 2 = LESTE
    ## 3 = SUL
    ## 4 = OESTE
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
    if direction <= -100:
        direction = str(direction)
        def split(direction):
            return [char for char in direction]
        direction_list = split(direction)
        direction_list = direction_list[0]+direction_list[-2]+direction_list[-1]
        direction = int(direction_list)
    if direction < 1:
        while direction < 1:
            direction += 4
        else:
            pass
    return direction

def test_direction_mov_condition():
    l = [1, 4, 10, 20, 99, 100, 123456789123456784, 0, -1, -10, -100, -12945678945614]
    for i in l:
        print(direction_mov_condition(i))

test_direction_mov_condition()


import time

def test_direction_mov_condition_with_range():
    init_time = time.perf_counter()
    for i in range (-10,10):
        #print(i)
        if direction_mov_condition(i) > 4:
            print (f'Error! Out of range, {direction_mov_condition(i)}')
        else:
            print(direction_mov_condition(i))
    final_time = time.perf_counter()
    print(f'execution time of this test = {final_time-init_time}')


test_direction_mov_condition_with_range()
#########################################################################