# Ismael Perez Martin

# Devuelve el mayor numero de una matriz cuadrada de enteros, pasada como un string
def encuentra_maximo(sopa):
    maximo = -1
    numeros = []
    matriz = to_matriz(sopa)

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

        numeros.extend([n,n_invertido]) # Aniado el numero obtenido en cada columna, y su inverso

    # Extraemos los enteros de las diagonales
    d1 = int(''.join(str(j) for j in diag1)) # Paso los elementos de la primera diagonal a un entero
    d2 = int(''.join(str(j) for j in diag2)) # Paso los elementos de la segunda diagonal a un entero

    d1_invertido = int(str(d1)[::-1]) # Invierto el numero que acabo de sacar de la primera diagonal, ya que es tambien una posible solucion
    d2_invertido = int(str(d2)[::-1]) # Invierto el numero que acabo de sacar de la segunda diagonal, ya que es tambien una posible solucion

    numeros.extend([d1,d2,d1_invertido, d2_invertido]) # Aniado el numero obtenido en cada diagonal, y su inverso

    # Me quedo solo con los impares y extraigo el mayor
    impares = [x for x in numeros if x%2!=0]
    if(len(impares)>0):
        maximo = max(impares)
    # Si no hay ningun numero impar, compruebo con los de menor dimension que la matriz
    else:
        for i in range (len(matriz)):
            numeros = [n//10 for n in numeros] # Elimino el ultimo digito de todos los numeros de la matriz
            impares = [x for x in numeros if x%2!=0]
            if(len(impares)>0):
                maximo = max(impares)
                break

    return maximo


# Devuelve el string como una matriz cuadrada
def to_matriz(sopa):
    lista = sopa.split("\n")

    # Inicializamos la matriz y la rellenamos
    matriz = []
    for i in range(len(lista)):
        matriz.append([])
        for j in range(len(lista)):
            matriz[i].append(None)
            matriz[i][j] = lista[i][j]

    return matriz


#Aprobado
##Sin números impares
assert(encuentra_maximo('''62\n28''') == -1)
##2x2
assert(encuentra_maximo('''62\n27''') == 67)

#5x5
##Columna arriba-abajo
assert(encuentra_maximo('''62959\n29678\n42887\n22742\n22322''') == 96873)
##Columna abajo-arriba
assert(encuentra_maximo('''62656\n29678\n42886\n22742\n22222''') == 24875)
##Fila izquierda-derecha
assert(encuentra_maximo('''62656\n29679\n42886\n22742\n22222''') == 29679)
##Fila derecha-izquierda
assert(encuentra_maximo('''62656\n79679\n42886\n22742\n22222''') == 97697)

#10x10

assert(encuentra_maximo('''6743605871\n1820953321\n8958054851\n7486519455\n1389386144\n4672017818\n9082874626\n6728050071\n1684990063\n4374367650''') == 8958054851)


##Diagonales
assert(encuentra_maximo('''92656\n79679\n42886\n22782\n22221''') == 99881)
assert(encuentra_maximo('''32651\n71674\n42885\n22742\n72223''') == 72871)
assert(encuentra_maximo('''32659\n79674\n42886\n22742\n12229''') == 97821)
assert(encuentra_maximo('''32639\n79674\n42886\n22742\n22229''') == 94893)

#Soluciones con m < n
assert(encuentra_maximo('''41622\n24084\n42084\n27746\n40220''') == 7241)
assert(encuentra_maximo('''42622\n24684\n42084\n22742\n42220''') == 6607)
assert(encuentra_maximo('''44444\n44444\n44944\n44444\n44444''') == 449)
assert(encuentra_maximo('''4444\n4444\n4944\n4444''') == 449)
