#importar la libreri que permite crerar la interfaz
import tkinter as tk
#importando libreria para mostarr un mensaje de error
from tkinter import messagebox
#definir la funcion 
def calcular ():
    try:
        comida=float(entry_comida.get())
        transporte=float(entry_transporte.get())
        otros=float(entry_otros.get())
        #la suma
        total = comida+transporte+otros
        #evaluar los gastos usando condicion if 
        if total >300:
            estado="Gastos Altos"
        else:
            estado="Gastos Controlados"
            #mostrar el resultado 
        resultado.set(f"Total: ${total}\n Estado {estado}")
    except ValueError:
        messagebox.showerror("Error","Valores invalidos")
    #ventana
ventana=tk.Tk() #crear la ventana
ventana.title("Calculadora de gastos personales")
ventana.geometry("350x350")
ventana.config(bg="pink")
#label con el titulo
tk.Label(ventana,text="Gastos mensuales",bg="pink",font=("arial",16,"bold"),fg="black").pack()
#labels de las variables y la caja para ingesar el dato
tk.Label(ventana,text="Comida",bg="pink",font=("arial",16,"bold"),fg="black").pack()
entry_comida=tk.Entry(ventana,bg="lavenderblush")
entry_comida.pack()
tk.Label(ventana,text="transporte",bg="pink",font=("arial",16,"bold"),fg="black").pack()
entry_transporte=tk.Entry(ventana,bg="lavenderblush")
entry_transporte.pack()
tk.Label(ventana,text="otros",bg="pink",font=("arial",16,"bold"),fg="black").pack()
entry_otros=tk.Entry(ventana,bg="lavenderblush")
entry_otros.pack()
#boton calcular
tk.Button(ventana,text="Calcular",command=calcular,bg="hot pink",font=("arial",12,"bold"),fg="white").pack()
#label para mostrar resultado
resultado=tk.StringVar()
tk.Label(ventana,textvariable=resultado , bg="lemon chiffon",font=("arial",12,"bold"),fg="black").pack()
ventana.mainloop()
