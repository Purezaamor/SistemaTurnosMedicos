# Informe Técnico: Patrón de Diseño Creacional - Factory Method

## 1. Introducción a los Patrones Creacionales y su relación con SOLID
Los patrones creacionales abstraen el proceso de instanciación de objetos. Ayudan a que un sistema sea independiente de cómo se crean, componen y representan sus objetos. 
Su relación con los principios SOLID es directa:
* **SRP (Responsabilidad Única):** Extrae el comportamiento de creación de objetos de las clases de negocio principales (como los controladores).
* **OCP (Abierto/Cerrado):** Permite introducir nuevos tipos de productos (en este caso, nuevas modalidades de Turnos) al sistema sin romper ni modificar el código cliente existente.

## 2. Propósito y Tipo del Patrón Seleccionado
* **Patrón:** Factory Method (Método de Fábrica).
* **Tipo:** Creacional.
* **Propósito:** Definir una interfaz para crear un objeto, pero dejar que las subclases decidan qué clase instanciar. Permite que una clase delegue la instanciación a las subclases.

## 3. Motivación Detallada del Problema y la Solución
* **Problema:** En el diseño inicial unificado, el `ControladorTurnos` creaba instancias directas de la clase concreta `Turno`. Esto generaba un acoplamiento rígido. Si el centro médico requería incorporar "Turnos de Telemedicina" o "Sobretornos de Emergencia" con atributos y flujos de datos particulares, se debía modificar el núcleo de operaciones del controlador, aumentando el riesgo de efectos colaterales no deseados.
* **Solución:** Introducir una estructura abstracta de creación (`CreadorTurnos`) y derivar fábricas concretas para cada subtipo de turno. El controlador ahora interactúa únicamente con interfaces/clases abstractas, logrando un desacoplamiento absoluto de los componentes.

## 4. Estructura de Clases con Diagrama UML
El diseño detallado del patrón se encuentra guardado en el repositorio y puede ser visualizado directamente en:
* Archivo fuente: [`diagramas/01-diagrama-clases/01-patron-creacional-factory.puml`](../../diagramas/01-diagrama-clases/01-patron-creacional-factory.puml)
* Diagrama exportado: [`diagramas/01-diagrama-clases/01-patron-creacional-factory.png`](../../diagramas/01-diagrama-clases/01-patron-creacional-factory.png)

## 5. Justificación Técnica de la Solución Propuesta
La implementación de Factory Method se justifica debido a que garantiza la escalabilidad del negocio tecnológico frente a futuras variantes de atención hospitalaria. Se reduce la complejidad ciclomática del controlador (eliminando bloques condicionales de tipo `if/switch` basados en strings para determinar qué tipo de objeto construir) y se asegura que la arquitectura respete de extremo a extremo el Principio de Inversión de Dependencias (DIP).