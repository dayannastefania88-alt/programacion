import tkinter as tk

lista = []

def agregarNotas():
    if entry.get() != "":
        nota = float(entry.get())
        entry.delete(0, "end")
        lista.append(nota)

        result.config(text=f"Notas: {lista}")
        result_promedio.config(text=f"Promedio: {promedio()}")

def promedio():
    if len(lista) == 0:
        return 0
    suma = 0
    for i in lista:
        suma += i
    return round(suma / len(lista), 2)

def estado():
    prom = promedio()
    if prom >= 6:
        estado_label.config(text="Aprobado ✅", fg="green")
    elif prom >= 4:
        estado_label.config(text="Recuperación ⚠️", fg="orange")
    else:
        estado_label.config(text="Reprobado ❌", fg="red")

# ventana
ventana = tk.Tk()
ventana.geometry("200x300")
ventana.title("Notas")
ventana.config(bg="pink")

frame = tk.Frame(ventana, bg="pink")
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Ingrese sus notas",
                 font=("Arial",12,"bold"),
                 bg="pink", fg="blue")
label.pack()

entry = tk.Entry(frame, bg="white")
entry.pack()

button = tk.Button(frame, text="Agregar", command=agregarNotas, bg="pink", fg="blue")
button.pack()
result = tk.Label(frame, text="", bg="pink")
result.pack()

result_promedio = tk.Label(frame, text="", bg="pink")
result_promedio.pack()

btn_estado = tk.Button(frame, text="Ver Estado", command=estado, bg="pink", fg="blue")
btn_estado.pack()

estado_label = tk.Label(frame, text="", bg="pink")
estado_label.pack()

ventana.mainloop()