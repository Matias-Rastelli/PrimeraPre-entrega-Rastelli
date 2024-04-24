

def registrar_usuario(usuarios):
    usuario = input("\nIngrese el nombre de usuario (entre 4 y 15 caracteres): ")
    if not usuario.isalnum():
        print("\n>>> El nombre de usuario solo puede contener letras y números.")
        return
    if len(usuario) < 4 or len(usuario) > 15:
        print("\n>>> El nombre de usuario debe tener entre 4 y 15 caracteres.")
        return
    if usuario in usuarios:
        print("\n>>> Este usuario ya está registrado.")
    else:
        contraseña = input("\n>>> Ingrese la contraseña (entre 6 y 15 caracteres): ")
        if len(contraseña) < 6 or len(contraseña) > 15:
            print("\n>>> La contraseña debe tener entre 6 y 15 caracteres.")
            return
        usuarios[usuario] = contraseña
        print("\n>>> Usuario registrado con éxito.")

def mostrar_usuarios(usuarios):
    if usuarios:
        print("\n>>> Lista de usuarios registrados:")
        for usuario in usuarios:
            print( f" - {usuario}" )
    else:
        print("\n>>> No hay usuarios registrados.")

def login_usuario(usuarios):
    usuario = input("\n>>> Ingrese su nombre de usuario para iniciar sesión: ")
    if usuario in usuarios:
        contraseña = input("\n>>> Ingrese su contraseña: ")
        if contraseña == usuarios[usuario]:
            print("\n>>> Inicio de sesión exitoso.")
        else:
            print("\n>>> Contraseña incorrecta.")
    else:
        print("\n>>> El usuario no existe.")

def main():
    usuarios = {}

    while True:
        print("\nMenú:")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("\n>>> Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            mostrar_usuarios(usuarios)
        elif opcion == '3':
            login_usuario(usuarios)
        elif opcion == '4':
            print("\n>>> Saliendo del programa...")
            break
        else:
            print("\n>>> Opción no válida. Por favor, intente de nuevo.")

main()
