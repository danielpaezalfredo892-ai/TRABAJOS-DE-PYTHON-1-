# Entrada de datos

nombre_producto = input("Ingrese el nombre del producto: ")
precio_base = float(input(f"Ingrese el precio de '{nombre_producto}': "))

# Inicialización de variables

categoria = ""
descuento_porcentaje = 0

# Lógica de categorización y asignación de descuento

if precio_base <= 10000:
    categoria = "Económico"
    descuento_porcentaje = 0
elif 10001 <= precio_base <= 50000:
    categoria = "Estándar"
    descuento_porcentaje = 0.05
elif 50001 <= precio_base <= 200000:
    categoria = "Premium"
    descuento_porcentaje = 0.10
else:
    categoria = "Lujo"
    descuento_porcentaje = 0.15

# Cálculos finales

monto_descuento = precio_base * descuento_porcentaje
precio_final = precio_base - monto_descuento

# Salida de resultados

print("-" * 30)
print(f"Resumen de Clasificación:")
print(f"Producto: {nombre_producto}")
print(f"Categoría: {categoria}")
print(f"Descuento aplicado: {descuento_porcentaje * 100}% (${monto_descuento:,.2f})")
print(f"Precio final a pagar: ${precio_final:,.2f}")
print("-" * 30)