const nombreEmpleadoTemplate: string = "Carlos";
const departamentoTemplate: string = "Talento Humano";
const proyectosCompletados: number = 12;
const bienvenida: string = `Turno iniciado por ${nombreEmpleadoTemplate}. Depto: ${departamentoTemplate}. Proyectos hoy: ${proyectosCompletados}.`;
console.log(bienvenida);
const salarioBase: number = 800.00;
const bonoDesempeno: number = 150.00;
const salarioNeto: string = `Salario a recibir: $${(salarioBase + bonoDesempeno).toFixed(2)}`;
console.log(salarioNeto);
let oficina: string = "Sede Principal";
let oficinaAbierta: boolean = true;
let asistenciaPorcentaje: number = 85.5;
const reporteEmpleado: string = `
=== Reporte de Empleado ===
Ubicación : Sede Central
Estado    : activo
Asistencia : 90%
`;
const reporteEmpleado2: string = `
=== Reporte de Empleado ===
Ubicación : ${oficina}
Estado    : ${oficinaAbierta ? 'activo' : 'inactivo'}
Asistencia : ${asistenciaPorcentaje}%
`;
console.log(reporteEmpleado);
console.log(reporteEmpleado2);
