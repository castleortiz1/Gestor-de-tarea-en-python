import os
import tkinter as tk
from tkinter import messagebox
from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.carpeta_book = 'book'

        # Crear la carpeta 'book' si no existe
        if not os.path.exists(self.carpeta_book):
            os.makedirs(self.carpeta_book)

    def cargar_tareas(self):
        try:
            archivos = os.listdir(self.carpeta_book)
            for archivo in archivos:
                ruta_archivo = os.path.join(self.carpeta_book, archivo)
                with open(ruta_archivo, 'r') as f:
                    lineas = f.readlines()
                    nombre = lineas[0].strip()
                    descripcion = lineas[1].strip()
                    contenido = lineas[2].strip()
                    fecha_vencimiento = lineas[3].strip()
                    completada = lineas[4].strip() == 'True'
                    tarea = Tarea(nombre, descripcion, contenido, fecha_vencimiento, completada)
                    self.tareas.append(tarea)
        except FileNotFoundError:
            pass

    def guardar_tarea(self, tarea):
        ruta_archivo = os.path.join(self.carpeta_book, f"{tarea.nombre}.md")
        with open(ruta_archivo, 'w') as f:
            f.write(f"{tarea.nombre}\n")
            f.write(f"{tarea.descripcion}\n")
            f.write(f"{tarea.contenido}\n")
            f.write(f"Fecha de vencimiento: {tarea.fecha_vencimiento}\n")
            f.write(f"Completada: {tarea.completada}\n")

    def agregar_tarea(self, nombre, descripcion, contenido, fecha_vencimiento):
        nueva_tarea = Tarea(nombre, descripcion, contenido, fecha_vencimiento)
        self.tareas.append(nueva_tarea)
        self.guardar_tarea(nueva_tarea)
        print(f"Tarea '{nombre}' agregada correctamente.")

    def ver_todas_tareas(self):
        for tarea in self.tareas:
            tarea.mostrar_tarea()

    def marcar_como_completada(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                tarea.completada = True
                self.guardar_tarea(tarea)
                print(f"Tarea '{nombre_tarea}' marcada como completada.")

    def eliminar_tarea(self, nombre_tarea):
        ruta_archivo = os.path.join(self.carpeta_book, f"{nombre_tarea}.md")
        os.remove(ruta_archivo)
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre_tarea]
        print(f"Tarea '{nombre_tarea}' eliminada correctamente.")

    def mostrar_interfaz(self):
        root = tk.Tk()
        root.title("Gestor de Tareas")

        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        label = tk.Label(frame, text="Lista de Tareas")
        label.pack()

        lista_tareas = tk.Listbox(frame, selectmode=tk.SINGLE)
        for tarea in self.tareas:
            lista_tareas.insert(tk.END, tarea.nombre)
        lista_tareas.pack()

        def on_select(event):
            seleccion = lista_tareas.curselection()
            if seleccion:
                tarea_seleccionada = self.tareas[seleccion[0]]
                tarea_seleccionada.mostrar_tarea()

        lista_tareas.bind("<ButtonRelease-1>", on_select)

        def marcar_como_completada():
            seleccion = lista_tareas.curselection()
            if seleccion:
                nombre_tarea = self.tareas[seleccion[0]].nombre
                self.marcar_como_completada(nombre_tarea)
                lista_tareas.delete(seleccion[0])
                messagebox.showinfo("Tarea Completada", f"Tarea '{nombre_tarea}' marcada como completada.")

        boton_completada = tk.Button(frame, text="Marcar como Completada", command=marcar_como_completada)
        boton_completada.pack()

        root.mainloop()

if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.cargar_tareas()
    gestor.mostrar_interfaz()
