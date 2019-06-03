def combinatoria(divisores,band,total,pos,n):
    total += divisores[pos]
    print(pos , len(divisores), total, band)
    if total == n :
        print('cambiar booleano')
        band = True
        total = 0
    else:
        for i in range(pos+1,len(divisores)):#que pasa con las funciones, no guarda la mod de las variables
            combinatoria(divisores,band,total,i,n)
        #while pos < len(divisores)-1 and not band:
        #    combinatoria(divisores,band,total,i,n) #ciclo infinito, porque?
    return band


def problema1ParcialPreparadores():
    n = int(input('ingrese el numero a revisar:'))

    div = []
    for i in range(1,n//2+1):
        if n % i == 0:
            div.append(i)

    s_perf = False
    total = 0
    for i in range(0,len(div)):
        combinatoria(div,s_perf,total,i,n)

    if s_perf:
        print('Si es semiperfecto')
    else:
        print('NO es semiperfecto')

#    for i in range(0,len(div)):
#        print(div[i])

problema1ParcialPreparadores()
