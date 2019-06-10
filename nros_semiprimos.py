def primo(n):
	Boo = True
	i = 1
	while Boo and i in range(1,n//2):
		i += 1
		if n % i == 0:
			Boo = False;
	return Boo



def semiPrimo(n):
	semi_primo = False
	i = 1
	while not(semi_primo) and i in range(1,n//2):
		i += 1
		if (n % i == 0) and primo(i) and primo(n // i):
			semi_primo = True
	return semi_primo



def buscar(n,c,lista_semiprimos):
	i = n
	while c>len(lista_semiprimos) :
		if semiPrimo(i):
			lista_semiprimos.append(i)
		i += 1


	return lista_semiprimos





def numerosSemiPrimos():
	n = int(input('ingrese el valor por el cual empezar:'))
	c = int(input('ingrese cuantos numeros semiprimos desea:'))

	numeros_semi_primos = []

	buscar(n,c,numeros_semi_primos)

	for i in range(0,len(numeros_semi_primos)):
		print(numeros_semi_primos[i])

numerosSemiPrimos()
