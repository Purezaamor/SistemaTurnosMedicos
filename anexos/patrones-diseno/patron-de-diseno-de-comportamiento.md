# Anexo – Aplicación de Patrón de Diseño de Comportamiento – Observer

## Patrones de Diseño de Comportamiento y su relación con SOLID

Los patrones de diseño de comportamiento se ocupan de los algoritmos y la asignación de responsabilidades entre objetos. En lugar de codificar comportamientos rígidos, estos patrones permiten que el sistema sea más flexible y extensible, facilitando la modificación de la lógica sin afectar otras partes del código.

En particular, el patrón **Observer** se relaciona directamente con varios principios **SOLID**:

- **Single Responsibility Principle (SRP):** el sujeto observado tiene la única responsabilidad de administrar su estado y notificar cambios, mientras que cada observador se encarga exclusivamente de reaccionar ante esas notificaciones según su propia lógica. De esta manera, las responsabilidades quedan claramente separadas.

- **Open/Closed Principle (OCP):** permite incorporar nuevos observadores sin modificar la implementación del sujeto observado. Basta con crear una nueva clase que implemente la interfaz de observador y registrarla en el sujeto.

- **Liskov Substitution Principle (LSP):** cualquier implementación concreta de un observador puede sustituir a otra siempre que respete el contrato definido por la interfaz. El sujeto interactúa con todos los observadores de la misma manera, sin depender de su implementación específica.

- **Interface Segregation Principle (ISP):** los observadores implementan una interfaz pequeña y específica, normalmente compuesta por el método de actualización (`update()`), evitando que las clases dependan de métodos que no utilizan.

- **Dependency Inversion Principle (DIP):** tanto el sujeto como los observadores dependen de abstracciones (interfaces) y no de implementaciones concretas. Esto reduce el acoplamiento y facilita la incorporación de nuevas implementaciones sin modificar el resto del sistema.

## Propósito y Tipo del Patrón

**Propósito:**  
En el sistema de turnos médicos, existía un problema de acoplamiento fuerte en la lógica de notificaciones. Cada vez que se creaba, cancelaba o reprogramaba un turno, el código debía llamar directamente a múltiples servicios de notificación (email, SMS, WhatsApp, etc.). Esto generaba código duplicado y difícil de mantener. El patrón Observer resuelve esto permitiendo que el **Sujeto** (Turno) mantenga una lista de **Observadores** (Notificadores) y los notifique automáticamente ante cualquier cambio de estado.

**Tipo:**  
Observer es un patrón de comportamiento que define una dependencia uno-a-muchos entre objetos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados y actualizados automáticamente. Es especialmente adecuado para manejar eventos y notificaciones en tiempo real sin generar un fuerte acoplamiento entre el objeto que produce el evento y quienes reaccionan a él.

En el sistema de turnos médicos, el cambio de estado de un `Turno` (por ejemplo, creación, cancelación o reprogramación) debe generar notificaciones simultáneas a distintos canales de comunicación, como correo electrónico, SMS o WhatsApp. El patrón **Observer** resulta el más apropiado porque permite que cada mecanismo de notificación se registre como observador y reciba automáticamente los eventos emitidos por el `Turno`, sin que este conozca las implementaciones concretas de cada canal.

Se analizaron otros patrones de comportamiento del catálogo GoF y se descartaron por no ajustarse al problema planteado. El patrón **Strategy** permite intercambiar distintos algoritmos para realizar una misma tarea, pero no está diseñado para notificar a múltiples receptores cuando ocurre un cambio de estado. Por su parte, **Chain of Responsibility** distribuye una solicitud a través de una cadena de objetos hasta que alguno la procesa, mientras que en este caso el objetivo es que **todos** los mecanismos de notificación reciban el mismo evento, y no que uno de ellos decida si continúa o detiene el procesamiento.

Por estas razones, **Observer** modela de manera directa la necesidad del sistema, facilita la incorporación de nuevos canales de notificación sin modificar la clase `Turno` y mantiene un bajo acoplamiento entre el emisor del evento y sus receptores, respetando además los principios Open/Closed (OCP) y Dependency Inversion (DIP).

## Motivación

Originalmente, el sistema manejaba las notificaciones mediante llamadas directas a métodos de clases concretas, como `EnviarEmail()`, `EnviarSMS()` y `EnviarWhatsApp()`. Esto provocaba:

