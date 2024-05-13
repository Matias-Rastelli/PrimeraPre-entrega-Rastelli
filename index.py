# En este archivo se hace importacion de la clase y se usa para comprobar su funcionamiento.


from mi_paquete.paquete_cliente.cliente import Cliente

cliente1 = Cliente("Matias", "Rastelli", "matias@rastelli.com", "Calle falsa 123")
print(cliente1)
print(cliente1.nombre)
print(cliente1.apellido)
cliente1.actualizar_direccion("Avenida siempre viva")
cliente1.enviar_correo_promocional()
print(cliente1.direccion)