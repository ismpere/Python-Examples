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
    impares = []

    # Extraigo los mayores elementos de las filas
    for i in range(len(matriz)):
        n = int(''.join(str(j) for j in matriz[i])) # Paso los elementos de la fila a un entero

        n_invertido = int(str(n)[::-1]) # Invierto el numero que acabo de sacar de la fila, ya que es tambien una posible solucion

        if n%2 != 0:
            impares.append(n)
        if n_invertido%2 != 0:
            impares.append(n_invertido)

    # Extraigo los mayores elementos de las columnas
    for j in range(len(matriz)):
        aux = []
        for i in range(len(matriz)):
            aux.append(matriz[i][j])

        n = int(''.join(str(j) for j in aux)) # Paso los elementos de la columna a un entero

        n_invertido = int(str(n)[::-1]) # Invierto el numero que acabo de sacar de la columna, ya que es tambien una posible solucion

        if n%2 != 0:
            impares.append(n)
        if n_invertido%2 != 0:
            impares.append(n_invertido)

    # Ordeno los elementos encontrados
    impares_ordenados = quick_sort(impares)
    # Devuelvo los 3 mayores elementos, o en su defecto de que no haya 3, los que haya
    return tres_maximos(impares_ordenados)

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

def main():
    sopa = ([6,2,9,5,9], [2,9,6,7,8], [4,2,8,8,7], [2,2,7,4,2], [2,2,3,2,2])
    print (encuentra_maximo(sopa))

if __name__ == "__main__":	#Si el programa se ejecuta directamente o se pasa como argumento al interprete se ejecute el main
    main()
