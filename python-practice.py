# Escribe tu nombre

def main():
    sopa = ([6,2,9,5,9], [2,9,6,7,8], [4,2,8,8,7], [2,2,7,4,2], [2,2,3,2,2])
    print (encuentra_maximo(sopa))

def encuentra_maximo(sopa):
    maximos = []
    #matriz = to_matriz(sopa,1,0,len(sopa))
    for k in range (3):
        maximosAux = []
        for i in range(k+1):
            for j in range(k+1):
                matriz = to_matriz(sopa,i,j,len(sopa)-k)
                maximosAux.extend(encuentra_submaximos(matriz))
        maximosAux = list(set(maximosAux))
        maximos.append(tuple(tres_maximos(quick_sort(maximosAux))))

    return tuple(maximos)

def tres_maximos(lista):
    if len(lista)<4:
        return lista
    else:
        return lista[0:3]

def encuentra_submaximos(matriz):
    impares = []
    for i in range(len(matriz)):
        n = int(''.join(str(j) for j in matriz[i]))

        n_invertido = int(str(n)[::-1])

        if n%2 != 0:
            impares.append(n)
        if n_invertido%2 != 0:
            impares.append(n_invertido)

    for j in range(len(matriz)):
        aux = []
        for i in range(len(matriz)):
            aux.append(matriz[i][j])

        n = int(''.join(str(j) for j in aux))

        n_invertido = int(str(n)[::-1])

        if n%2 != 0:
            impares.append(n)
        if n_invertido%2 != 0:
            impares.append(n_invertido)

    impares_ordenados = quick_sort(impares)

    print(impares_ordenados)

    return tres_maximos(impares_ordenados)


# Devuelve la lista de tuplas como una matriz, con su dimension reducida en n unidades
def to_matriz(lista, fIni, cIni, tam):
    # Inicializamos la matriz
    matriz = []
    for i in range(fIni, fIni+tam):
        matriz.append([])
        for j in range(cIni, cIni+tam):
            matriz[i-fIni].append(None)
            matriz[i-fIni][j-cIni] = lista[i][j]
            print (matriz[i-fIni][j-cIni], end="")
        print("")
    print("\n")

    return matriz

# Ordena una lista de elementos de mayor a menor
def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        # Elijo el pivote como el elemento central del array
        pivot = array[len(array)//2]

        # Comienzo a ordenar
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        # Devuelvo la concatenacion de los arrays ordenador less + equal + greater
        return quick_sort(greater)+equal+quick_sort(less)
    else:
        return array

if __name__ == "__main__":	#Si el programa se ejecuta directamente o se pasa como argumento al interprete se ejecute el main
    main()
