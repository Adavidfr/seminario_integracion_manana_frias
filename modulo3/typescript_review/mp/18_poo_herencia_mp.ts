class EmpleadoEmpresa {
  constructor(public nombre: string) {}
  reportarse(): string {
    return `${this.nombre} se reporta a su turno laboral.`;
  }
}
class Reclutador extends EmpleadoEmpresa {
  constructor(nombre: string, public especialidad: string) {
    super(nombre); 
  }
  override reportarse(): string {
    return `${this.nombre} inicia proceso de selección (Especialidad: ${this.especialidad}).`;
  }
  entrevistarCandidato(candidato: string): string {
    return `${this.nombre} está entrevistando al candidato ${candidato}.`;
  }
}
const tEmpleado = new EmpleadoEmpresa("Empleado General");
const cReclutador = new Reclutador("Carlos", "Tecnología");
console.log(tEmpleado.reportarse());       
console.log(cReclutador.reportarse());       
console.log(cReclutador.entrevistarCandidato("Juan Pérez")); 
console.log(cReclutador.especialidad);           
