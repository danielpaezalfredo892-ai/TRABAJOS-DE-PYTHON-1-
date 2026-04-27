#PROYECO DE REGISTRO DE ESTUDIANTES Y NOTAS
# 1. Entrada inicial
n = int(input("¿Cuántos estudiantes hay en el grupo?: "))

nombres = []
notas = []

# 2. Registro de estudiantes
for i in range(n):
    print(f"\n--- Estudiante {i + 1} ---")
    nombres.append(input("Nombre: "))
    notas.append(float(input("Nota: ")))

# 3. Procesamiento y Reporte
print("\n" + "="*30)
print("REPORTE FINAL")
print("="*30)

suma_notas = 0
aprobados = 0
reprobados = 0

for i in range(n):
    estado = "APROBADO" if notas[i] >= 3.0 else "REPROBADO"
    
    if estado == "APROBADO":
        aprobados += 1
    else:
        reprobados += 1
        
    suma_notas += notas[i]
    print(f"Estudiante: {nombres[i]} | Nota: {notas[i]} | Estado: {estado}")

# 4. Cálculos finales
promedio = suma_notas / n
print("-"*30)
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Total Aprobados: {aprobados}")
print(f"Total Reprobados: {reprobados}")

# 5. RETO BONUS: Búsqueda
print("\n" + "="*30)
busqueda = input("Ingrese el nombre a buscar: ")

if busqueda in nombres:
    indice = nombres.index(busqueda)
    print(f"La nota de {busqueda} es: {notas[indice]}")
else:
    print("Estudiante no encontrado.")