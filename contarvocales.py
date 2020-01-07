palabra=input ("Ingrese palabra")

n=0
for letra in palabra.lower() :
    if (letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
        n=n+1


print ("la palabra ",palabra, "tiene ", n, "vocales")