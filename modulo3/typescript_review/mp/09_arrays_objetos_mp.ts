type EmpleadoObj = {
  idEmpleado: number;
  codigo: string;
  capacidadProyectos: number;
  activo: boolean;
  horasTrabajadas: number;
};
const plantilla: EmpleadoObj[] = [
  { idEmpleado: 1, codigo: "EMP-1234", capacidadProyectos: 4, activo: true, horasTrabajadas: 25 },
  { idEmpleado: 2, codigo: "EMP-5678", capacidadProyectos: 8, activo: true, horasTrabajadas: 60 },
  { idEmpleado: 3, codigo: "EMP-9012", capacidadProyectos: 4, activo: false, horasTrabajadas: 0 },
  { idEmpleado: 4, codigo: "EMP-3456", capacidadProyectos: 2, activo: true, horasTrabajadas: 15 },
  { idEmpleado: 5, codigo: "EMP-7890", capacidadProyectos: 12, activo: true, horasTrabajadas: 100 },
];
const enTurno: EmpleadoObj[] = plantilla.filter((v) => v.activo);
const codigos: string[] = plantilla.map((v) => v.codigo);
const menosHoras: EmpleadoObj | undefined = plantilla.reduce((min, v) =>
  v.horasTrabajadas < min.horasTrabajadas ? v : min
);
const plantillaCompleta: EmpleadoObj[] = plantilla.map((v) => v);
console.log(plantillaCompleta);
const horasEmpleado4: number = plantilla[3].horasTrabajadas;
console.log(`Horas actuales del empleado 4: ${horasEmpleado4}`);
