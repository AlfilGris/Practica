global z

def combinaciones (div,suma,pos,n):

	suma += div[pos]
	
	if suma == n:
		z = True
	else:
		for i in range(pos+1,len(div)):
			#print(pos)
			combinaciones(div,suma,pos+1,n)
			




def problema1ParcialPreparadores():
	n = 18
	z = False
	divisores = []
	for i in range(1,n//2+1):
		if n % i == 0 :
			divisores.append(i)

	suma = 0
	pos = 0
	combinaciones(divisores,suma,pos,n)

	if z :
		print('El nro es semiperfecto')
	else:
		print('NO es semiperfecto')


problema1ParcialPreparadores()