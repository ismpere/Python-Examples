# Escribe tu nombre

def main():
    array=[12,4,5,6,7,3,1,15]
    array2 = quickSort(array)
    for i in array2:
        print (i)


def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        # Elijo el pivote como el elemento central del arrau
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
        return quickSort(less)+equal+quickSort(greater)
    else:
        return array

if __name__ == "__main__":	#Si el programa se ejecuta directamente o se pasa como argumento al interprete se ejecute el main
    main()
