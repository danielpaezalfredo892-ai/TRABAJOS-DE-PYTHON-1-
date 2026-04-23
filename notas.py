# Programa para calcular el promedio de notas de un grupo de estudiantes
print("=" * 45)
print(" PROMEDIO DE NOTAS DE UN GRUPO ")
print("=" * 45)


n = int(input("¿cuantos estudiantes tine el grupo: "))
#inicializar acumulaciones antes del ciclo 
total = 0
aprobados = 0
reprobados = 0
for i in range(1, n + 1):
    print(f"\n--- estudiante {i} de {n} ---")

#validar que la nota este en el rango
nota_texto = input("ingrese la nota (0 a 10):")

#verificar que el numero desimal sea valido 
if not nota_texto.replace(".", "", 1).isdigit():
    print("nota invalidad. se registra como 0.")
    nota = 0.0
else:
    nota = float(nota_texto)
    if nota < 0 or nota > 10:
        print("nota fuera de rango. se registra como 0.")
        nota = 0.0  

        #Acumulador 
total += nota
if nota >= 6:
    aprobados += 1
    print(f"nota: {nota} - Aprobado")
else:
    reprobados += 1
    print(f"nota: {nota} - Reprobado")
    promedio = total / n if n > 0 else 0.0
 #fuera del ciclo: aquì se muestran los resultados finales del grupo
print("\n" + "-" * 45)
print(" resultados del grupo ")
print("=" * 45)
print(f"total de estudiantes: {n}")
print(f" promedio del grupo : (promedio:.2f)")
print(f" aprobados  : {aprobados}")
print(f" reprobados : {reprobados}")

if aprobados > 6:
    print("\n EL GRUPO APROBO EL PERIODO")
else:
    print("\n EL GRUPO REPROBO EL PERIODO")
    print("-" * 45)