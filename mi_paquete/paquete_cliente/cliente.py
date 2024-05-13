class Cliente:
    def __init__(self, nombre, apellido, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada a: {self.direccion}")

    def enviar_correo_promocional(self):
        print(f"Se ha enviado un correo promocional a {self.correo}.")
