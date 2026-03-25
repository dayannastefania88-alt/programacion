#impirtar la libreria para crea interfaz
import tkinter as tk 
#definir las funciones
def suma ():
    n1= float(entry1.get())
    n2= float(entry2.get()) #ingresar valores deicmales y enteros 
    resultado.config(text=f"Resultado : {n1+n2}")
def resta ():
    n1= float(entry1.get())
    n2= float(entry2.get()) #ingresar valores deicmales y enteros 
    resultado.config(text=f"Resultado : {n1-n2}")
def multiplicar ():
    n1= float(entry1.get())
    n2= float(entry2.get()) #ingresar valores deicmales y enteros 
    resultado.config(text=f"Resultado : {n1*n2}")
def dividir ():
    n1= float(entry1.get())
    n2= float(entry2.get()) #ingresar valores deicmales y enteros 
    resultado.config(text=f"Resultado : {n1/n2}")
#ventana
ventana=tk.Tk() #crear la ventana
ventana.geometry("300x300") #tamaño
ventana.title("Calculadora Basica") # titulo
#frame
frame=tk.Frame(ventana,bg="yellow")
frame.pack(fill="both",expand="true")
#labels para la entrada de numeros
tk.Label(frame,text="Ingrese el primer numero", bg="yellow").pack()
#caja para ingeeso del primer numero 
entry1=tk.Entry(frame)
entry1.pack()
tk.Label(frame,text="Ingrese el segundo numero", bg="yellow").pack()
entry2=tk.Entry(frame)
entry2.pack()
#botones
tk.Button(frame,text="Suma",command=suma , bg="orange3",fg="white").pack()
tk.Button(frame,text="Resta",command=resta , bg="orange3",fg="white").pack()
tk.Button(frame,text="Multiplicar",command=multiplicar , bg="orange3",fg="white").pack()
tk.Button(frame,text="Dividir",command=dividir , bg="orange3",fg="white").pack()
#label paramostrar resultado
resultado=tk.Label(frame,text="Resultado",bg="yellow",fg="black")
resultado.pack()
ventana.mainloop()