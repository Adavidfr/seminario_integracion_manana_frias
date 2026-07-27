const totalEmpleadosGlobales: number = 42;
const salarioPorHora: number = 12.50;
const diasVacacionesPendientes: number = -5;
const codigoColorBadge: number = 0xff;   
const binarioDept: number = 0b1010;     
const octalDept: number = 0o17;         
const empleadosGlobales: number = 1_000_000;   
console.log(codigoColorBadge); 
console.log(binarioDept);     
console.log(empleadosGlobales);      
console.log(Number.MAX_SAFE_INTEGER); 
console.log(Number.isFinite(1 / 0)); 
console.log(Number.isNaN(0 / 0));    
const nombreDepartamento: string = "Recursos Humanos";
const oficinaDestino: string = 'Sede Sur';
const avisoOficina: string = `Próxima capacitación: ${"Integración"}`; 
const empleadoTipos: string = "Elena";
const saldoBonos: number = 250.50;
const mensajeSaldo: string = `Hola, ${empleadoTipos}. Tu saldo de bonos es $${saldoBonos}.`;
const puedeCapacitarse: string = `Puedes ${saldoBonos >= 50 ? "inscribirte" : "solicitar fondos"} hoy.`;
const avisoCapacitacion: string = `
  Módulo 1: Inducción
  Módulo 2: Seguridad
  Módulo 3: Liderazgo
`.trim();
console.log("  Depto 1  ".trim());      
console.log("RECURSOS HUMANOS".toLowerCase());   
console.log("oficina".toUpperCase());      
console.log("2024-06-15".split("-"));   
console.log("alerta: vacante activa".includes("alerta")); 
console.log("empleado.json".endsWith(".json"));     
console.log("empleado.json".startsWith(".json"));
const empleadoEnTurno: boolean = true;
const contratoCancelado: boolean = false;
const esSinCosto = 12.50 <= 0;    
const hayVacantesDisponibles = 5 > 0;    
if (!hayVacantesDisponibles) {
  console.log("Sin vacantes disponibles en el departamento");
}
let departamentoSinAsignar: undefined = undefined;
let puestoSinEmpleado: null = null;
function buscarGerente(idDept: number): string | null {
  if (idDept === 1) return "Mario";
  return null; 
}
const gerenteAsignado = buscarGerente(5);
const nombreGerente = gerenteAsignado ?? "Reemplazo";
console.log(nombreGerente); 
const experienciaGerente = nombreGerente?.length;
console.log(experienciaGerente); 
