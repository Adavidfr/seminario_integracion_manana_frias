class EvaluacionDesempeno {
  private _horasCapacitacion: number;
  constructor(horas: number) {
    this._horasCapacitacion = horas;
  }
  get horas(): number {
    return this._horasCapacitacion;
  }
  set horas(valor: number) {
    if (valor <= 0) throw new Error("Las horas deben ser positivas");
    this._horasCapacitacion = valor;
  }
  get puntosDesempeno(): number {
    return this._horasCapacitacion * 2.5;
  }
}
const evalA = new EvaluacionDesempeno(15);
console.log(evalA.horas);          
console.log(evalA.puntosDesempeno.toFixed(0)); 
evalA.horas = 20;                  
console.log(evalA.puntosDesempeno.toFixed(0)); 
