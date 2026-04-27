# Inicialización de listas
estudiantes = []
notas_finales = []
porcentaje_asistencia = []

print("--- Registro Académico 'Iteandes PRO' ---")
print("Escriba 'SALIR' en el nombre para terminar el registro.\n")

# 1. Ciclo while para entrada continua de datos
while True:
    nombre = input("Ingrese nombre del alumno (o 'SALIR'): ")
    if nombre.upper() == "SALIR":
        break
    
    # 2. Manejo de errores con try/except
    try:
        nota = float(input(f"Ingrese nota final para {nombre}: "))
        asistencia = int(input(f"Ingrese porcentaje de asistencia para {nombre}: "))
        
        # Guardar en listas
        estudiantes.append(nombre)
        notas_finales.append(nota)
        porcentaje_asistencia.append(asistencia)
        print("Datos registrados correctamente.\n")
        
    except ValueError:
        print("Error: Por favor, ingrese un número válido para nota y asistencia.\n")
        continue

# 3. Procesamiento con ciclo for y condicionales
print("\n--- REPORTE FINAL ---")
suma_notas = 0

for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota = notas_finales[i]
    asistencia = porcentaje_asistencia[i]
    
    suma_notas += nota
    
    # Condicionales y Operadores Lógicos7

    if nota >= 3.5 and asistencia >= 80:
        estado = "APROBADO"
    elif nota >= 3.0 and nota < 3.5:
        estado = "HABILITA"
    else:
        estado = "REPROBADO"
        
    print(f"Estudiante: {nombre} | Nota: {nota} | Asistencia: {asistencia}% | Estado: {estado}")

# Cálculo del promedio general
if len(notas_finales) > 0:
    promedio_general = suma_notas / len(notas_finales)
    print(f"\nEl promedio general del salón es: {promedio_general:.2f}")
else:
    print("\nNo se registraron estudiantes.")