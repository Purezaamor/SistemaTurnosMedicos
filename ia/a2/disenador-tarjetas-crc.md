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