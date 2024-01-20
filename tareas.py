class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento, completada=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = completada

    def mostrar_tarea(self):
        estado = "Completada" if self.completada else "Pendiente"
        print(f"{self.nombre} ({estado}): {self.descripcion}, Vence el {self.fecha_vencimiento}")
