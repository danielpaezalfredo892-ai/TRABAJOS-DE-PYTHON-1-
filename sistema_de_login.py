#================================================
import time

while True:
  #SISTEMA DE LOGIN – Clase 7
# Módulo 8 – Fundamentos de Programación en Python
# Integración: variables + condiciones + ciclos + try/except
# ================================================
    
    print('=' * 45)
    print('          SISTEMA DE ACCESO SEGURO')
    print('=' * 45)

    # Credenciales válidas
    USUARIO_CORRECTO = 'admin'
    CONTRASENA_CORRECTA = 'python123'
    INTENTOS_MAX = 3

    # Variables de control
    intentos = 0
    acceso = False

    # Ciclo principal
    while intentos < INTENTOS_MAX and not acceso:
        intentos += 1
        print(f'\nIntento {intentos} de {INTENTOS_MAX}')
        print('-' * 30)

        try:
            usuario_ing = input('Usuario    : ').strip()
            contrasena_ing = input('Contraseña : ').strip()

            if usuario_ing == USUARIO_CORRECTO:
                if contrasena_ing == CONTRASENA_CORRECTA:
                    acceso = True
                    print('\n✅ ACCESO PERFECTO ¡Bienvenido!')
                else:
                    print('❌ Contraseña no valida.')
                    time.sleep(3)
            else:
                print('❌ Usuario no encontrado en la base de datos.')
                time.sleep(3)
        except Exception as e:
            print(f'⚠️ Error inesperado: {e}')

    # Resultado final
    print('\n' + '=' * 45)
    if not acceso:
        print('🔒 CUENTA BLOQUEADA')
        print('  Se superó el número máximo de intentos.')
        print(f"  intentos totales realizados: {intentos}.")
        print('  Contacte al administrador del sistema.')
    
    # Pregunta para volver a usar el programa
    respuesta = input("\n¿Deseas volver a intentar? (s/n): ").lower()
    if respuesta != 's':
        print("Saliendo... ¡Hasta luego!")
        break # Esto termina el while True

    