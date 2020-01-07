clave=input("Ingrese la clave")

hay_num=False
hay_may=False
hay_min=False

largo=len(clave)>=6

for letra in clave:
    if("a"<= letra and letra <= "z"):
        hay_min=True
    if("A" <= letra and letra <="Z"):
        hay_may=True
    if("0"<= letra and letra <= "9"):
        hay_num=True

if(largo and hay_min and hay_may and hay_num):
    print ("la clave", clave, "ES VALIDA")
else:
    print ("la clave", clave, "NO ES VALIDA")