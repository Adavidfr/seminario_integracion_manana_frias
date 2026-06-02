print("Match Case - Clasificar tipo de empleado")
tipo_empleado = input("Tipo de empleado (temporal/permanente/contratista): ")
match tipo_empleado:
    case "temporal":
        print("Beneficios: Básicos")
        contrato = "6 meses"
    case "permanente":
        print("Beneficios: Completos")
        contrato = "Indefinido"
    case "contratista":
        print("Beneficios: Servicios solo")
        contrato = "Por proyecto"
    case _:
        print(f"Tipo '{tipo_empleado}' no reconocido")
        contrato = "N/A"

print(f"Duración contrato: {contrato}")

print("\nMatch con condiciones - Clasificar salario")
salario = 1500
match salario:
    case s if s < 1000:
        print(f"Salario {s} es bajo")
        categoria = "Junior"
    case 1000 | 1500 | 2000:
        print(f"Salario {s} está en escala estándar")
        categoria = "Senior"
    case s if s > 3000:
        print(f"Salario {s} es alto")
        categoria = "Ejecutivo"
    case s:
        print(f"Salario {s} personalizado")
        categoria = "Especial"
