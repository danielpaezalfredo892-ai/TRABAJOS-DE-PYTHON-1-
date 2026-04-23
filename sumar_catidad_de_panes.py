#sumar cantidad de panes que salen cada mañana 

total_panes = 0
bandejas = 6

# El bucle sera repetido exactamente 6 veces, ya que sabemos el numero de bandejas que se producen cada mañana
for i in range(bandejas):
    # i representa el número de bandeja actual (empezando desde 0)
    print(f"Bandeja número {i + 1}:")
    panes = int(input("¿Cuántos panes salieron en esta bandeja?: "))
    total_panes += panes

print("-" * 30)
print(f"La producción total de las {bandejas} bandejas es: {total_panes} panes.")