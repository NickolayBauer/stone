import random

M = []
row = [] 


def create_row():
	palm = random.randint(3,5)
	stone = random.randint(3,palm)
	row = []
	while len(row) < 10:
		elem = random.randint(1,61)
		if elem <20:
			row.append(0)
		elif elem >=20 and elem < 40 and palm > 0:
			row.append(1)
			palm=-1
		elif elem >=40 and elem <= 60 and stone > 0:
			row.append(2)
			stone =-1 
		if elem%2 == 0:
			row = row[::-1]

	return row


def create_map():
	for row in range(10):
		M.append(create_row())
	M[random.randint(0,len(M)-1)][random.randint(0,len(M[0])-1)] = 3
	return M




def show_map(M):
	for row in M:
		print(row)

def search_klad(M): 
	
	
	mass_palm = []
	mass_stone = []

	for row in M:
		for elem in row:
				if elem == 1:
				    mass_palm.append(M.index(row))
				elif elem == 2:
				    mass_stone.append(row.index(elem))


	while True:
		Upalm = int(input('по вертикали относительно пальмы(1): '))
		Ustone = int(input('по горизонтали относительно камня(2): '))
		for palm in mass_palm:
			for stone in mass_stone:
				try:
					if M[palm+Upalm][stone+Ustone] == 3 :
						print("Найдено, координаты клада: M",[palm+Upalm],[stone+Ustone])
						return 
				except IndexError:
					pass

		print('ничего не найдено, попробуйте ввести координаты ещё раз')		




M = create_map()
show_map(M)
search_klad(M)

