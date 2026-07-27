type EstadoEmpleado = "en_induccion" | "activo" | "en_vacaciones" | "desvinculado";
type PrioridadSolicitud = "baja" | "media" | "alta";
function registrarEstadoEmpleado(idEmpleado: number, estado: EstadoEmpleado): void {
  console.log(`Empleado #${idEmpleado}: ${estado}`);
}
registrarEstadoEmpleado(101, "activo"); 
type NivelSolicitud = "baja" | "media" | "alta" | "critica";
interface SolicitudRRHH {
  id: number;
  descripcion: string;
  prioridad: NivelSolicitud;
  atendido: boolean;
}
function clasificarSolicitud(s: SolicitudRRHH): string {
  const prefijos: Record<NivelSolicitud, string> = {
    baja:    "⚪",
    media:   "🟡",
    alta:    "🟠",
    critica: "🔴",
  };
  const estado = s.atendido ? "✅" : "⏳";
  return `${estado} ${prefijos[s.prioridad]} [#${s.id}] ${s.descripcion}`;
}
const solicitudes: SolicitudRRHH[] = [
  { id: 1, descripcion: "Actualización de certificado laboral", prioridad: "baja",    atendido: true  },
  { id: 2, descripcion: "Incapacidad médica urgente",           prioridad: "critica", atendido: false },
  { id: 3, descripcion: "Solicitud de vacaciones",              prioridad: "media",   atendido: false },
];
for (const s of solicitudes) {
  console.log(clasificarSolicitud(s));
}
