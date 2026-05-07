## Code Review 1

### PR revisada
feature/disenador-dip-analisis-dependencias

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- herramientas-agile/tarjetas-crc/
- anexos/principios-solid/05-dip.md
- diagramas/01-diagrama-clases/01-solid-05-dip.puml
- ia/primer-parcial/especialista-dip.md
- changelog.md

### Prompt utilizado

```text
Actuá como revisor técnico de la materia Diseño Orientado a Objetos.

Analizá la rama/PR feature/disenador-dip-analisis-dependencias correspondiente al rol Especialista en Inversión de Dependencias (DIP).

Usá como contexto:
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- herramientas-agile/tarjetas-crc/
- anexos/principios-solid/05-dip.md
- diagramas/01-diagrama-clases/01-solid-05-dip.puml
- ia/primer-parcial/especialista-dip.md
- changelog.md

Validá específicamente:
- Que exista anexos/principios-solid/05-dip.md.
- Que explique qué es una clase abstracta y qué es una interfaz.
- Que identifique dependencias concretas del diseño actual.
- Que proponga abstracciones coherentes con el dominio.
- Que explique dónde aplicar inyección de dependencias.
- Que exista diagramas/01-diagrama-clases/01-solid-05-dip.puml y su .png.
- Que el diagrama represente correctamente DIP.
- Que exista ia/primer-parcial/especialista-dip.md con prompt, contexto, output y ajustes.
- Que changelog.md registre la PR con formato correcto.
- Que la PR esté lista para aprobar o requiera cambios.


### Observaciones detectadas

#### Qué cumple
- Existe `anexos/principios-solid/05-dip.md` con explicación correcta de clases abstractas e interfaces.
- Se identifican dependencias concretas del diseño actual (Turno, Agenda, ControladorTurnos, NotificadorEmail).
- Se proponen abstracciones coherentes con el dominio (ITurno, IEspecialista, IPaciente, IAgenda, INotificador).
- Se explica correctamente la aplicación de inyección de dependencias.
- Existe el diagrama `01-solid-05-dip.puml` representando correctamente el principio DIP.

#### Qué falta o está mal
- No existe el archivo `.png` del diagrama.
- Falta el archivo `ia/primer-parcial/especialista-dip.md`.
- El archivo `changelog.md` contiene conflictos sin resolver (`<<<<<<<`, `=======`, `>>>>>>>`).
- No se registra la PR #98 en el changelog con el formato correcto.
- La rama no respeta el flujo requerido (debería ser `fix/` desde `release/primer-parcial`).

#### Ajustes solicitados
- Generar y agregar `01-solid-05-dip.png`.
- Crear `ia/primer-parcial/especialista-dip.md` con estructura completa (prompt, contexto, output y ajustes).
- Resolver conflictos en `changelog.md`.
- Registrar correctamente la PR #98 en el changelog.
- Corregir el flujo de trabajo creando una rama `fix/disenador-dip-analisis-dependencias` desde `release/primer-parcial` y recrear la PR.

### Veredicto
Request Changes


## Code Review 2

### PR revisada
fix/esp-ocp-lsp-correcciones

### Archivos de contexto usados
- anexos/introduccion.md
- herramientas-agile/tarjetas-crc/
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- anexos/principios-solid/02-ocp.md
- anexos/principios-solid/03-lsp.md
- diagramas/01-diagrama-clases/01-solid-02-ocp.puml
- diagramas/01-diagrama-clases/01-solid-02-ocp.png
- diagramas/01-diagrama-clases/01-solid-03-lsp.puml
- diagramas/01-diagrama-clases/01-solid-03-lsp.png
- ia/primer-parcial/especialista-ocp.md
- ia/primer-parcial/especialista-lsp.md
- changelog.md

### Prompt utilizado

```text
Actuá como revisor técnico de la materia Diseño Orientado a Objetos.

Analizá la rama/PR `fix/esp-ocp-lsp-correcciones` correspondiente al rol Especialista en Principios de Extensión (OCP + LSP).

Validá si existen los archivos 02-ocp.md y 03-lsp.md, si explican correctamente OCP y LSP, si incluyen motivación con ejemplos del sistema, si explican herencia, si existen los diagramas .puml y .png, si los diagramas representan correctamente OCP y LSP, si la solución respeta extensibilidad y sustituibilidad, si existe documentación de IA completa y si el changelog registra correctamente la PR.

### Observaciones detectadas

#### Qué cumple
- Existen `02-ocp.md` y `03-lsp.md` con explicaciones correctas de OCP y LSP.
- Incluyen motivación con ejemplos del sistema.
- Hay explicación de herencia en ambos archivos.
- Existen los diagramas `.puml` y `.png` para OCP y LSP.
- Los diagramas representan correctamente OCP mediante tipos de turno y LSP mediante la jerarquía `Persona`.
- La solución respeta extensibilidad mediante polimorfismo.
- Las subclases son sustituibles sin alterar el comportamiento esperado.
- Existe documentación de IA completa en `especialista-ocp.md` y `especialista-lsp.md`.

