def primo(n):
	Boo = True
	for i in range(2,n):
		if n % i == 0:
			Boo = False;
	return Boo


def buscar(n,c,lista_semiprimos):
	x = n
	while c>len(lista_semiprimos) :

		semi_primo = False
		i = 2
		while not(semi_primo) and i<x//2+1:
			if (x % i == 0) and primo(i) and primo(x // i):
				lista_semiprimos.append(x)
				semi_primo = True
			i+=1

		x+=1
	return lista_semiprimos





def numerosSemiPrimos():
	n = int(input('ingrese el valor por el cual empezar:'))
	c = int(input('ingrese cuantos numeros semiprimos desea:'))

	numeros_semi_primos = []

	buscar(n,c,numeros_semi_primos)

	for i in range(0,len(numeros_semi_primos)):
		print(numeros_semi_primos[i])

numerosSemiPrimos()
