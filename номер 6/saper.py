import math as m
import random as r












win = True
wverh = int(input('Введите ширину поля'))
hverh = int(input('Введите высоту поля'))
wniz = wverh+2
hniz = hverh+2
while(True):
	bombs = int(input('Введите количество бомб'))
	if(bombs < wverh*hverh):
		break
	else:
		print('Столько бомб не поместится!')
poleniz = []
poleverh = []
poleitogniz = [] 
for i in range(hverh):
	poleverh.append([])
	for o in range(wverh):
		poleverh[-1].append(-1)
for i in range(hniz):
	poleitogniz.append([])
	poleniz.append([])
	for o in range(wniz):
		poleitogniz[-1].append(0)
		poleniz[-1].append(0)




def draw(poleverh):
	global wverh, hverh, poleitogniz, win
	print('-'*(3*wverh))
	for i in range(hverh):
		for o in range(wverh):
			if(poleverh[i][o] == -1):
				print(' · ',end = '')
			elif(poleverh[i][o] == 0):
				if(poleitogniz[i+1][o+1] == -1):
					print(' * ',end = '')
					win = False
				else:
					
					print('',poleitogniz[i+1][o+1],'', end = '')
			elif(poleverh[i][o] == 1):
				print(' $ ', end = '')
			if(o+1 == wverh):
				print('\n')

def req(poleverh):
	global wverh, hverh
	req = []
	while(True):
		req = list(input('Введите ход').split(' '))
		if(len(req) != 3):
			print("Неправильно составлен ход")
		else:
			req[0] = int(req[0])
			req[1] = int(req[1])
			if(((req[0] > 0) and (req[0] < wverh+1)) and ((req[1] > 0) and (req[1] < hverh+1))):
				if((req[2] == 'Open') or (req[2] == 'Flag')):
					break
				else:
					print('Неправильно составлен запрос')
			else:
				print('Такой клетки нет на поле')
	if(req[2] == 'Open'):
		poleverh[req[1]-1][req[0]-1] = 0
	elif(req[2] == 'Flag'):
		poleverh[req[1]-1][req[0]-1] = 1
	return req




draw(poleverh)
firstreq = req(poleverh)


massbombs = []

for i in range(bombs):
	bomba = r.randint(0,wverh*hverh-1)
	y = bomba//wverh
	x = bomba - y*wverh
	y += 1
	x += 1
	while(True):
		if((y == firstreq[1]) and (x == firstreq[0])):
			pass
		elif(poleniz[y][x] == 0):
			poleniz[y][x] = -1
			massbombs.append([x,y])
			break
		x += 1
		if(x == wniz-1):
			x = 1
			y += 1
			if(y == hniz-1):
				y = 1




for i in range(hverh):
	for o in range(wverh):
		if(poleniz[i+1][o+1] == -1):
			poleitogniz[i+1][o+1] = -1
		else:
			poleitogniz[i+1][o+1] = -1 * (poleniz[i][o] + poleniz[i][o+1] + poleniz[i][o+2] + poleniz[i+1][o]  + poleniz[i+1][o+2] + poleniz[i+2][o] + poleniz[i+2][o+1] + poleniz[i+2][o+2])


draw(poleverh)

while(True):
	zakrklet = 0
	
	
	for i in range(hverh):
		for o in range(wverh):
			if((poleverh[i][o] == -1) or (poleverh[i][o] == 1)):
				zakrklet += 1
	if(win == False):
		print('Ты попался на бомбу! Ты проиграл хахах')
		print('Поле было вот таким:')
		for i in range(hverh):
			for o in range(wverh):
				poleverh[i][o] = 0
		draw(poleverh)
		break
	elif(zakrklet == bombs):
		print('Молодец - ты победил!')
		break
	
	req(poleverh)
	draw(poleverh)









