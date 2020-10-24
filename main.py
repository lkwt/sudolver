from pprint import pprint

from random import randint





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
block.append(list([30,31,32,39,40,41]))
block.append(list([33,34,35,]))

block.append(list([]))
block.append(list([39,40,41,]))
block.append(list([42,43,44,]))

for initcount in range(0,81):
    initDings = Digs(initcount)
    play.append(initDings)


for initvalue in range(0,81):
    #print(initvalue, ': ')
    #value = input()
    value = randint(1,9)
    play[initvalue].setvalue(value)

for l in line:

    for v in l:
        print(play[v].getvalue(),end=' ')
    print()
