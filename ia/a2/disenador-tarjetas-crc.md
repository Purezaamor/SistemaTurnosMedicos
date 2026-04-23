# Uso de IA - Diseñador de Tarjetas CRC

## Prompt utilizado

"Analizar el archivo anexos/introduccion.md y el diagrama de clases del sistema de turnos médicos para identificar las clases principales. Generar tarjetas CRC incluyendo nombre de clase, superclase, subclase, responsabilidades, colaboradores, pensamiento del objeto y propiedades."

---

## Archivos utilizados como contexto

- anexos/introduccion.md  
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw  

---

## Ajustes realizados al resultado de la IA

- Se corrigieron nombres de clases para alinearlos al dominio del sistema de turnos médicos
- Se ajustaron responsabilidades para evitar duplicación de funciones entre clases
- Se mejoraron los colaboradores para reflejar correctamente la interacción entre objetos
- Se simplificaron los pensamientos del objeto para que sean más claros y representativos
- Se validaron las propiedades según los requisitos funcionales del sistema
- Se incorporó una nueva clase **HistorialCambios** para representar la auditoría y trazabilidad del sistema
- Se revisó la clase **Turno** para explicitar la relación con **Paciente** y **Medico**
- Se descartaron elementos que no correspondían al modelo (clases irrelevantes o redundantes)

---

## Resultado final

Como resultado del proceso se generaron un total de **6 tarjetas CRC** correspondientes a las clases principales del sistema:

- Persona  
- Paciente  
- Medico  
- Turno  
- Agenda  
- HistorialCambios  

Inicialmente se identificaron 5 clases clave, pero durante la revisión del diseño se incorporó la clase **HistorialCambios** con el objetivo de cubrir los requerimientos de auditoría del sistema.

Las tarjetas incluyen responsabilidades, colaboradores, pensamiento del objeto y propiedades, permitiendo validar la correcta asignación de responsabilidades dentro del modelo orientado a objetos.

Las tarjetas fueron organizadas en la carpeta:

herramientas-agile/tarjetas-crc/

Cumpliendo con la estructura y formato requerido por la consigna.