lista=[]
l=0
while l==0:
    x=int(input("ingrese el termino a agregar"))
    lista.append(x)
    print("usted ingreso",len(lista),"terminos")
    c=lista.count(4)
    print(c)
    if c>2:
        lista.remove(4)
    if x==" ":
        lista.remove(" ")
    print(lista)

