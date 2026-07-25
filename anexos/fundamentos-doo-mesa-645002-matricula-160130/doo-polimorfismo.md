# POLIMORFISMO

El polimorfismo es uno de los pilares del Diseño Orientado a Objetos y se refiere a la capacidad de distintos objetos de responder al mismo mensaje o contrato de forma específica, según su propia implementación. En términos de diseño de software, su objetivo principal es aumentar la flexibilidad del sistema, reducir el acoplamiento y permitir que el código opere sobre abstracciones sin depender de las clases concretas que las implementan. Esta cualidad resulta especialmente valiosa en sistemas complejos, ya que facilita la incorporación de nuevas funcionalidades sin modificar constantemente la lógica existente. En el contexto del Sistema de Turnos Médicos, el polimorfismo se manifiesta de manera clara en los mecanismos de extensibilidad del diseño, donde distintos componentes pueden comportarse de manera uniforme desde el punto de vista del cliente aunque presenten implementaciones diferentes. Desde la perspectiva de los principios SOLID, el polimorfismo está estrechamente vinculado con el Principio de Inversión de Dependencias (DIP), porque permite depender de contratos abstractos en lugar de implementaciones concretas, y también con el Principio Abierto/Cerrado (OCP), ya que facilita la incorporación de nuevas variantes sin alterar el código que ya funciona. En el proyecto, este pilar se relaciona de forma directa con los patrones de diseño aplicados, especialmente con el patrón Observer, donde múltiples observadores distintos pueden recibir la misma notificación y reaccionar según su propia lógica.

## Ejemplo en el proyecto
Un ejemplo claro de polimorfismo en el proyecto es el patrón Observer implementado para las notificaciones de los turnos. En este diseño, la interfaz IObservador define un contrato común mediante el método actualizar(evento: String), mientras que las clases NotificadorEmail, NotificadorSMS y NotificadorWhatsApp implementan ese contrato de manera distinta. Aunque todas ellas responden al mismo mensaje, cada una ejecuta una lógica específica según el canal de comunicación que representa. Desde el punto de vista técnico, este diseño cumple con el pilar del polimorfismo porque el sistema puede tratar a todos los observadores de manera uniforme a través de la abstracción IObservador, sin importar cuál de las clases concretas esté ejecutando la operación. 
La Figura 4 muestra la interfaz IObservador, la clase abstracta Observable, y las clases NotificadorEmail, NotificadorSMS y NotificadorWhatsApp, evidenciando cómo distintas implementaciones responden al mismo contrato

![Figura 4. Polimorfismo en el patrón Observer](image-4.png)

**Figura 4.** Aplicación del principio de polimorfismo mediante la interfaz `IObservador` y sus implementaciones `NotificadorEmail`, `NotificadorSMS` y `NotificadorWhatsApp`, donde distintas clases responden al mismo contrato con comportamientos específicos.

## Ejemplo de código
```java
interface IObservador {
    void actualizar(String evento);
}

class NotificadorEmail implements IObservador {
    public void actualizar(String evento) {
        System.out.println("Enviar email: " + evento);
    }
}

@Override
class NotificadorSMS implements IObservador {
    public void actualizar(String evento) {
        System.out.println("Enviar SMS: " + evento);
    }
}
```

En este fragmento, la interfaz IObservador representa el contrato común que deben cumplir todos los observadores del sistema. Por su parte, NotificadorEmail y NotificadorSMS son clases concretas que implementan ese contrato, pero lo hacen de manera distinta según el canal de notificación que requieren. La aplicación del polimorfismo se evidencia porque el sistema puede tratar a ambas clases mediante la misma interfaz, invocando el método actualizar() sin conocer previamente la implementación concreta que se utilizará. Este ejemplo demuestra correctamente el pilar del polimorfismo porque muestra cómo distintas clases pueden compartir un comportamiento común y, al mismo tiempo, ofrecer respuestas diferenciadas bajo el mismo contrato.
