interface Evaluable {
  generarReporteEvaluacion(): string;
}
interface Contratable {
  estaActivo(): boolean;
}
class EmpleadoAsignado implements Evaluable, Contratable {
  constructor(
    public id: string,
    public habilidades: string[],
    public proyectosActivos: number
  ) {}
  generarReporteEvaluacion(): string {
    return JSON.stringify({ id: this.id, habilidades: this.habilidades, evaluacion: "Satisfactoria" });
  }
  estaActivo(): boolean {
    return this.habilidades.length >= 2 && this.proyectosActivos > 0;
  }
}
const empleadoProgramado = new EmpleadoAsignado("EMP-001", ["TypeScript", "Liderazgo"], 5);
console.log(empleadoProgramado.estaActivo());    
console.log(empleadoProgramado.generarReporteEvaluacion());
