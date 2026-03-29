#impotar las librerias
import tkinter  as tk #crear la interfaz e usuario
from tkinter import messagebox #nos permite mostar mensaje de error 
#definir funciones
# Es un bloque de codigo que permite ejecutar tarea o programa en especifico
def calcular ():
    try:
        #variable el tipo de dato y  la funcion get para que guarde los datos que sean ingresados por caja texto 
        n1=float(num1.get())
        n2=float(num2.get())
        #operador matematico + - * /
        total = n1+n2   
        #condicion if nos sirve para tomar desiciones y si la condicion se cumple el programa se ejecuta y caso contrario usamos else:
        if total >10:
            resultado.set(f"Total : {total} Es mayor a 10")
        else:
             resultado.set(f"Total : {total} Es menor o igual  a 10")
    except ValueError:
        messagebox.showerror("Error","Ingrese valores Validos") #para mosrtar mensaje d e error 
        #crear la ventana 
ventana=tk.Tk() #crear la ventana
ventana.geometry("300x300")
ventana.title("Ejemplo")
#elementos widgets que iran en la ve¿entana 
#label
#caja de texto para ingresar datos 
#botones
#crear el label "Ingrese el primer numero"
tk.Label(ventana,text="Ingrese el primer numero").pack()
#cja de texto 
num1=tk.Entry(ventana)
num1.pack()
tk.Label(ventana,text="Ingrese el psegundo numero  numero").pack()
num2=tk.Entry(ventana)
num2.pack()
#boton para calcular 
tk.Button(ventana,text="Calcular",command=calcular).pack()
#label que muestre el resultado
resultado=tk.StringVar()
tk.Label(ventana,textvariable=resultado).pack()
#ventana s eejecute y se mantenga abierta 
ventana.mainloop()
