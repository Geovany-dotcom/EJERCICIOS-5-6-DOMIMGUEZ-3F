import tkinter as tk
from tkinter import messagebox

# Definimos la clase que manejará la lógica del cálculo de cambio
class CalculadoraCambio:
    def __init__(self):
        self.monedas = [100, 50, 20, 10, 5, 1, 0.50, 0.20, 0.01]
    
    def calcular(self, total_compra, cantidad_pagada):
        try:
            # Calcular el cambio total
            cambio = round(cantidad_pagada - total_compra, 2)
            if cambio < 0:
                raise ValueError("El pago es menor que el total de la compra.")
            
            # Desglose de monedas
            resultado = {}
            for moneda in self.monedas:
                cantidad_monedas = int(cambio // moneda)
                cambio = round(cambio - cantidad_monedas * moneda, 2)
                resultado[moneda] = cantidad_monedas
            
            return resultado
        except Exception as e:
            return str(e)

# Definimos la clase que manejará la interfaz gráfica con Tkinter
class InterfazCambio:
    def __init__(self, ventana):
        self.calculadora = CalculadoraCambio()  # Instanciamos la lógica del cálculo
        
        # Configuramos la ventana principal
        self.ventana = ventana
        self.ventana.title("Calculadora de Cambio")
        self.ventana.geometry("400x400")
        
        # Etiquetas y campos de entrada
        self.label_total = tk.Label(self.ventana, text="Total de la compra:")
        self.label_total.pack()

        self.entry_total = tk.Entry(self.ventana)
        self.entry_total.pack()

        self.label_pago = tk.Label(self.ventana, text="Cantidad pagada:")
        self.label_pago.pack()

        self.entry_pago = tk.Entry(self.ventana)
        self.entry_pago.pack()

        # Botón para calcular el cambio
        self.boton_calcular = tk.Button(self.ventana, text="Calcular Cambio", command=self.mostrar_cambio)
        self.boton_calcular.pack()

        # Etiqueta para mostrar el resultado
        self.label_result = tk.Label(self.ventana, text="", justify="left")
        self.label_result.pack()
    
    def mostrar_cambio(self):
        try:
            # Obtener los valores ingresados por el usuario
            total_compra = float(self.entry_total.get())
            cantidad_pagada = float(self.entry_pago.get())
            
            # Llamamos a la calculadora para obtener el resultado
            resultado = self.calculadora.calcular(total_compra, cantidad_pagada)
            
            # Si el resultado es un error, mostramos un mensaje de error
            if isinstance(resultado, str):
                messagebox.showerror("Error", resultado)
            else:
                # Mostramos el desglose del cambio
                resultado_text = "Cambio a devolver:\n"
                for moneda, cantidad in resultado.items():
                    resultado_text += f"{cantidad} monedas de {moneda} pesos\n"
                self.label_result.config(text=resultado_text)
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Ejecutamos la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazCambio(ventana)
    ventana.mainloop()
