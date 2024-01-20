import os
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
                    fecha_vencimiento = lineas[2].strip()
                    completada = lineas[3].strip() == 'True'
                    tarea = Tarea(nombre, descripcion, fecha_vencimiento, completada)
                    self.tareas.append(tarea)
        except FileNotFoundError:
            pass

    def guardar_tarea(self, tarea):
        ruta_archivo = os.path.join(self.carpeta_book, f"{tarea.nombre}.md")
        with open(ruta_archivo, 'w') as f:
            f.write(f"{tarea.nombre}\n")
            f.write(f"{tarea.descripcion}\n\n")
            f.write(f"Fecha de vencimiento: {tarea.fecha_vencimiento}\n")
            f.write(f"Completada: {tarea.completada}\n")

    def agregar_tarea(self, nombre, descripcion, fecha_vencimiento):
        nueva_tarea = Tarea(nombre, descripcion, fecha_vencimiento)
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

if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.cargar_tareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Ver Todas las Tareas")
        print("3. Marcar Tarea como Completada")
        print("4. Eliminar Tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            fecha_vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ")
            gestor.agregar_tarea(nombre, descripcion, fecha_vencimiento)
        elif opcion == '2':
            print("\n--- Todas las Tareas ---")
            gestor.ver_todas_tareas()
        elif opcion == '3':
            nombre_tarea = input("Nombre de la tarea a marcar como completada: ")
            gestor.marcar_como_completada(nombre_tarea)
        elif opcion == '4':
            nombre_tarea = input("Nombre de la tarea a eliminar: ")
            gestor.eliminar_tarea(nombre_tarea)
        elif opcion == '5':
            print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
