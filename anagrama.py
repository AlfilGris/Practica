def anagrama():
	s_1 = input('ingrese la primera palabra:')
	s_2 = input('ingrese la segunda palabra:')

	string_1 = list(s_1)
	string_2 = list(s_2)

	c = 0

	for i in string_1:	
		for j in string_2:
			if i == j:
				string_2.pop(string_2.index(i))
				c += 1


	if len(string_1) == c:
		print('Es un anagrama')
	else:
		print('No es un anagrama')
anagrama()