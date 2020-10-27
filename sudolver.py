

from sudolver import libsudolver
import readchar




saved_sudoku = [
    {
        'name': "Heft 11",
        'values': [0, 4, 0, 0, 0, 0, 0, 7, 0, 3, 9, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 8, 0, 0, 3, 0, 4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 9, 3, 0, 4, 8, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 0, 6, 9, 7, 8, 0, 0, 2, 0]
    },
    {
        'name': "Heft 11 gel",
        'values': [5, 4, 1, 3, 6, 8, 9, 7, 2, 3, 9, 8, 2, 5, 7, 6, 4, 1, 7, 2, 6, 4, 1, 9, 8, 3, 5, 9, 8, 7, 5, 4, 3, 2, 1, 6, 6, 5, 2, 8, 7, 1, 3, 9, 4, 1, 3, 4, 6, 9, 2, 7, 5, 8, 2, 1, 5, 9, 3, 6, 4, 8, 7, 8, 7, 3, 1, 2, 4, 5, 6, 9, 4, 6, 9, 7, 8, 5, 1, 2, 3]
    },
    {
        'name': "Heft 48",
        'values': [0, 0, 0, 0, 5, 0, 2, 4, 0, 2, 6, 0, 0, 0, 0, 7, 0, 9, 0, 1, 0, 0, 8, 7, 0, 6, 0, 9, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 3, 0, 0, 9, 8, 0, 0, 3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 0, 0, 0, 0, 9, 5, 1, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0]
    },
    {
        'name': "Killer 1",
        'values': [7, 0, 0, 9, 2, 0, 0, 0, 4, 0, 0, 0, 7, 8, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 9, 0, 6, 0, 9, 0, 0, 5, 0, 0, 8, 0, 8, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 5, 0, 2, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 9, 1, 0, 0]
    },
    {
        'name': "Killer 2",
        'values': [7, 0, 0, 9, 2, 0, 0, 0, 4, 0, 0, 0, 7, 8, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 9, 0, 6, 0, 9, 0, 0, 5, 0, 0, 8, 0, 8, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 5, 0, 2, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 9, 1, 0, 0]
    },
    {
        'name': "Tagesspiegel sehr schwer",
        'values': [0, 4, 0, 9, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 4, 3, 0, 0, 0, 2, 2, 5, 8, 0, 0, 6, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 5, 8, 0, 8, 0, 9, 0, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0]
    },
    {
        'name': "ps-heine.de 8 extrem ungel",
        'values': [6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 7, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 8, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 0, 0, 0, 9, 0, 0, 6, 0, 0, 0, 0, 0, 4, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 2, 1, 7, 0, 0, 0, 3, 1, 0, 5, 0]
    },




]








def readvalue():
    while True:
        inp = repr(readchar.readchar())
        inp = inp.strip("'")
        inp = inp.replace("b\'", '')  # Windows Fix
        if inp == '\\x1b':
            print()
            exit()
        elif inp == ' ':
            return 0
        try:
            value = int(inp)
            return value

        except ValueError:
            continue



def input_sudoku():
    sudoku  = list()
    print("         ANGABE")
    print(u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510')
    for block in range(3):
        for blockline in range(3):
            for l in range(3):
                print(u'\u2502', end=' ', flush=True)
                for b in range(3):
                    value = readvalue()
                    sudoku.append(value)
                    if value == 0:
                        value = ' '
                    print(value, end=' ', flush=True)

            print(u'\u2502\n', end='', flush=True)
        if block==0 or block==1:
            print(
                u'\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524',
                '', sep='')
        else:
            print(u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518')
    return sudoku



def print_sudoku(sudoku, title=None):

    pos=0
    if title:
        print('\n', title)
    else:
        print("         LÖSUNG")
    print(u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510')
    for block in range(3):
        for blockline in range(3):
            for l in range(3):
                print(u'\u2502', end=' ', flush=True)
                for b in range(3):
                    value = sudoku[pos]
                    if value == 0:
                        value = ' '
                    print(value, end=' ', flush=True)
                    pos += 1
            print(u'\u2502\n', end='', flush=True)
        if block==0 or block==1:
            print(
                u'\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524',
                '', sep='')
        else:
            print(u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518')
    return True












print('Sudolver - Sudoku Löser\n\tLucas Kranawetter, Oktober 2020\n\n')


print(' Drücke N um ein neues Rätsel einzugeben!\n Drücke L um ein Rätsel zu laden!\n Drücke ESC um zu Beenden!\n')
while True:
    inp = repr(readchar.readchar())
    inp = inp.strip("'")
    inp = inp.replace("b\'",'')  # Windows Fix
    if inp == 'n':
        sudoku = input_sudoku()

        solved_sudoku, start_sudoku, stats = libsudolver.sudolver(sudoku)

        print_sudoku(solved_sudoku)
        print(' Drücke N um ein neues Rätsel einzugeben!\n Drücke S um das Rätsel zu speichern!\n Drücke D um Details anzuzeigen!\n Drücke ESC um zu Beenden!\n')
        while True:
            inp2 = repr(readchar.readchar())
            inp2 = inp2.strip("'")
            inp2 = inp2.replace("b\'", '')  # Windows Fix
            if inp2 == 'n':
                break
            elif inp2 == "s":
                continue ##daweil
            elif inp2 == "d":
                print(sudoku)
                print(stats)
            elif inp2 == '\\x1b':
                exit(0)

    elif inp == 'l':
        print(' Gespeicherte Rätsel:')
        for x in saved_sudoku:
            print('\t', x['name'])
        while True:
            print('\nLaden: ', end='')
            load = input()

            res = next((sub for sub in saved_sudoku if sub['name'] == load), None)
            if res:
                print_sudoku(res['values'], title=res['name'])
                solved_sudoku, start_sudoku, stats = libsudolver.sudolver(res['values'])
                print_sudoku(solved_sudoku)
                exit(0)
    elif inp == '\\x1b':
        exit(0)

