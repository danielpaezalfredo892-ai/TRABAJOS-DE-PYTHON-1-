# ==========================================
# SISTEMA DE REGISTRO DE NOTAS 
# ==========================================

print('=' * 45)
print('      SISTEMA DE REGISTRO DE NOTAS')
print('=' * 45)

n = int(input('¿Cuántos estudiantes tiene el grupo? '))

total = 0
aprobados = 0
reprobados = 0

# --- NUEVAS VARIABLES ---
nota_alta = 0.0
nota_baja = 10.0
nota_perfecta_count = 0 

if n > 0:
    for i in range(1, n + 1):
        print(f'\n--- Estudiante {i} de {n} ---')
        nota_texto = input('Ingresa la nota (0 a 10): ')
        
        if not nota_texto.replace('.', '', 1).isdigit():
            print('Nota inválida. Se registra como 0.')
            nota = 0.0
        else:
            nota = float(nota_texto)
            if nota < 0 or nota > 10:
                print('Nota fuera de rango. Se registra como 0.')
                nota = 0.0
        
        # --- LÓGICA PARA LAS NUEVAS MÉTRICAS ---
        if nota > nota_alta:
            nota_alta = nota
        if nota < nota_baja:
            nota_baja = nota
        if nota == 10:
            nota_perfecta_count += 1
                
        total += nota
        
        if nota >= 6:
            aprobados += 1
            print(f'Nota {nota} -> APROBADO ✔')
        else:
            reprobados += 1
            print(f'Nota {nota} -> REPROBADO X')

    promedio = total / n

    print('\n' + '=' * 45)
    print('          RESULTADOS DEL GRUPO')
    print('=' * 45)
    print(f' Total de estudiantes      : {n}')
    print(f' Promedio del grupo        : {promedio:.2f}')
    print(f' Aprobados                 : {aprobados}')
    print(f' Reprobados                : {reprobados}')
    
    # --- MOSTRAR LOS NUEVOS RESULTADOS ---
    print(f' Nota más alta del grupo   : {nota_alta:.1f}')
    print(f' Nota más baja del grupo   : {nota_baja:.1f}')
    print(f' Estudiantes con nota 10   : {nota_perfecta_count}')

    if promedio >= 6:
        print('\n ✅ El grupo APROBÓ el período.')
    else:
        print('\n ❌ El grupo REPROBÓ el período.')
else:
    print("\nEl número de estudiantes debe ser mayor a 0.")

print('=' * 45)