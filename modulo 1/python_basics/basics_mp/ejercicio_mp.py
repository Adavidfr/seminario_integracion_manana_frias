# Ejercicio: Sistema de gestión de nómina y ventas de cursos RR.HH.

total_nomina = 0.0
cursos_premium_vendidos = 0

while True:
    print("\n=== SISTEMA DE RR.HH. ===")
    print("1. Curso Básico")
    print("2. Curso Intermedio")
    print("3. Curso Premium")
    print("0. Finalizar")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 0:
        print("\nFinalizando operaciones...")
        break
    
    cantidad = int(input("Cantidad de empleados: "))
    certificado = input("¿Desea certificado? (si/no): ").lower() == "si"
    
    match opcion:
        case 1:
            subtotal = 50.0 * cantidad  # curso básico
        case 2:
            subtotal = 100.0 * cantidad  # curso intermedio
        case 3:
            subtotal = 200.0 * cantidad  # curso premium
            cursos_premium_vendidos += cantidad
        case _:
            continue
    
    # Descuento por volumen
    if subtotal > 500.0:
        subtotal = subtotal * 0.85
    
    # Certificado adicional
    if certificado:
        subtotal += 25.0
    
    total_nomina += subtotal

print(f"\n=== RESUMEN FINAL ===")
print(f"Total recaudado: ${total_nomina:.2f}")
print(f"Cursos Premium vendidos: {cursos_premium_vendidos}")
if cursos_premium_vendidos > 5:
    print("❤ ¡Excelente desempeño! Bonificación aplicada.")