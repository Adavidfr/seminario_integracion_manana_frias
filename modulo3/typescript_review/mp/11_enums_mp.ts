enum AreaEmpresa {
  Reclutamiento,  
  Nomina,    
  Capacitacion,   
  Bienestar,  
}
const areaActual: AreaEmpresa = AreaEmpresa.Reclutamiento;
console.log(areaActual);           
console.log(AreaEmpresa[0]);    
enum CodigoEvaluacion {
  Sobresaliente = 200,
  Regular = 404,
  Deficiente = 500,
}
enum RolRRHH {
  Reclutador     = "RECLUTADOR",
  AnalistaNomina = "ANALISTA_NOMINA",
  GerenteRRHH    = "GERENTE_RRHH",
}
const miRolO: RolRRHH = RolRRHH.AnalistaNomina;
console.log(miRolO); 
