from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def cargar_tareas(self):
        try:
            with open('tareas.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    detalles = linea.strip().split(', ')
                    tarea = Tarea(detalles[0], detalles[1], detalles[2], detalles[3] == 'True')
                    self.tareas.append(tarea)
        except FileNotFoundError:
            pass

    def guardar_tareas(self):
        with open('tareas.txt', 'w') as archivo:
            for tarea in self.tareas:
                archivo.write(f"{tarea.nombre}, {tarea.descripcion}, {tarea.fecha_vencimiento}, {tarea.completada}\n")

    def agregar_tarea(self, nombre, descripcion, fecha_vencimiento):
        nueva_tarea = Tarea(nombre, descripcion, fecha_vencimiento)
        self.tareas.append(nueva_tarea)
        self.guardar_tareas()
        print(f"Tarea '{nombre}' agregada correctamente.")

    def ver_todas_tareas(self):
        for tarea in self.tareas:
            tarea.mostrar_tarea()

    def marcar_como_completada(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                tarea.completada = True
                self.guardar_tareas()
                print(f"Tarea '{nombre_tarea}' marcada como completada.")

    def eliminar_tarea(self, nombre_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre_tarea]
        self.guardar_tareas()
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
