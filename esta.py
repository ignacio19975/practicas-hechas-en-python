palabra=input("Ingrese una palabra")

b=input ("Ingrese una letra")

print (palabra)
print (b)

cont=0
for letra in palabra:
    if (letra==b):
        cont+=1
print (b, "aparece en ",palabra, cont, "veces")