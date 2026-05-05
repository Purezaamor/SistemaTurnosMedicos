### Prompt utilizado
Leer los archivos anexos/introduccion.md y diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw.
Identifica las clases principales del sistema y genera una tarjeta CRC para cada una, usando la plantilla: nombre, superclase/subclase, pensamiento del objeto, responsabilidades, colaboraciones, propiedad. Revisa el diseño y corrige errores si detectás.

### Archivos de contexto utilizados

- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

### Ajustes realizados

- Unifiqué los atributos "nombre", "apellido", "telefono" y "mail" en una clase base abstracta "Persona" (no repetir código).
- Trasladé la lógica de gestión de turnos desde "Paciente" a la clase "Agenda" para respetar el diseño por responsabilidad.
- Eliminé métodos de actores desde "Secretaria", dejando solo las colaboraciones y propiedades.
- Incorporé la clase "HistorialCambio" que no estaba en el boceto pero era requerida por los requisitos funcionales.

---
=======
# Uso de IA - Diseñador de Tarjetas CRC

## Prompt utilizado

```text
Analizar el archivo anexos/introduccion.md y el diagrama de clases del sistema de turnos médicos
para identificar las clases principales. Generar tarjetas CRC incluyendo nombre de clase,
superclase, subclase, responsabilidades, colaboradores, pensamiento del objeto y propiedades.
```

---

## Archivos utilizados como contexto

- anexos/introduccion.md  
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw  

---

## Output generado por la IA (fragmento)

Clase: Turno  
Responsabilidades:
- Registrar turno
- Cambiar estado
- Permitir cancelación  

Colaboradores:
- Paciente  
- Medico  
- Agenda  

---

## Ajustes realizados al resultado de la IA

- Se corrigieron nombres de clases para alinearlos al dominio del sistema
- Se ajustaron responsabilidades para evitar duplicación entre clases
- Se mejoraron los colaboradores para reflejar correctamente la interacción entre objetos
- Se simplificaron los pensamientos del objeto para mayor claridad
- Se validaron las propiedades según los requisitos funcionales
- Se incorporó la clase **HistorialCambios** para representar la auditoría del sistema
- Se ajustó la clase **Turno** para explicitar su relación con **Paciente** y **Medico**

---

## Iteraciones realizadas

- Iteración 1: Generación inicial de tarjetas CRC con inconsistencias en responsabilidades y colaboradores.
- Iteración 2: Ajuste de responsabilidades y mejora de relaciones entre clases.
- Iteración 3: Incorporación de la clase HistorialCambios para cubrir auditoría.
- Iteración 4: Refinamiento final para cumplir con la consigna y estructura requerida.

---

## Resultado final

Se generaron **8 tarjetas CRC** correspondientes a las clases principales del sistema:

- Persona  
- Paciente  
- Medico  
- Turno  
- Agenda  
- HistorialCambios  
- Secretaria  
- LlegadaPaciente  

Las tarjetas fueron organizadas en la carpeta:

herramientas-agile/tarjetas-crc/

Cumpliendo con la estructura y formato requerido por la consigna.

