# Ejercicio: Suma de Ventas

total_ventas = 0
# Pedimos el primer monto antes de entrar al bucle
monto = float(input("Ingrese monto de venta (0 para terminar): "))

# El bucle solo ocurre SI monto es diferente de 0
while monto != 0:
    total_ventas += monto
    monto = float(input("Ingrese monto de venta (0 para terminar): "))

print(f"El total de ventas es: ${total_ventas:.2f}")