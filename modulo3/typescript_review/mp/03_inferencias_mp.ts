const empleadoId: number = 101;
const departamentoDestino: string = "Recursos Humanos";
const enNomina: boolean = true;
const empleadoId2 = 101;       
const departamentoDestino2 = "Recursos Humanos";  
const enNomina2 = true;       
let diasVacaciones: number;      
diasVacaciones = 15;
let codigoEmpleado: number | string = 500;  
codigoEmpleado = "EMP-500";  
function reportarAsistencia(departamento: string, empleados: number): string {
  return `Reporte en ${departamento} — ${empleados} empleado(s) en turno`;
}
