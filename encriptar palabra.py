def letra2numero(letra,abcd):
    for i in range(len(abcd)):
        if(letra == abcd[i]):
            return(i+1)

def palabra2numeros(cadena,abcd):
    lista = []
    for elem in cadena:
        lista.append(letra2numero(elem,abcd))
    return(lista)

def restoPalabras(listanum1,listanum2):
    lista = []
    for i in range(len(listanum1)):
        a = listanum1[i]-listanum2[i]
        if(a>0):
            lista.append(a)
        else:
            lista.append(a+26)
    return(lista)

def numero2palabra(lista,abcd):
    listaPalabra = []
    for i in range(len(lista)):
        listaPalabra.append(abcd[lista[i]-1])
    return(listaPalabra)

encriptada = "DIOSES"
clave = "BTBQDZ"
abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#encrNum = palabra2numeros(encriptada,abcd)
#claveNum = palabra2numeros(clave,abcd)
#otraLista = restoPalabras(encrNum,claveNum)
#textoOculto = numero2palabra(otraLista,abcd)
#print(textoOculto)
print(numero2palabra(restoPalabras(palabra2numeros(encriptada,abcd),
palabra2numeros(clave,abcd)),abcd))