#### Qué falta o está mal
- El changelog registra una PR relacionada (`feature/esp-extension-ocp-lsp`, PR #91), pero falta una entrada específica para `fix/esp-ocp-lsp-correcciones`.
- Falta crear o vincular la PR correspondiente desde `fix/esp-ocp-lsp-correcciones` hacia la rama base apropiada.

#### Ajustes solicitados
- Agregar entrada en `changelog.md` para `fix/esp-ocp-lsp-correcciones`.
- Crear o vincular la PR correspondiente a la rama `fix/esp-ocp-lsp-correcciones`.

### Veredicto
**Approve**

## Code Review 3

### PR revisada
fix/correcciones-isp-y-docum

### Archivos de contexto usados
- anexos/introduccion.md
- herramientas-agile/tarjetas-crc/
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- anexos/principios-solid/04-isp.md
- diagramas/01-diagrama-clases/01-solid-04-isp.puml
- diagramas/01-diagrama-clases/01-solid-04-isp.png
- ia/primer-parcial/especialista-isp.md
- changelog.md
- README.md

### Prompt utilizado

```text
Actuá como revisor técnico de la materia Diseño Orientado a Objetos.

Analizá la rama/PR fix/correcciones-isp-y-docum correspondiente al rol Especialista en Segregación de Interfaces (ISP) y ajustes de documentación.

Usá como contexto:
- anexos/introduccion.md
- herramientas-agile/tarjetas-crc/
- diagrama de clases inicial
- archivo 04-isp.md
- diagramas UML de ISP
- documentación de IA
- changelog.md
- README.md

Validá específicamente:
- Que exista 04-isp.md.
- Que explique correctamente qué es una interfaz.
- Que identifique responsabilidades que deben separarse.
- Que evite interfaces “gordas”.
- Que proponga interfaces coherentes con el dominio.
- Que exista el diagrama .puml y .png.
- Que el diagrama represente correctamente ISP.
- Que exista documentación de IA completa.
- Que los cambios de documentación sean correctos.
- Que el changelog registre la PR correctamente.
- Que la rama respete el flujo (fix/ desde release/primer-parcial).

### Observaciones detectadas

#### Qué cumple
- Existe `04-isp.md` con estructura completa y correcta.
- Explica adecuadamente qué es una interfaz como contrato abstracto.
- Identifica responsabilidades que deben separarse en clases sobrecargadas (`Turno`, `Agenda`, `Secretaria`).
- Evita interfaces “gordas” proponiendo interfaces específicas (`ICancelable`, `IReprogramable`, `IVerificadorLlegada`, `INotificable`, `IOperadorTurnos`, `IValidadorDisponibilidad`).
- Propone interfaces coherentes con el dominio del sistema de turnos médicos.
- Existen los diagramas `01-solid-04-isp.puml` y `01-solid-04-isp.png`.
- El diagrama representa correctamente la segregación de interfaces (cada clase implementa solo lo necesario).
- Existe documentación de IA completa en `especialista-isp.md` (prompt, contexto, output y ajustes).
- La rama respeta el flujo correcto (`fix/` basada en `release/primer-parcial`).
- El `changelog.md` registra la PR #102 correctamente.

#### Qué falta o está mal
- En `README.md` se eliminaron enlaces de navegación importantes:
  - `Casos de Uso`
  - `Escenarios`
  Esto afecta la navegabilidad del proyecto.
- En `changelog.md` hay una referencia inválida:
  - `PR: [#0143278]` corresponde a un hash de commit y no a un número de PR.
- Existe inconsistencia menor en la sintaxis del changelog:
  - Uso mezclado de `—` y `-` para autores.
  - Presencia/ausencia de punto final en las líneas.

#### Ajustes solicitados
- Restaurar los enlaces eliminados en `README.md` dentro de la sección correspondiente.
- Corregir la referencia inválida en `changelog.md`, utilizando un número de PR válido o eliminando la referencia.
- Normalizar el formato del changelog:
  - Usar `—` (em-dash) de forma consistente.
  - Mantener punto final al final de cada entrada.

### Veredicto
Request Changes

## Code Review 4

### PR revisada
fix/esp-ocp-lsp-correcciones

### Archivos de contexto usados
- anexos/introduccion.md
- herramientas-agile/tarjetas-crc/
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- anexos/principios-solid/02-ocp.md
- anexos/principios-solid/03-lsp.md
- diagramas/01-diagrama-clases/01-solid-02-ocp.puml
- diagramas/01-diagrama-clases/01-solid-02-ocp.png
- diagramas/01-diagrama-clases/01-solid-03-lsp.puml
- diagramas/01-diagrama-clases/01-solid-03-lsp.png
- ia/primer-parcial/especialista-ocp.md
- ia/primer-parcial/especialista-lsp.md
- changelog.md

### Prompt utilizado

```text
Actuá como revisor técnico de la materia Diseño Orientado a Objetos.

Analizá la rama/PR fix/esp-ocp-lsp-correcciones correspondiente al rol Especialista en Principios de Extensión (OCP + LSP).

Validá si existen los archivos 02-ocp.md y 03-lsp.md, si explican correctamente OCP y LSP, si incluyen motivación con ejemplos del sistema, si explican herencia y polimorfismo, si existen los diagramas .puml y .png, si los diagramas representan correctamente OCP y LSP, si la solución respeta extensibilidad y sustituibilidad, si existe documentación de IA completa y si el changelog registra correctamente la PR.

### Observaciones detectadas

#### Qué cumple
- Existen `02-ocp.md` y `03-lsp.md` con explicaciones detalladas y correctas de OCP y LSP.
- Incluyen motivación con ejemplos del sistema.
- Explican correctamente herencia y polimorfismo.
- Existen los diagramas `.puml` y `.png` para OCP y LSP.
- Los diagramas representan correctamente OCP (jerarquía de `Turno`) y LSP (jerarquía de `Persona`).
- La solución respeta extensibilidad mediante polimorfismo.
- Las subclases son sustituibles sin alterar el comportamiento esperado.
- Existe documentación de IA completa en `especialista-ocp.md` y `especialista-lsp.md`.
- La rama respeta el flujo (`fix/` basada en `release/primer-parcial`).
- El `changelog.md` registra la corrección en la sección correspondiente.

#### Qué falta o está mal

#### Ajustes solicitados

### Veredicto
Approve