- **Alto acoplamiento:** cada clase que modificaba un turno debía conocer todos los servicios de notificación.
- **Dificultad para agregar nuevos canales:** cada nuevo medio implicaba modificar todas las clases que notificaban.
- **Violación de SRP:** las clases de negocio tenían responsabilidades de notificación.

Con el patrón Observer, se introduce:

- **Interfaz `IObservador`:** define el método `actualizar(evento)`.
- **Clase `Sujeto` (Turno):** mantiene la lista de observadores y notifica cambios.
- **Observadores concretos:** `NotificadorEmail`, `NotificadorSMS`, `NotificadorWhatsApp` que implementan `IObservador`.

El flujo ahora es:

1. El paciente o secretaria realiza una acción (crear/cancelar/reprogramar turno).
2. El turno cambia su estado y ejecuta `notificarObservadores()`.
3. Cada observador reacciona según su canal (envía email, SMS, etc.).

Esto desacopla completamente la lógica de notificación de la lógica de negocio, facilitando agregar nuevos canales sin modificar las clases existentes.

## Estructura de Clases

Solo se incluyen las clases directamente relacionadas con la implementación del patrón Observer, para mantener claridad y enfoque.

![Diagrama UML - Observer](../../diagramas/01-diagrama-clases/01-patron-comportamiento-observer.png)

*Ver diagrama en tamaño completo: [01-patron-comportamiento-observer.puml](../../diagramas/01-diagrama-clases/01-patron-comportamiento-observer.puml)*

## Justificación Técnica de la Estructura de Clases

El patrón **Observer** fue seleccionado porque el problema consiste en mantener sincronizados múltiples componentes cuando cambia el estado de un turno. Cada vez que un `Turno` es creado, cancelado o reprogramado, distintos mecanismos de notificación deben reaccionar automáticamente sin que el `Turno` conozca los detalles de implementación de cada uno.

Se decidió que `Turno` **herede de la clase abstracta `Observable`** en lugar de implementar directamente una interfaz `ISubject`. Esta decisión permite reutilizar la lógica común de administración de observadores, como registrarlos, eliminarlos y notificarlos cuando ocurre un cambio de estado. Si `Turno` implementara únicamente una interfaz, debería desarrollar toda esta funcionalidad por sí mismo o duplicarla en otras clases que también requirieran ser observables. De este modo, `Observable` actúa como una clase base reutilizable que encapsula dicho comportamiento común, mientras que `Turno` se concentra exclusivamente en la lógica propia del dominio de negocio.

### Clases incluidas en el diagrama:

| Clase | Responsabilidad | Relación |
|-------|----------------|----------|
| `Observable` | Clase base abstracta que administra la lista de observadores y proporciona las operaciones para registrarlos, eliminarlos y notificarlos. | Superclase de `Turno` |
| `Turno` | Sujeto observable. Mantiene su estado y utiliza la funcionalidad heredada para notificar cambios a los observadores. | Hereda de `Observable` |
| `IObservador` | Interfaz que define el método `actualizar(evento)`. | Implementada por observadores concretos |
| `NotificadorEmail` | Observador concreto que envía email ante un evento. | Implementa `IObservador` |
| `NotificadorSMS` | Observador concreto que envía SMS ante un evento. | Implementa `IObservador` |
| `NotificadorWhatsApp` | Observador concreto que envía mensaje por WhatsApp. | Implementa `IObservador` |

### Flujo de comportamiento:

1. El `Turno` cambia su estado (`creado`, `cancelado`, `reprogramado`).
2. Se invoca el método heredado `notificarObservadores(evento)`.
3. `Observable` recorre su lista de observadores y llama a `actualizar(evento)` en cada uno.
4. Cada observador reacciona según su canal, enviando el mensaje correspondiente.

Este diseño permite agregar nuevos observadores (por ejemplo, `NotificadorPush`) sin modificar la clase `Turno` ni la clase `Observable`, cumpliendo con los principios **Open/Closed (OCP)** y **Dependency Inversion (DIP)**.

### Justificación de la selección del patrón

El patrón **Observer** es el más adecuado para este problema porque el objetivo es notificar automáticamente a múltiples componentes cuando cambia el estado de un `Turno`. En cambio, **Strategy** se utiliza para intercambiar algoritmos o comportamientos, mientras que **Command** encapsula solicitudes u operaciones para ejecutarlas posteriormente o desacoplar al emisor del receptor. Ninguno de ellos resuelve de forma tan directa la necesidad de propagar eventos a múltiples interesados como lo hace **Observer**.