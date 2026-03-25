import tkinter as tk
from tkinter import messagebox

# Función para calcular el IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        if altura <= 0 or peso <= 0:
            messagebox.showerror("Error", "Valores inválidos")
            return

        imc = peso / (altura ** 2)

        # Clasificación del IMC
        if imc < 18.5:
            estado = "Bajo peso"
        elif imc < 24.9:
            estado = "Peso normal"
        elif imc < 29.9:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        resultado.set(f"IMC: {imc:.2f}\nEstado: {estado}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora IMC")
ventana.geometry("300x300")
ventana.config(bg="pink")  # rosado bonito 💖

# Título
tk.Label(ventana, text="Calculadora IMC", bg="pink",
         font=("Arial", 16, "bold")).pack(pady=10)

# Peso
tk.Label(ventana, text="Peso (kg):", bg="pink").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

# Altura
tk.Label(ventana, text="Altura (m):", bg="pink").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

# Botón
tk.Button(ventana, text="Calcular", command=calcular_imc,
          bg="#ff99cc").pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, bg="#ffe4ec",
         font=("Arial", 12)).pack()

ventana.mainloop()