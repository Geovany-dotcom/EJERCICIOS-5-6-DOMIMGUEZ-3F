import tkinter as tk
from tkinter import messagebox

class TorresDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.movimientos = []
    
    def mover_disco(self, n, origen, destino, auxiliar):
        if n == 1:
            self.movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        else:
            # Mover los n-1 discos de origen a auxiliar
            self.mover_disco(n - 1, origen, auxiliar, destino)
            # Mover el disco n de origen a destino
            self.movimientos.append(f"Mover disco {n} de {origen} a {destino}")
            # Mover los n-1 discos de auxiliar a destino
            self.mover_disco(n - 1, auxiliar, destino, origen)

    def resolver(self):
        self.movimientos.clear()
        self.mover_disco(self.num_discos, 'Origen', 'Destino', 'Auxiliar')
        return self.movimientos


class InterfazHanoi:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Torres de Hanói")
        self.ventana.geometry("400x400")
        
        # Etiqueta para el número de discos
        self.label_num_discos = tk.Label(self.ventana, text="Número de discos:")
        self.label_num_discos.pack(pady=10)

        # Campo de entrada para el número de discos
        self.entry_num_discos = tk.Entry(self.ventana)
        self.entry_num_discos.pack(pady=10)

        # Botón para iniciar el juego
        self.boton_iniciar = tk.Button(self.ventana, text="Resolver", command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=10)

        # Área para mostrar los movimientos
        self.text_area = tk.Text(self.ventana, height=15, width=40)
        self.text_area.pack(pady=10)

    def iniciar_juego(self):
        try:
            num_discos = int(self.entry_num_discos.get())
            if num_discos <= 0:
                raise ValueError("El número de discos debe ser positivo.")
            
            # Crear una instancia de TorresDeHanoi
            hanoi = TorresDeHanoi(num_discos)
            movimientos = hanoi.resolver()

            # Limpiar el área de texto
            self.text_area.delete(1.0, tk.END)
            
            # Mostrar los movimientos en el área de texto
            for movimiento in movimientos:
                self.text_area.insert(tk.END, movimiento + "\n")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido de discos.")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazHanoi(ventana)
    ventana.mainloop()
