#Calculadora basica con funciones "+-*/"
#Definir las funciones y lo que va a retronar
def suma (a,b):
    return a+b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a*b
def division (a,b):
    return a/b
#Muestre el menu de ocpiones 
print("**Calculadora basica** ")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
opcion=int(input("Escoga un opcion del menu: "))
if opcion in (1,2,3,4):
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo  numero: ")) #se usa para ingresar valores 
    if opcion ==1:
        print("Resultado:",suma(num1,num2))
    elif opcion == 2:
        print("Resultado:",resta(num1,num2))
    elif opcion ==3:
        print("Resultado:",multiplicacion(num1,num2))
    elif opcion==4:
        print("Resultado:",division(num1,num2))
else :
    print("Opcion invalida intente de nuevo ")