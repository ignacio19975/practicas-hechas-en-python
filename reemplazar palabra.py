pal=input("Ingrese la palabra")
le=input("Ingresde letra a reemplazar")
while(len(le)!=1):
    le=input("Ingresde letra a reemplazar")
nueva=""

for letra in pal:
    if le.upper()==letra.upper():
        nueva=nueva+"*"
    else:
        nueva=nueva+letra

print(nueva)