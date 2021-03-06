import os
import pickle

f = pickle.load(open('data.p' ,'rb'))
x = f['x']
y = f['y']
completed = f['completed']

def action():
    global x
    global y
    global completed

    if x == 1:
        if y == 3:
            completed = 1
    elif x == 2:
        if y == 4:
            completed = 1

def box():
    print('|   |   |   |   |')
    print('|   |   |   |   |')
    print('|___|___|___|___|')

def box1():
    print('|   |   |   |   |')
    print('| * |   |   |   |')
    print('|___|___|___|___|')

def box2():
    print('|   |   |   |   |')
    print('|   | * |   |   |')
    print('|___|___|___|___|')

def box3():
    print('|   |   |   |   |')
    print('|   |   | * |   |')
    print('|___|___|___|___|')

def box4():
    print('|   |   |   |   |')
    print('|   |   |   | * |')
    print('|___|___|___|___|')

def startOfBox():
    print(' ___ ___ ___ ___')

def topOfBox():
    print('|   |   |   |   |')

def endOfBox():
    print('|___|___|___|___|')

def updateImage():
    global x
    global y
    global completed

    if completed == 1:
        if x == 1:
            if y == 1:
                startOfBox()
                box1()
                box()
                box()
                box()
            elif y == 2:
                startOfBox()
                box2()
                box()
                box()
                box()
            elif y == 3:
                startOfBox()
                box3()
                box()
                box()
                box()
            else:
                startOfBox()
                box4()
                box()
                box()
                box()
        elif x == 2:
            if y == 1:
                startOfBox()
                box()
                box1()
                box()
                box()
            elif y == 2:
                startOfBox()
                box()
                box2()
                box()
                box()
            elif y == 3:
                startOfBox()
                box()
                box3()
                box()
                box()
            else:
                startOfBox()
                box()
                box4()
                box()
                box()
        elif x == 3:
            if y == 1:
                startOfBox()
                box()
                box()
                box1()
                box()
            elif y == 2:
                startOfBox()
                box()
                box()
                box2()
                box()
            elif y == 3:
                startOfBox()
                box()
                box()
                box3()
                box()
            else:
                startOfBox()
                box()
                box()
                box4()
                box()
        else:
            if y == 1:
                startOfBox()
                box()
                box()
                box()
                box1()
            elif y == 2:
                startOfBox()
                box()
                box()
                box()
                box2()
            elif y == 3:
                startOfBox()
                box()
                box()
                box()
                box3()
            else:
                startOfBox()
                box()
                box()
                box()
                box4()
    else:
        if x == 1:
            if y == 1:
                startOfBox()
                topOfBox()
                print('| * |   |   | * |')
                endOfBox()
                box()
                box()
                box()
            elif y == 2:
                startOfBox()
                topOfBox()
                print('|   | * |   | * |')
                endOfBox()
                box()
                box()
                box()
            else:
                startOfBox()
                topOfBox()
                print('|   |   | * | * |')
                endOfBox()
                box()
                box()
                box()
        elif x == 2:
            if y == 1:
                startOfBox()
                box4()
                box1()
                box()
                box()
            elif y == 2:
                startOfBox()
                box4()
                box2()
                box()
                box()
            elif y == 3:
                startOfBox()
                box4()
                box3()
                box()
                box()
            else:
                startOfBox()
                box4()
                box4()
                box()
                box()
        elif x == 3:
            if y == 1:
                startOfBox()
                box4()
                box()
                box1()
                box()
            elif y == 2:
                startOfBox()
                box4()
                box()
                box2()
                box()
            elif y == 3:
                startOfBox()
                box4()
                box()
                box3()
                box()
            else:
                startOfBox()
                box4()
                box()
                box4()
                box()
        else:
            if y == 1:
                startOfBox()
                box4()
                box()
                box()
                box1()
            elif y == 2:
                startOfBox()
                box4()
                box()
                box()
                box2()
            elif y == 3:
                startOfBox()
                box4()
                box()
                box()
                box3()
            else:
                startOfBox()
                box4()
                box()
                box()
                box4()

def playerMovement():
    global x
    global y

    print('\n')
    print('1) Up')
    print('2) Left')
    print('3) Down')
    print('4) Right')
    print('5) Action')
    print('6) Exit')
    print('\n')

    asdf = input('Enter in your input: ')

    if asdf == '1':
        x -= 1
        os.system('cls')
    elif asdf == '2':
        y -= 1
        os.system('cls')
    elif asdf == '3':
        x += 1
        os.system('cls')
    elif asdf == '4':
        y += 1
        os.system('cls')
    elif asdf == '5':
        action()
        os.system('cls')
    elif asdf == '6':
        exit()
        os.system('cls')
    elif asdf == 'w':
        x -= 1
        os.system('cls')
    elif asdf == 'a':
        y -= 1
        os.system('cls')
    elif asdf == 's':
        x += 1
        os.system('cls')
    elif asdf == 'd':
        y += 1
        os.system('cls')
    elif asdf == 'q':
        action()
        os.system('cls')
    elif asdf == 'x':
        exit()

    pickle.dump({'x': x, 'y': y, 'completed': completed}, open('data.p' ,'wb'))
    updateImage()
    playerMovement()

updateImage()
playerMovement()