def primo(n):
	Boo = False
	for i in range(2,n):
		if n % i == 0:
			boo = True;
	return Boo


def buscar(n,c,numeros_semi_primos):
	x = c
	while c>len(numeros_semi_primos) :

		semi_primo = False
		i = 2
		while not(semi_primo) or i<x//2+1:
			if (x % i == 0) and primo(i) and primo(x // i):
				numeros_semi_primos.append(x)
				semi_primo = True
			i+=1

		x+=1
	return numeros_semi_primos





def numerosSemiPrimos():
	n = int(input('ingrese el valor por el cual empezar:'))
	c = int(input('ingrese cuantos numeros semiprimos desea:'))

	numeros_semi_primos = []

	buscar(n,c,numeros_semi_primos)

	for i in range(0,len(numeros_semi_primos)):
		print(numeros_semi_primos[i])

numerosSemiPrimos()