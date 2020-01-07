def intercambiar(lista,n1,n2):
    aux=lista[n1]
    lista[n1]=lista[n2]
    lista[n2]=aux

s=["a","b","c","d","e","f","g"]
print("inicial   ",s)
a=2
b=5

intercambiar(s,a,b)
print("modificada",s)