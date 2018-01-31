# Ismael Perez Martin

# Devuelve la lista de tuplas como una matriz cuadrada, desde la fila y columnas iniciales, con una dimension indicada
def to_matriz(lista, fIni, cIni, dim):
    # Inicializamos la matriz
    matriz = []
    for i in range(fIni, fIni+dim):
        matriz.append([])
        for j in range(cIni, cIni+dim):
            matriz[i-fIni].append(None)
            matriz[i-fIni][j-cIni] = lista[i][j]

    return matriz

# Devuelve los tres primeros elementos de una lista
# Si tiene 3 elementos o menos, devuelve la lista
def tres_maximos(lista):
    if len(lista)<4:
        return lista
    else:
        return lista[0:3]

# Ordena una lista de elementos de mayor a menor
# Usa el algoritmo de ordenacion rapida
def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        # Elijo el pivote como el elemento central del array
        pivot = array[len(array)//2]

        # Divido el array entre los menos, iguales y mayores que el pivote
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        # Devuelvo la concatenacion de los arrays ordenador greater + equal + less
        return quick_sort(greater)+equal+quick_sort(less)
    else:
        return array

# Devuelve los tres mayores numeros impares de una matriz cuadrada de enteros
# Si hay menos de tres elementos impares, devuelve los que hay
def encuentra_submaximos(matriz):
    numeros = []
    mayores = []

    # Extraigo los elementos de las filas
    for i in range(len(matriz)):
        n = int(''.join(str(j) for j in matriz[i])) # Paso los elementos de la fila a un entero
        n_invertido = int(str(n)[::-1]) # Invierto el numero que acabo de sacar de la fila, ya que es tambien una posible solucion

        numeros.extend([n,n_invertido]) # Aniado el numero obtenido en cada fila, y su inverso

    diag1 = []
    diag2 = []
    # Extraigo los elementos de las columnas y diagonales
    for j in range(len(matriz)):
        aux = []
        for i in range(len(matriz)):
            aux.append(matriz[i][j])
            # Evaluamos las posiciones para saber si pertenecen a alguna diagonal
            if i==j:
                diag1.append(matriz[i][j])
            if i == abs(j-(len(matriz)-1)):
                diag2.append(matriz[i][j])

        n = int(''.join(str(j) for j in aux)) # Paso los elementos de la columna a un entero
        n_invertido = int(str(n)[::-1]) # Invierto el numero que acabo de sacar de la columna, ya que es tambien una posible solucion

        numeros.extend([n,n_invertido]) #Aniado el numero obtenido en cada columna, y su inverso

    # Extraemos los enteros de las diagonales
    d1 = int(''.join(str(j) for j in diag1)) # Paso los elementos de la primera diagonal a un entero
    d2 = int(''.join(str(j) for j in diag2)) # Paso los elementos de la segunda diagonal a un entero

    d1_invertido = int(str(d1)[::-1]) # Invierto el numero que acabo de sacar de la primera diagonal, ya que es tambien una posible solucion
    d2_invertido = int(str(d2)[::-1]) # Invierto el numero que acabo de sacar de la segunda diagonal, ya que es tambien una posible solucion

    numeros.extend([d1,d2,d1_invertido, d2_invertido]) #Aniado el numero obtenido en cada diagonal, y su inverso

    # Me quedo solo con los impares y extraigo los mayores
    impares = [x for x in numeros if x%2!=0]
    if(len(impares)>0):
        impares_ordenados = quick_sort(impares)
        mayores.extend(tres_maximos(impares_ordenados))

    # Si no tenemos 3 mayores, compruebo con los numeros de menor dimension que la matriz hasta completar los 3, o se acabasen las posibilidades
    if len(mayores)<3:
        for i in range (len(matriz)):
            aux = [n//10 for n in numeros] # Elimino el ultimo digito de todos los numeros de la matriz
            aux.extend([n%(10**(len(str(n))-1)) for n in numeros]) # Aniado los numeros eliminando el primer digito de cada numero
            numeros = aux
            impares = [x for x in numeros if x%2!=0]
            if(len(impares)>0):
                impares_ordenados = quick_sort(impares)
                if(len(mayores)+len(impares)>=3):
                    mayores.extend(impares_ordenados[:(3-len(mayores))])
                    break
                else:
                    mayores.extend(impares_ordenados)

    return mayores

# Encuentra los 3 mayores elementos impares de una matriz para su dimension n, n-1 y n-2
# Si hay menos de 3 elementos para una dimension, devuelve los que hay
def encuentra_maximo(sopa):
    maximos = []
    for k in range (3):
        maximosAux = []
        for i in range(k+1):
            for j in range(k+1): # Recorro todos los posibles bloques que se pueden formar para cada dimension
                matriz = to_matriz(sopa,i,j,len(sopa)-k)
                maximosAux.extend(encuentra_submaximos(matriz))
        maximosAux = list(set(maximosAux)) #Elimino los duplicados
        maximos.append(tuple(tres_maximos(quick_sort(maximosAux))))

    return tuple(maximos)

sopa = ([6,2,9,5,9], [2,9,6,7,8], [4,2,8,8,7], [2,2,7,4,2], [2,2,3,2,2])
assert(encuentra_maximo(sopa) == ((96873, 62959, 42887), (9687, 8769, 7869), (987, 977, 967)))

sopa1 = ([7,2,9,6,9], [2,8,6,7,9], [5,2,8,8,6], [2,2,6,4,3], [3,3,4,1,1])
assert(encuentra_maximo(sopa1) == ((99631, 97823, 96927), (9963, 9863, 9631), (985, 969, 963)))
