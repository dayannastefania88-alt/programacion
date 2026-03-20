#pida un numero ty se calcule la suma acvumulada desde el 1 
num=int(input("Ingrese un numero: ")) #para pedir el numero por teclado 
suma=0
#para la suma 
for i in range (1,num,+1):
    suma +=i
    print("la suma es ", suma )
