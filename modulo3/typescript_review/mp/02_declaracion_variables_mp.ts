const MAX_EMPLEADOS: number = 40;
const NOMBRE_APP: string = "GestionRRHHApp";
const DEBUG_MODE: boolean = false;
let empleadosActivos: number = 0;
let estadoDepartamento: string = "inactivo";
let sistemaOperativo: boolean = false;
console.log(`
    empleados activos: ${empleadosActivos} 
    estado del departamento: ${estadoDepartamento} 
    sistema operativo: ${sistemaOperativo}`);
empleadosActivos++;                         
estadoDepartamento = "operativo";       
sistemaOperativo = true;  
console.log(`
    empleados activos: ${empleadosActivos} 
    estado del departamento: ${estadoDepartamento} 
    sistema operativo: ${sistemaOperativo}`);             
