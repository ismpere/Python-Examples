# Escribe tu nombre

def main():
    sopa = ([6,2,9,5,9], [2,9,6,7,8], [4,2,8,8,7], [2,2,7,4,2], [2,2,3,2,2])
    encuentra_maximo(sopa)

def encuentra_maximo(sopa):
    maximos = []
    for i in range(3):
        matriz = to_matriz(sopa, i)
        print (matriz)
        maximos.append(encuentra_submaximos(matriz))

    return tuple(maximos)

def encuentra_submaximos(matriz):
    impares = []
    for i in range(len(matriz)):
        n = 0
        for j in range (len(matriz[i])):
            n += matriz[i][j] *(10 ** len(matriz[i])-j)

        n_invertido = int(str(n)[::-1])

        if n%2 != 0:
            impares.append(n)
        if n_invertido%2 != 0:
            impares.append(n_invertido)

    impares_ordenados = quick_sort(impares)

    if len(impares_ordenados)<4:
        return tuple(impares)
    else:
        return tuple(impares[len(impares)-3:])


# Devuelve la lista de tuplas como una matriz, con su dimension reducida en n unidades
def to_matriz(lista, n):
    tam = len(lista)-n
    # Inicializamos la matriz
    matriz = []
    for i in range(tam):
        matriz.append([])
        for j in range(tam):
            matriz[i].append(None)
            matriz[i][j] = lista[i][j]
            print (matriz[i][j], end="")
        print("")
    print("\n")

    return matriz


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
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array

if __name__ == "__main__":	#Si el programa se ejecuta directamente o se pasa como argumento al interprete se ejecute el main
    main()
