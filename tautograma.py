def verificarTautograma(s):
	aux = s[0].lower()
	tauto = True
	for i in range(1,len(s)-1):
		while s[i] == ' ' and s[i+1] == ' ':
			i += 1 
		if (s[i] == ' ') and (aux != s[i+1].lower()):
			tauto = False

	return tauto



def tautograma():
	s = input('ingrese la oracion a verificar:')
	string = list(s)
	print(verificarTautograma(string))

tautograma()