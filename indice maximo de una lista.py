def maximo(list):
    max=list[0]
    for elem in list:
        if(max<elem):
            max=elem
    return max

def indiceDelMax(lista):
    pos=0
    for i in range(len(lista)):
        if(lista[i]>lista[pos]):
            pos=i
    return pos

l2=[3, 0, 8, 6, 0, 9, 1, 0, 6, 0]

m=maximo(l2)
print("el maximo de la lista",l2,"es",m)
p=indiceDelMax(l2)
print("el indice del maximo de la lista es",p)