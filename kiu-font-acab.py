import lib_sl
import random
import time

cs =    [
            [000,255,255,000,000,000,255],
            [000,000,255,255,255,000,000],
            [000,000,000,000,255,255,255],
        ]

text = "AllColoursAreBeautiful - CCC - Street Life - AllColoursAreBeautiful - MUCCC - Corso Leopold - "
tick = 0.2

font = 	{
	    "a" :	[
			    [0,0,0,0,0],
			    [0,0,0,0,0],
			    [0,0,0,0,0],
			    [0,1,1,0,0],
			    [1,0,1,0,0],
			    [1,1,1,0,0]
			],
	    "b" :	[
			    [0,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,1,1,0]
			],
	    "c" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,1,0,0],
			    [1,0,0,0],
			    [1,1,1,0]
			],
	    "d" :	[
			    [0,0,0,0],
			    [0,0,1,0],
			    [0,0,1,0],
			    [0,1,1,0],
			    [1,0,1,0],
			    [1,1,1,0]
			],
	    "e" :	[
			    [0,0,0,0],
			    [0,1,0,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,1,1,0]
			],
	    "f" :	[
			    [0,0,0,0],
			    [0,1,1,0],
			    [0,1,0,0],
			    [1,1,1,0],
			    [0,1,0,0],
			    [0,1,0,0]
	    
			],
	    "g" :	[
			    [0,0,0,0],
			    [0,1,0,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [0,0,1,0],
			    [1,1,1,0]
			],
	    "h" :	[
			    [0,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,0,1,0]
			],
	    "i" :	[
			    [0,0],
			    [1,0],
			    [0,0],
			    [1,0],
			    [1,0],
			    [1,0]
			],
	    "j" :	[
			    [0,0,0],
			    [0,1,0],
			    [0,0,0],
			    [0,1,0],
			    [0,1,0],
			    [1,1,0]
			],
	    "k" :	[
			    [0,0,0,0],
			    [1,0,0,0],
			    [1,0,1,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,0,1,0]
			],
	    "l" :	[
			    [0,0,0],
			    [1,0,0],
			    [1,0,0],
			    [1,0,0],
			    [1,0,0],
			    [1,1,0]
			],
	    "m" :	[
			    [0,0,0,0,0,0],
			    [0,0,0,0,0,0],
			    [0,0,0,0,0,0],
			    [1,1,1,1,0,0],
			    [1,0,1,0,1,0],
			    [1,0,1,0,1,0]
			],
	    "n" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,0,1,0]
			],
	    "o" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,1,1,0]
			],
	    "p" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,0,0,0]
			],
	    "q" :	[
			    [0,0,0,0,0],
			    [0,0,0,0,0],
			    [0,0,0,0,0],
			    [1,1,1,0,0],
			    [1,0,1,0,0],
			    [1,1,0,1,0]
			],
	    "r" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,1,1,0],
			    [1,0,1,0],
			    [1,0,0,0]
			],
	    "s" :	[
			    [0,0,0,0],
			    [0,1,1,0],
			    [1,0,0,0],
			    [0,1,0,0],
			    [0,0,1,0],
			    [1,1,0,0]
			],
	    "t" :	[
			    [0,0,0,0],
			    [0,1,0,0],
			    [1,1,1,0],
			    [0,1,0,0],
			    [0,1,0,0],
			    [0,1,0,0]
			],
	    "u" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,1,1,0]
			],
	    "v" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [0,1,0,0]
			],
	    "w" :	[
			    [0,0,0,0,0,0],
			    [0,0,0,0,0,0],
			    [0,0,0,0,0,0],
			    [1,0,1,0,1,0],
			    [1,0,1,0,1,0],
			    [0,1,0,1,0,0]
			],
	    "x" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,0,1,0],
			    [0,1,0,0],
			    [1,0,1,0]
			],
	    "y" :	[
			    [0,0,0,0],
			    [0,0,0,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [0,0,1,0],
			    [1,1,1,0]
			],
	    "z" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [0,0,1,0],
			    [0,1,0,0],
			    [1,0,0,0],
			    [1,1,1,0]
			],
	    "A" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,0,1,0],
			],
	    "B" :	[
			    [0,0,0,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,1,0,0],
			],
	    "C" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,1,1,0],
			],
	    "D" :	[
			    [0,0,0,0],
			    [1,1,0,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,1,0,0],
			],
	    "E" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,1,0,0],
			    [1,0,0,0],
			    [1,1,1,0],
			],
	    "F" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,1,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			],
	    "G" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,0,1,0],
			    [1,1,1,0],
			],
	    "H" :	[
			    [0,0,0,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,0,1,0],
			],
	    "I" :	[
			    [0,0],
			    [1,0],
			    [1,0],
			    [1,0],
			    [1,0],
			    [1,0],
			],
	    "J" :	[
			    [0,0,0,0],
			    [0,0,1,0],
			    [0,0,1,0],
			    [0,0,1,0],
			    [1,0,1,0],
			    [0,1,0,0],
			],
	    "K" :	[
			    [0,0,0,0,0],
			    [1,0,0,1,0],
			    [1,0,1,0,0],
			    [1,1,0,0,0],
			    [1,0,1,0,0],
			    [1,0,0,1,0],
			],
	    "L" :	[
			    [0,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,0,0,0],
			    [1,1,1,0],
			],
	    "M" :	[
                            [0,0,0,0,0,0],
			    [1,0,0,0,1,0],
			    [1,1,0,1,1,0],
			    [1,0,1,0,1,0],
			    [1,0,0,0,1,0],
			    [1,0,0,0,1,0],
			],
	    "N" :	[
			    [0,0,0,0,0],
			    [1,0,0,1,0],
			    [1,1,0,1,0],
			    [1,0,1,1,0],
			    [1,0,0,1,0],
			    [0,0,0,0,0],
			],
            "O" :       [
                            [0,0,0,0],
                            [1,1,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,1,1,0],
                        ],
            "P" :       [
                            [0,0,0,0],
                            [1,1,1,0],
                            [1,0,1,0],
                            [1,1,1,0],
                            [1,0,0,0],
                            [1,0,0,0],
                        ],
            "Q" :       [
                            [0,0,0,0,0],
                            [1,1,1,0,0],
                            [1,0,1,0,0],
                            [1,0,1,0,0],
                            [1,0,1,0,0],
                            [1,1,0,1,0],
                        ],
            "R" :       [
                            [0,0,0,0],
                            [1,1,1,0],
                            [1,0,1,0],
                            [1,1,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                        ],
            "S" :       [
                            [0,0,0,0],
                            [0,1,1,0],
                            [1,0,0,0],
                            [0,1,0,0],
                            [0,0,1,0],
                            [1,1,1,0],
                        ],
            "T" :       [
                            [0,0,0,0],
                            [1,1,1,0],
                            [0,1,0,0],
                            [0,1,0,0],
                            [0,1,0,0],
                            [0,1,0,0],
                        ],
            "U" :       [
                            [0,0,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,1,1,0],
                        ],
            "V" :       [
                            [0,0,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [0,1,0,0],
                        ],
            "W" :       [
                            [0,0,0,0,0,0],
                            [1,0,1,0,1,0],
                            [1,0,1,0,1,0],
                            [1,0,1,0,1,0],
                            [1,0,1,0,1,0],
                            [0,1,0,1,0,0],
                        ],
            "X" :       [
                            [0,0,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [0,1,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                        ],
            "Y" :       [
                            [0,0,0,0],
                            [1,0,1,0],
                            [1,0,1,0],
                            [0,1,0,0],
                            [0,1,0,0],
                            [0,1,0,0],
                        ],
            "Z" :       [
                            [0,0,0,0],
                            [1,1,1,0],
                            [0,0,1,0],
                            [0,1,0,0],
                            [1,0,0,0],
                            [1,1,1,0],
                        ],
	    " " : [
			    [0,0],
			    [0,0],
			    [0,0],
			    [0,0],
			    [0,0],
			    [0,0],
			],
	    "-" : [
			    [0,0,0],
			    [0,0,0],
			    [1,1,0],
			    [1,1,0],
			    [0,0,0],
			    [0,0,0],
			],
	    "UNKNOWN" :	[
			    [0,0,0,0],
			    [1,1,1,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,0,1,0],
			    [1,1,1,0]
			]
	}


content = [[],[],[],[],[],[]]

def look(c):
    try:
	font[i]
	return i
    except:
	return "UNKNOWN"
    
for i in text:
    c = look(i)
    content[0]+=font[c][0]
    content[1]+=font[c][1]
    content[2]+=font[c][2]
    content[3]+=font[c][3]
    content[4]+=font[c][4]
    content[5]+=font[c][5]

l = len(content[0])

idx = 0
cx = 0

col1 = 0
col2 = 0

def pickcolor():
    global col1
    global col2
    
    col1 = random.randint(0,6)
    while 1:
	col2 = random.randint(0,6)
	if (col2 != col1):
	    break

pickcolor()    
lib_sl.update()

while 1:

    for x in range(0,16):
	cx = x + idx;
	if (cx > l - 1):
	    cx = cx - l
	    
	for y in range(0,6):
	    col = content[y][cx]
	    
	    if (col == 0):
		lib_sl.send(x,y,cs[0][col1],cs[1][col1],cs[2][col1],tick/1.5)

	    if (col == 1):
		lib_sl.send(x,y,cs[0][col2],cs[1][col2],cs[2][col2],tick/1.5)
    lib_sl.update()    
    time.sleep(tick)
    
    idx = idx + 1
    if (idx > l):
	idx = 0
	pickcolor()
