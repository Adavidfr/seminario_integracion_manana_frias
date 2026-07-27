class DepartamentoRRHH {
  nombre: string;
  capacidadMax: number;
  activo: boolean;
  constructor(nombre: string, capacidadMax: number, activo: boolean) {
    this.nombre = nombre;
    this.capacidadMax = capacidadMax;
    this.activo = activo;
  }
  informarEstado(): string {
    const estado = this.activo ? "operativo" : "inactivo";
    return `Departamento ${this.nombre} — Capacidad: ${this.capacidadMax} emp (${estado})`;
  }
}
const deptoReclutamiento = new DepartamentoRRHH("Reclutamiento", 40, true);
const deptoCapacitacion = new DepartamentoRRHH("Capacitación", 120, false);
console.log(deptoReclutamiento.informarEstado()); 
console.log(deptoCapacitacion.informarEstado()); 
