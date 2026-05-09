# Uso de IA - Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5

## Prompt utilizado

```
Basándote en los archivos diagramas/02-casos-de-uso/02-caso-uso-cancelar-turno-03.puml y diagramas/03-escenarios-casos-de-uso/03-cancelar-turno-principal-01.md (lo mismo hice con los otros casos de uso), generame el código PlantUML para un diagrama de actividades. Necesito que tenga al menos 3 swimlanes (Paciente, Secretaria, Sistema), más de 10 actividades y que incluya rombos de decisión para el flujo alternativo (Incluir elementos de control de flujo: decisiones (if), caminos alternativos, inicio y fin.)
Ya he creado el archivo .puml donde quiero que ponga el codigo, el cual se llama (le pegué el directorio donde tiene que poner para los 3 casos de uso) que está dentro de la nueva carpeta que tambien he creado "04-diagramas-actividades".
```

## Archivos utilizados como contexto

* diagramas/02-casos-de-uso/02-caso-uso-cancelar-turno-03.puml
* diagramas/03-escenarios-casos-de-uso/03-cancelar-turno-principal-01.md
* diagramas/02-casos-de-uso/02-caso-uso-visualizar-agenda-medica-04.puml
* diagramas/03-escenarios-casos-de-uso/03-ver-agenda-flujo-principal-01.md
* diagramas/02-casos-de-uso/02-caso-uso-administrar-disponibilidad-05.puml
* diagramas/03-escenarios-casos-de-uso/03-disponibilidad-flujo-principal-01.md


## Ajustes realizados al output de la IA

* Se eliminaron los acentos que puso la IA en las palabras que requerian acentos, ya que generaba error en el diagrama.
* En el codigo .puml que me ha hecho Copilot Agent Mode en el diagrama de actividades del caso 4, había un rombo que estaba en "Sistema (Base de Datos)" que no hacía nada, pero como la condición "if" se abrió en ese swimlane quería cerrarlo ahí y quedaba raro. Entonces se modificó el codigo para que el "if" de `¿Existen turnos cargados?` esté en "Modulo Agenda (Interfaz)".
* En el codigo .puml que me generó el Copilot en el caso 5, puso una palabra "merge" todo suelta y me rompió el diagrama para visualizarlo, entonces he eliminado la palabra para que funcione correctamente.

## Resultado

Se obtuvo con gran acertación el diagrama PlantUML hecho por la IA, añadiendole pequeños retoques en los codigos que fueron minimos.