from pprint import pprint

from random import randint

def check(play, object):
    possiblevalues = set({1,2,3,4,5,6,7,8,9})
    for x in object:
        value = play[x].getvalue()
        if value!=0:
            possiblevalues.remove(value)
    print('Mögliche Werte:')
    pprint(possiblevalues)

def printsudoku(play,line):
    hlim = 0
    for l in line:

        vlim = 0
        for v in l:
            if vlim == 3:
                print('|', end=' ')
                vlim = 0
            if play[v].getvalue()==0:
                print(' ', end=' ')
            else:
                print(play[v].getvalue(), end=' ')
            vlim += 1
        hlim += 1
        print()
        if hlim == 3:
            print('---------------------')
            hlim = 0


class Digs:
    def __init__(self, pcount):
        self.pcount = pcount


    def setvalue(self, value):
        self.value = value

    def getvalue(self):
        #print('pCount:', self.pcount, ' Value:', self.value)
        return self.value






play = list()

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

for initcount in range(0,81):
    initDings = Digs(initcount)
    play.append(initDings)


# test anfang
anfang = list([0,1,2,0,0,0,5,7,0,
               6,0,0,5,0,1,0,0,4,
               4,0,0,0,2,0,0,0,8,

               0,2,0,0,1,0,0,5,0,
               0,0,4,9,0,7,8,0,0,
               0,7,0,0,8,0,0,1,0,

               7,0,0,0,9,0,0,0,5,
               5,0,0,4,0,8,0,0,6,
               0,3,8,0,0,0,9,4,0])
# test fertig
fertig = list([9,1,2,8,4,6,5,7,3,
               6,8,3,5,7,1,2,9,4,
               4,5,7,3,2,9,1,6,8,

               8,2,9,6,1,3,4,5,7,
               1,6,4,9,5,7,8,3,2,
               3,7,5,2,8,4,6,1,9,

               7,4,6,1,9,2,3,8,5,
               5,9,1,4,3,8,7,2,6,
               2,3,8,7,6,5,9,4,1])


##zufallswerte befüllen
#for initvalue in range(0,81):
#    #print(initvalue, ': ')
#    #value = input()
#    value = randint(1,9)
#    play[initvalue].setvalue(value)

#anfangswerte befüllen
#for initvalue in range(0,81):
#    value = anfang[initvalue]
#    play[initvalue].setvalue(value)

##endwerte befüllen
for initvalue in range(0, 81):
    value = fertig[initvalue]
    play[initvalue].setvalue(value)




printsudoku(play, line)

print("Reihe 1:")
check(play, line[0])

print("Spalte 2:")
check(play, row[1])

print("Block 3:")
check(play, block[2])

#strukturcheck
#print('Block 5:')
#for x in block[5]:
#  print(play[x].getvalue(), end=' ')
#
#print()
#print('Reihe 4:')
#for x in row[4]:
#    print(play[x].getvalue(), end=' ')