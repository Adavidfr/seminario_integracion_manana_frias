print("Evaluación de elegibilidad para beneficios")
edad = int(input("Edad del empleado: "))
antiguedad = int(input("Años en la empresa: "))

if edad >= 18 and antiguedad >= 1:
    print("✓ Elegible para beneficios básicos")
elif edad >= 18 and antiguedad < 1:
    print("• Espere 1 año para beneficios")
else:
    print("✗ No cumple requisitos de edad"
