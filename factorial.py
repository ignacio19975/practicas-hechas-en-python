n=int (input("Ingresa el numero al que desea calcularle su factorial"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print ("El factorial de ",n,"es: ",factorial)