print("Análisis de desempeño")
salario_actual = float(input("Salario mensual (USD): "))
evaluacion = input("¿Evaluación anual aprobada? (s/n): ")
antiguedad_años = int(input("Años en la empresa: "))

if (salario_actual >= 1000 and evaluacion.lower() == 's') or (antiguedad_años >= 5):
    print("✓ Aplica para aumento por desempeño")
    aumento = salario_actual * 0.07
    print(f"Aumento sugerido: {aumento:.2f} USD")
else:
    print("✗ No aplica para aumento por ahora")
