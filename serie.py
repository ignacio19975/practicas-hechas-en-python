
S=0
n=int(input("cantidad de terminos"))

for i in range (1,n+1):
    S=S+1/i

print("la serie para",n,"terminos es:",S)