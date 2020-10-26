import logging
from pprint import pprint

## Basiskonfiguration
logging.basicConfig(filename='sudolver.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
logging.info("Running sudolver")




### KLASSE DER WERTE DER FELDER
# Insgesamt werden 81 Objekte von der Klasse 'Digs' abgeleitet und in die Liste 'play' gespeichert.
#
# __init__
# Beim Initialisieren wird die Position des Feldes 'pcount' gespeichert (Beginnend mit 0 links oben, bis 80 rechts unten.)
# Des weiteren werden die möglichen Werte in einem Set gespeichert (1-9) und das Feld wird einer Zeile, einer Reihe
# und einem Block zugeordnet (line, row, block)
#
# setvalue(Wert)
# Ein bestimmer Wert wird dem Feld zugewiesen. Das Set der möglichen Werte wird gelöscht und in den Feldern der verbundene Zeile, Reihe,
# und im selben Block, wird der zugewiesene Wert aus dem Set der möglichen Werte entfernt.
#
# setstartvalue(Wert)
# Identisch mit 'setvalue' zusätzlich wird der Wert als Startwert gespeichert. Das ist notwendig damit die Angabe
# wiederhergestellt werden kann.
#
# getvalue
# Liefert den aktuellen Wert des Felds zurück.
#
# getstartvalue
# Liefert den Wert des Feldes bei der Angabe zurück.

class Digs:
    def __init__(self, pcount):
        self.pcount = pcount
        self.poss_values = set({1,2,3,4,5,6,7,8,9})

        for index, v in enumerate(line):
            if self.pcount in v:
                self.line = index
        for index, v in enumerate(row):
            if self.pcount in v:
                self.row = index
        for index, v in enumerate(block):
            if self.pcount in v:
                self.block = index

    def setvalue(self, v):
        self.v = v
        self.poss_values.clear()

        for x in line[self.line]:
            if v in play[x].poss_values:
                play[x].poss_values.remove(v)


        for x in row[self.row]:
            if v in play[x].poss_values:
                play[x].poss_values.remove(v)

        for x in block[self.block]:
            if v in play[x].poss_values:
                play[x].poss_values.remove(v)


    def setstartvalue(self, v):
        self.setvalue(v)
        self.startv = v



    def getvalue(self):
        return self.v

    def getstartvalue(self):
        return self.startv









### UNTERSTÜTZENDE FUNKTIONEN

## ANZAHL DER BEREITS BEKANNTEN WERTE IM SUDOKU FINDEN
def getinfo():
    known_values=0
    for x in play:
        if x.v != 0:
            known_values += 1
    return known_values



### LÖSUNGSALGORITHMEN

## ALGORITHMUS 1
## Jedes Feld durchgehen und die Schnittmenge aus möglichen Werten in Zeile, Reihe und Block bilden.
## Ist die Schnittmenge ein Zeichen lag, ist der Wert gefunden und wird eingesetzt.



def check_group(sudoku_object):
    possiblevalues = set({1,2,3,4,5,6,7,8,9})
    for x in sudoku_object:
        v = play[x].getvalue()
        if v != 0:
            possiblevalues.remove(v)
    return possiblevalues

def alg_1(dig_id):
    #print(play[dig_id].getvalue())
    if play[dig_id].getvalue() != 0:
#        print('Bereits gesetzt')
        return False

    myline_possiblevalues = check_group(line[play[dig_id].line])
    myrow_possiblevalues = check_group(row[play[dig_id].row])
    myblock_possiblevalues = check_group(block[play[dig_id].block])

    dig_intersection_values = myline_possiblevalues.intersection(myrow_possiblevalues, myblock_possiblevalues)

    logging.info('\n\nDig '+ str(dig_id))
    logging.info(' gefunden in Line ' + str(play[dig_id].line) + ' Row ' + str(play[dig_id].row) + ' Block ' + str(play[dig_id].block))
    logging.info(' Mögliche Werte:\n\tLine ' + str(myline_possiblevalues) + ' \n\tRow ' + str(myrow_possiblevalues) + '\n\tBlock ' + str(myblock_possiblevalues) + '\n\tIntersection: ' + str(dig_intersection_values) + ' len ' + str(dig_intersection_values.__len__()))

    if dig_intersection_values.__len__() == 1:
        for x in dig_intersection_values:
            play[dig_id].setvalue(x)
        return True
    else:
        play[dig_id].poss_values = dig_intersection_values

        return False

## ALGORITHMUS 2
## Jedes Feld durchgehen und die Restmenge aus den eigenen möglichen Werten und jenen der anderer Felder in
## dem selben Block bilden.
## Ist die Restmenge ein Zeichen lag, ist der Wert gefunden und wird eingesetzt.

def alg_2(dig_id):
    if play[dig_id].getvalue() != 0:
        #        print('Bereits gesetzt')
        return False

    dig_difference_values = play[dig_id].poss_values
    for x in block[play[dig_id].block]:
        if x != dig_id and play[x].poss_values != {}:
            # print( x, play[x].poss_values)
            dig_difference_values = dig_difference_values.difference(play[x].poss_values)
    logging.info('\tDifference Block:' + str(dig_difference_values))
    if dig_difference_values.__len__() == 1:
        for x in dig_difference_values:
            play[dig_id].setvalue(x)
        return True
    else:
        return False


## ALGORITHMUS 3
## Jedes Feld durchgehen und die Restmenge aus den eigenen möglichen Werten und jenen der anderer Felder in
## der selben Zeile bilden.
## Ist die Restmenge ein Zeichen lag, ist der Wert gefunden und wird eingesetzt.

def alg_3(dig_id):
    if play[dig_id].getvalue() != 0:
        #        print('Bereits gesetzt')
        return False

    dig_difference_values = play[dig_id].poss_values
    logging.info(str(dig_difference_values))
    for x in line[play[dig_id].line]:
        if x != dig_id and play[x].poss_values != {}:
            logging.info( str(x) + ' ' + str(play[x].poss_values))
            dig_difference_values = dig_difference_values.difference(play[x].poss_values)
    logging.info('\tPos: ' + str(dig_id) + ' Difference Lines: '+ str(dig_difference_values))
    if dig_difference_values.__len__() == 1:
        for x in dig_difference_values:
            play[dig_id].setvalue(x)
        return True
    else:
        return False

## ALGORITHMUS 4
## Jedes Feld durchgehen und die Restmenge aus den eigenen möglichen Werten und jenen der anderer Felder in
## der selben Spalte bilden.
## Ist die Restmenge ein Zeichen lag, ist der Wert gefunden und wird eingesetzt.

def alg_4(dig_id):
    if play[dig_id].getvalue() != 0:
        #        print('Bereits gesetzt')
        return False

    dig_difference_values = play[dig_id].poss_values
    logging.info(str(dig_difference_values))
    for x in row[play[dig_id].row]:
        if x != dig_id and play[x].poss_values != {}:
            logging.info( str(x) + ' ' + str(play[x].poss_values))
            dig_difference_values = dig_difference_values.difference(play[x].poss_values)
    logging.info('\tPos: ' + str(dig_id) + ' Difference Rows: '+ str(dig_difference_values))
    if dig_difference_values.__len__() == 1:
        for x in dig_difference_values:
            play[dig_id].setvalue(x)
        return True
    else:
        return False


## Aktuellen Zustand des Sudokus ausgeben


def printsudoku():
    print(u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510')
    hlim = 0
    for index, l in enumerate(line):
        print(u'\u2502', end='')
        vlim = 0
        for v in l:
            if vlim == 3:
                print(u' \u2502', end='')
                vlim = 0
            if play[v].getvalue() == 0:
                print('  ', end='')
            else:
                print('', play[v].getvalue(), end='')
            vlim += 1
        hlim += 1
        print(u' \u2502')
        if hlim == 3 and index != 8:
            print(
                u'\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524',
                '', sep='')
            hlim = 0

    print(u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518')


## Zustand des Sudokus am Start ausgeben

def printstartsudoku():
    print(
        u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510')
    hlim = 0
    for index, l in enumerate(line):
        print(u'\u2502', end='')
        vlim = 0
        for v in l:
            if vlim == 3:
                print(u' \u2502', end='')
                vlim = 0
            if play[v].getstartvalue() == 0:
                print('  ', end='')
            else:
                print('', play[v].getstartvalue(), end='')
            vlim += 1
        hlim += 1
        print(u' \u2502')
        if hlim == 3 and index != 8:
            print(
                u'\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524',
                '', sep='')
            hlim = 0

    print(
        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518')


### INITIALISIERUNG DES SPIELBRETTS

# Liste die alle Felder-Objekte enthalten wird
play = list()

# Liste mit den Referenzwerten aller Zeilen (0-8, absteigend)
line = list()
line.append(list([ 0, 1, 2, 3, 4, 5, 6, 7, 8]))
line.append(list([ 9,10,11,12,13,14,15,16,17]))
line.append(list([18,19,20,21,22,23,24,25,26]))

line.append(list([27,28,29,30,31,32,33,34,35]))
line.append(list([36,37,38,39,40,41,42,43,44]))
line.append(list([45,46,47,48,49,50,51,52,53]))

line.append(list([54,55,56,57,58,59,60,61,62]))
line.append(list([63,64,65,66,67,68,69,70,71]))
line.append(list([72,73,74,75,76,77,78,79,80]))

# Liste mit den Referenzwerten aller Spalten (0-8, von links nach rechts)
row = list()
row.append(list([ 0, 9,18,27,36,45,54,63,72]))
row.append(list([ 1,10,19,28,37,46,55,64,73]))
row.append(list([ 2,11,20,29,38,47,56,65,74]))

row.append(list([ 3,12,21,30,39,48,57,66,75]))
row.append(list([ 4,13,22,31,40,49,58,67,76]))
row.append(list([ 5,14,23,32,41,50,59,68,77]))

row.append(list([ 6,15,24,33,42,51,60,69,78]))
row.append(list([ 7,16,25,34,43,52,61,70,79]))
row.append(list([ 8,17,26,35,44,53,62,71,80]))

# Liste mit den Referenzwerten aller Blöcke (0-8, von links oben zeilenweise nach rechts unten)
block = list()
block.append(list([ 0, 1, 2, 9,10,11,18,19,20]))
block.append(list([ 3, 4, 5,12,13,14,21,22,23]))
block.append(list([ 6, 7, 8,15,16,17,24,25,26]))

block.append(list([27,28,29,36,37,38,45,46,47]))
block.append(list([30,31,32,39,40,41,48,49,50]))
block.append(list([33,34,35,42,43,44,51,52,53]))

block.append(list([54,55,56,63,64,65,72,73,74]))
block.append(list([57,58,59,66,67,68,75,76,77]))
block.append(list([60,61,62,69,70,71,78,79,80]))





def sudolver(sudokulist):
    # Inistialisierung der 81 Felder-Objekte
    for initcount in range(0,81):
        initDings = Digs(initcount)
        play.append(initDings)






    #anfangswerte befüllen
    for initvalue in range(0,81):
        value = sudokulist[initvalue]
        play[initvalue].setstartvalue(value)



    startvalue = getinfo()


    algorithms = {'alg_1': alg_1,
                  'alg_2': alg_2,
                  'alg_3': alg_3,
                  'alg_4': alg_4}

    stats = dict()

    big_loop = 0

    known = startvalue

    while known !=81:
        big_loop += 1
        last_known = known
        for alg_name in ['alg_1', 'alg_2', 'alg_3', 'alg_4']:
            check = True
            loop=0
            while check:
                check = False
                loop += 1
                logging.info('Loop: ' + str(loop))
                for dig in range(81):
                    if algorithms[alg_name](dig):
                        check = True
            logging.info("Total Loop: " + str(loop))

            known = getinfo()
            stats[str(big_loop)+'_nach_'+alg_name] = getinfo()
            stats[str(big_loop)+'_loop_'+alg_name] = loop
        if last_known == known:
            #print(" Eine Veränderung - abbruch")
            break

    #printstartsudoku()

#    printsudoku()
    #print('Bekannte Werte:')
    #print('\t Bei Start:', startvalue)
    #pprint(stats)


    solved_sudoku = list()
    start_sudoku = list()

    for x in play:
        solved_sudoku.append(x.getvalue())
    for x in play:
        start_sudoku.append(x.getstartvalue())


    return  solved_sudoku, start_sudoku, stats