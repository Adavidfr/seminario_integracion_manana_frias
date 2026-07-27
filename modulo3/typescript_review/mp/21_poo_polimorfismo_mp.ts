class ContratoLaboral {
  tipo(): string { return "Contrato Genérico"; }
  horasSemanalesMax(): number { return 0; }
}
class ContratoTiempoParcial extends ContratoLaboral {
  constructor(private horasPactadas: number) { super(); }
  override tipo(): string { return "Tiempo Parcial"; }
  override horasSemanalesMax(): number { return this.horasPactadas + 5; } 
}
class ContratoTiempoCompleto extends ContratoLaboral {
  constructor(private horasPactadas: number) { super(); }
  override tipo(): string { return "Tiempo Completo"; }
  override horasSemanalesMax(): number { return this.horasPactadas + 10; } 
}
class ContratoConsultoria extends ContratoLaboral {
  constructor(private proyectos: number) { super(); }
  override tipo(): string { return "Consultoría"; }
  override horasSemanalesMax(): number { return this.proyectos * 15; } 
}
const listaContratos: ContratoLaboral[] = [
  new ContratoTiempoParcial(20),
  new ContratoTiempoCompleto(40),
  new ContratoConsultoria(2),
];
for (const c of listaContratos) {
  console.log(`${c.tipo()}: horas semanales máximas = ${c.horasSemanalesMax()} horas`);
}
