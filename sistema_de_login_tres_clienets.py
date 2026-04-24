#sistema de login con tres clientes, cada uno con un rol diferente (administrador, usuario, invitado)

def sistema_login():
    # 1. Definición de usuarios (variables separadas)
    user1, pass1, rol1 = "admin", "1234", "administrador"
    user2, pass2, rol2 = "user", "abcd", "usuario"
    user3, pass3, rol3 = "invitado", "0000", "invitado"

    try:
        # 4. Uso de try/except en la entrada de datos
        print("--- INGRESO AL SISTEMA ---")
        u_ingresado = input("Usuario: ")
        p_ingresado = input("Contraseña: ")

        # 2. Lógica de validación y roles
        if u_ingresado == user1 and p_ingresado == pass1:
            mostrar_menu(rol1)
        elif u_ingresado == user2 and p_ingresado == pass2:
            mostrar_menu(rol2)
        elif u_ingresado == user3 and p_ingresado == pass3:
            mostrar_menu(rol3)
        else:
            print("Usuario o contraseña incorrectos.")

    except EOFError:
        print("\nError: Entrada finalizada inesperadamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# 3. Función para mostrar el menú correspondiente al rol
def mostrar_menu(rol):
    print(f"\nBienvenido. Tu rol es: {rol}")
    print("--- MENÚ ---")
    
    if rol == 'administrador':
        print("1. Gestionar usuarios\n2. Ver logs\n3. Configuración total")
    elif rol == 'usuario':
        print("1. Ver archivos\n2. Editar perfil")
    elif rol == 'invitado':
        print("1. Visualizar contenido")

# Ejecutar el sistema
sistema_login()