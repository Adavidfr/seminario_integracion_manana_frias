class SalarioLaboral {
  valorMensual: number = 0;
  valorAnual: number = 0;
  constructor(mensual: number = 0, anual: number = 0) {
    this.valorMensual = mensual;
    this.valorAnual = anual;
  }
  aAnual(): number {
    return this.valorMensual * 12;
  }
  aSemanal(): number {
    return (this.valorMensual * 12) / 52;
  }
  aMensual(): number {
    this.valorMensual = this.valorAnual / 12;
    return this.valorMensual;
  }
  reportarSalario(): string {
    return (
      `$${this.valorMensual.toFixed(2)} mensual = ` +
      `$${this.aAnual().toFixed(2)} anual = ` +
      `$${this.aSemanal().toFixed(2)} semanal`
    );
  }
}
const salarioJunior = new SalarioLaboral(800);
const sinIngresos = new SalarioLaboral(0);
const salarioEjecutivo = new SalarioLaboral(0, 24000); 
console.log(salarioJunior.reportarSalario());     
console.log(sinIngresos.reportarSalario()); 
console.log(salarioEjecutivo.aMensual().toFixed(2));
