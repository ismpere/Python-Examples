#Extrae la dimensión de la sopa de entrada.
def extrae_dimension(soup):
    """Extrae la dimensión de la sopa de números"""
    return soup.count('\n') + 1

#Devuelve el caracter en la posicion [fila, columna] de la sopa, dada la dimension de la misma
def char_at_position(soup, dim, fila, columna):
    return soup[(dim+1)*fila + columna]

def leer_horizontal(sopa,dim,num):
    contador=0
    nuevo=""
    mayor=num
    for e in sopa:
        if (contador<dim):
            nuevo=num+1
            if (int(nuevo)%2 !=0 and int(nuevo)>int(mayor)):
                mayor=nuevo
        contador=(contador+1)
        if (contador==(dim+1)):
            nuevo=""
            contador=0
    return mayor

def leer_vertical(sopa,dim,num):
    nuevo=""
    contador=(dim+1)
    mayor=num
    for a in range(dim):
        nuevo=""
        for x in sopa:
            if (contador==(dim+1)):
                nuevo=nuevo+x
                if (int(nuevo)%2 !=0 and int(nuevo)>int(mayor)):
                    mayor= int(nuevo)
                contador=0
            contador=(contador+1)
    return mayor

def encuentra_maximo(sopa):
    num=-1
    dim=extrae_dimension(sopa)
    num=leer_horizontal(sopa,dim,num)
    num=leer_vertical(sopa,dim,num)
    sopa_nueva=sopa
    sopa_nueva=reversed(sopa_nueva)
    num=leer_horizontal(sopa_nueva,dim,num)
    num=leer_vertical(sopa_nueva,dim,num)
    return num
