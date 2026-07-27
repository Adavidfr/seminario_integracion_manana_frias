# polimorfismo.py - Sistemas de notificación para empleados

# POLIMORFISMO POR HERENCIA — override de métodos
class Notificacion:
    """Clase base para distintos tipos de notificación."""
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje      = mensaje

    def enviar(self):
        raise NotImplementedError("Las subclases deben implementar enviar()")

    def __str__(self):
        return f"{self.__class__.__name__} → {self.destinatario}"

class NotificacionEmail(Notificacion):
    def __init__(self, destinatario, mensaje, asunto="Sin asunto"):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        return f"📧 Email a {self.destinatario}: [{self.asunto}] {self.mensaje}"

class NotificacionSMS(Notificacion):
    MAX_CHARS = 160

    def enviar(self):
        msg = self.mensaje[:self.MAX_CHARS]
        return f"📱 SMS a {self.destinatario}: {msg}"

class NotificacionPush(Notificacion):
    def enviar(self):
        return f"🔔 Push a {self.destinatario}: {self.mensaje[:50]}..."

class NotificacionSlack(Notificacion):
    def __init__(self, canal, mensaje):
        super().__init__(canal, mensaje)

    def enviar(self):
        return f"💬 Slack #{self.destinatario}: {self.mensaje}"

# Polimorfismo en acción — misma función, distintos tipos
def notificar_todos(notificaciones: list):
    for notif in notificaciones:
        print(f"  {notif.enviar()}")   # cada uno envía a su manera

alerts = [
    NotificacionEmail("ana@empresa.com",  "Tu nomina fue procesada", "Nómina #2024-01"),
    NotificacionSMS("+34600111222",        "Tu evaluación está disponible"),
    NotificacionPush("dispositivo-abc",    "¡Nueva solicitud de vacaciones recibida!"),
    NotificacionSlack("rrhh-alerts",       "Auditoría de nómina completada — revisar reportes"),
]

print("Enviando notificaciones de RR.HH.:")
notificar_todos(alerts)

# POLIMORFISMO DUCK TYPING — sin herencia
# "Si camina como un pato y grazna como un pato, es un pato"
class RegistroLocal:
    def leer(self):   return "datos desde archivo local"
    def guardar(self, datos): print(f"Guardando en disco: {datos[:30]}...")

class RegistroNube:
    def leer(self):   return "datos desde la nube"
    def guardar(self, datos): print(f"Subiendo a la nube: {datos[:30]}...")

class RegistroBD:
    def leer(self):   return "datos desde base de datos"
    def guardar(self, datos): print(f"Insertando en BD: {datos[:30]}...")

# Esta función funciona con CUALQUIER objeto que tenga leer() y guardar()
def procesar_registro(registro):
    contenido = registro.leer()
    print(f"Procesando: {contenido}")
    registro.guardar(f"resultado_{contenido}")

for registro in [RegistroLocal(), RegistroNube(), RegistroBD()]:
    procesar_registro(registro)
