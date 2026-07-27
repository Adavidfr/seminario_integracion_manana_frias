import math

print("Cálculos de aumento salarial")
salario_actual = 1234.56
porcentaje_aumento = 0.075
nuevo_salario = salario_actual * (1 + porcentaje_aumento)
print(f"Salario con aumento {porcentaje_aumento*100}%: {nuevo_salario:.2f}")
print(f"Redondeado hacia arriba: {math.ceil(nuevo_salario)}")
print(f"Redondeado hacia abajo: {math.floor(nuevo_salario)}")
print(f"Redondeado normal: {round(nuevo_salario, 2)}")
print(f"Valor absoluto: {abs(-1500)}")
print(f"Máximo: {max(1200, 1500, 1100)}")
print(f"Mínimo: {min(1200, 1500, 1100)}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Potencia 2^8: {2**8}")
