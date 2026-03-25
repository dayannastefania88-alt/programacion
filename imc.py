#IMPORTAR LA LIBRERIA PARA CREAR LA INTERFAZ
import tkinter as tk 
from tkinter import messagebox
#definir la funcion
def calcularImc():
    try:
        peso=float(entry_peso.get()) #ingresar valores decimales
        altura=float(entry_altura.get())
        if altura <=0 or peso <=0:
            messagebox.showerror("Error" , "Valores Invalidos")
            #return para calcular imc
            return
        imc = peso / (altura**2) #formula imc 
        #clasificar el imc
        if imc <18.5:
            estado="Peso Bajo"
        elif imc >=18.5 and imc <24.9:
            estado="Peso normal"
        elif imc >=25 and imc <29.9:
            estado="Sobrepeso"
        else:
            estado="Obesidad"
            #mostrar resultado
        resultado.set(f"IMC : {imc:.2f}\n Estado{estado}")
    except ValueError:
        messagebox.showerror("Erro","Ingrese numeros validos" )
        #ventana
ventana=tk.Tk() #CREAR LA VENTANA
ventana.title("Calculadora IMC")
ventana.geometry("300x300")
ventana.config(bg="plum")
#elemtos que iran en la ventana
tk.Label(ventana,text="Calculadora imc",bg="plum",font=("arial",14,"bold"),fg="black").pack()
#label y la cjaa de texto para el peso
tk.Label(ventana,text="Peso(kg)",bg="plum",font=("arial",14,"bold"),fg="black").pack()
entry_peso=tk.Entry(ventana)
entry_peso.pack()
#label y la caja de texto para la altura 
tk.Label(ventana,text="Altura(m)",bg="plum",font=("arial",14,"bold"),fg="black").pack()
entry_altura=tk.Entry(ventana)
entry_altura.pack()
#boton
tk.Button(ventana,text="Calcular",command=calcularImc,bg="purple",font=("arial",16,"bold"),fg="White").pack()
#label para el resultado
resultado=tk.StringVar()
tk.Label(ventana,textvariable=resultado,bg="plum",font=("arial",14,"bold"),fg="black").pack()
ventana.mainloop()