type TipoNivel = "junior" | "semi_senior" | "senior";
interface LiquidacionNomina {
  empleado: string;
  horasTrabajadas: number;
  horasExtra: number;
  nivel: TipoNivel;
}
const SALARIOS_BASE: Record<TipoNivel, number> = {
  junior:      500.00,   
  semi_senior: 1000.00,
  senior:      2000.00,
};
const COSTO_HORA_EXTRA = 15.00;  
const BONO_ASISTENCIA = 50.00;
function calcularNomina(nomina: LiquidacionNomina): string {
  const salarioBase = SALARIOS_BASE[nomina.nivel];
  const costoHorasExtra = nomina.horasExtra * COSTO_HORA_EXTRA;
  const bono = nomina.horasTrabajadas >= 160 ? BONO_ASISTENCIA : 0;
  const total = salarioBase + costoHorasExtra + bono;
  return `
💼 Liquidación de Nómina
   Empleado    : ${nomina.empleado}
   Nivel       : ${nomina.nivel}
   Salario Base: $${salarioBase.toFixed(2)}
   Horas Extra : $${costoHorasExtra.toFixed(2)}
   Bono Asist. : $${bono.toFixed(2)}
   ─────────────────────────
   TOTAL       : $${total.toFixed(2)}
  `.trim();
}
const empleado1: LiquidacionNomina = {
  empleado: "María López",
  horasTrabajadas: 160,
  horasExtra: 0,
  nivel: "junior",
};
const empleado2: LiquidacionNomina = {
  empleado: "Carlos Pérez",
  horasTrabajadas: 180,
  horasExtra: 10,
  nivel: "senior",
};
console.log(calcularNomina(empleado1));
console.log("---");
console.log(calcularNomina(empleado2));
