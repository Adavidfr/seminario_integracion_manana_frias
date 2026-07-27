let datosEmpleadoCualquiera: any = "sin registros";
datosEmpleadoCualquiera = 101;       
datosEmpleadoCualquiera = true;     
datosEmpleadoCualquiera.desvincular(); 
let datosCapacitacion: unknown = "activo";
datosCapacitacion = 120;                 
if (typeof datosCapacitacion === "string") {
  console.log(datosCapacitacion.toUpperCase()); 
}
function alertaCriticaRRHH(msg: string): never {
  throw new Error(`CRÍTICO RRHH: ${msg}`); 
}
function manejarEstadoImposible(estado: never): never {
  throw new Error(`Estado de empleado no manejado: ${String(estado)}`);
}
