# Sistema para el Supermercado "La Economía"

continuar = 'S'

while continuar.upper() == 'S':
    print("\n--- Nuevo Cliente ---")
    
    # Entrada de datos: número de productos
    try:
        num_productos = int(input("¿Cuántos productos lleva en el carrito? "))
        if num_productos < 0:
            num_productos = 0
    except ValueError:
        num_productos = 0
        print("Entrada inválida. Se tomará como 0 productos.")

    total_carrito = 0
    precio_maximo = 0
    
    # Ciclo de productos (for)
    for i in range(1, num_productos + 1):
        try:
            precio = float(input(f"Ingrese el precio del producto {i}: "))
            
            # Validación de precio
            if precio < 0:
                print("¡Error! Precio negativo. Se asignará valor $0.")
                precio = 0
        except ValueError:
            print("¡Error! Entrada no válida. Se asignará valor $0.")
            precio = 0
            
        # Cálculos acumulados
        total_carrito += precio
        if precio > precio_maximo:
            precio_maximo = precio

    # Cálculos finales por cliente
    if num_productos > 0:
        promedio = total_carrito / num_productos
    else:
        promedio = 0

    # Mostrar resultados
    print("\n--- Resumen del Cliente ---")
    print(f"Total a pagar: ${total_carrito:.2f}")
    print(f"Producto más caro: ${precio_maximo:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")
    print("-" * 25)

    # Preguntar si continuar
    continuar = input("¿Desea registrar la compra de otro cliente? (S/N): ")

print("\nCaja cerrada. ¡Hasta mañana!")