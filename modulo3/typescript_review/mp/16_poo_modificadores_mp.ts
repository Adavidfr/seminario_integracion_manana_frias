class ExpedienteEmpleado {
  readonly numeroExpediente: string;           
  public empleado: string;        
  private salarioBase: number;         
  protected tipoContrato: string;      
  constructor(numeroExpediente: string, empleado: string, salarioInicial: number) {
    this.numeroExpediente = numeroExpediente;
    this.empleado = empleado;
    this.salarioBase = salarioInicial;
    this.tipoContrato = "Indefinido";
  }
  obtenerSalario(): number {
    return this.salarioBase;
  }
  aplicarBono(monto: number): void {
    if (monto <= 0) throw new Error("Monto de bono inválido");
    this.salarioBase += monto;
  }
}
const expediente = new ExpedienteEmpleado("EXP-001", "Ana García", 800.00);
console.log(expediente.empleado);         
console.log(expediente.numeroExpediente);              
console.log(expediente.obtenerSalario());  
expediente.aplicarBono(150);
console.log(expediente.obtenerSalario());  
