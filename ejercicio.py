#ingresar un numero en este caso la edad del usuario
edad =int(input("Ingrese su edad:"))
#verificar si la edad ingresada es igual o mayor a 18 
if edad >=18:
    #si es mayor o igual a 18
    print("El usuario puede votar")
else:
    print("El usuario no puede votar")