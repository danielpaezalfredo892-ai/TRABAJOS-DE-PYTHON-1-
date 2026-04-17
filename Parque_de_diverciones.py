# Entrada de datos

edad = int(input("Ingrese la edad del visitante: "))
dia = input("Ingrese el día de la semana: ").capitalize() # .capitalize() pone la primera en mayúscula

precio_base = 0

# 1. Determinamos el precio base según la edad

if edad < 3:
    precio_base = 0
    print("Entrada gratis.")
elif 3 <= edad <= 12:
    precio_base = 8000
elif 13 <= edad <= 60:
    precio_base = 15000
else:
    precio_base = 10000

# 2. Aplicamos la regla del Miércoles (solo si no es gratis)

if dia == "Miércoles" or dia == "Miercoles":
    if precio_base > 0:
        descuento = precio_base * 0.20
        precio_final = precio_base - descuento
        print(f"¡Hoy es {dia}! Se aplica un 20% de descuento.")
    else:
        precio_final = 0
else:
    precio_final = precio_base

# 3. Resultado final

print("-" * 30)
print(f"Precio final a pagar: ${precio_final:,.0f}")
print("-" * 30)
    