# sistemas de notas del estudiante

nota=float(input("ingresar nota del estudiante (0.0 - 5.0):"))
if nota < 0 or nota > 5:
    print("❌ Error: La nota debe estar entre 0.0 y 5.0")
elif nota >= 4.5:
    mensaje = "🏆 Excelente — Aprobado con distinción "
elif nota >= 3.0:
    mensaje = "✅ Aprobado"
elif nota >= 2.0:
    mensaje = "⚠️ Recuperación"
else:
    mensaje = "❌ Reprobado"
if 0 <= nota <= 5:
    print(f"Resultado final: {mensaje}")


 