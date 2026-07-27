abstract class BeneficioLaboral {
  abstract calcularCosto(): number;       
  abstract duracionMeses(): number;
  generarSolicitud(): string {
    return (
      `Costo Estimado: $${this.calcularCosto().toFixed(2)} | ` +
      `Vigencia: ${this.duracionMeses().toFixed(1)} meses`
    );
  }
}
class SeguroMedico extends BeneficioLaboral {
  constructor(private dependientes: number) {
    super();
  }
  override calcularCosto(): number {
    return 50 + (this.dependientes * 20); 
  }
  override duracionMeses(): number {
    return 12.0;
  }
}
class BonoAlimentacion extends BeneficioLaboral {
  constructor(private diasTrabajados: number) {
    super();
  }
  override calcularCosto(): number {
    return this.diasTrabajados * 5; 
  }
  override duracionMeses(): number {
    return 1.0; 
  }
}
const seguro = new SeguroMedico(2);
const bono = new BonoAlimentacion(22);
console.log(seguro.generarSolicitud()); 
console.log(bono.generarSolicitud());    
