# IBD - Práctica 1
Primera práctica de la asignatura de Infraestructuras de Big Data

## Descripción detallada de la infraestructura

**USO DE LA API:** 

Se trata de una API diseñada para extraer información de libros de diversos géneros literarios (*https://openlibrary.org/*). Esta API descarga archivos JSON que contienen información detallada de cada libro, como su título, autor, descripción, año de publicación y plataformas de compra disponibles.


**INFRAESTRUCTURA:**

La infraestructura propuesta se basa en el uso de Docker, aprovechando los conocimientos sobre contenedores y volúmenes adquiridos en el aula. Esta plataforma se empleará para gestionar la aplicación y sus dependencias de forma eficiente.

Docker proporciona un entorno aislado y portable para ejecutar la aplicación, lo que facilita su despliegue en diferentes entornos. La capacidad de empaquetar la aplicación y sus dependencias en contenedores ligeros asegura la portabilidad y consistencia del entorno de ejecución. Cada contenedor opera en un entorno aislado propio, asegurando que el rendimiento de la aplicación no se vea afectado por otras instancias en ejecución. Los archivos JSON generados por la aplicación (*data_extractor.py*) se almacenan en un volumen Docker, garantizando su persistencia incluso después de la detención de los contenedores. El uso de volúmenes también permite la compartición de datos entre contenedores distintos, lo que facilita la colaboración entre componentes de la aplicación, como la extracción y el procesamiento de datos.

En cuanto a la configuración del despliegue en un entorno virtualizado, se establecerán los volúmenes necesarios para almacenar y persistir los archivos JSON generados por la aplicación. Los contenedores se configurarán de manera que interactúen eficientemente entre sí, facilitando así la extracción, procesamiento y almacenamiento de datos en crudo. 
 

**Datos:**

•	Disponibilidad:
Para garantizar la disponibilidad de los datos, se pueden crear réplicas del volumen en varios nodos del clúster, de forma que los datos estén disponibles, aunque alguno de los nodos falle. En este caso, el servicio será desplegado en un modo replicado con tres réplicas.








•	Escalabilidad:
En la aplicación, se ha limitado la descarga de los datos a 4 géneros literarios por tiempo de ejecución, sin embargo, se pueden ampliar los géneros obteniendo un mayor número de archivos. Algunos ejemplos de esto son romance, fantasy….

**Calidad:**

•	Eficiencia:
Utilizar un volumen Docker es eficiente en términos de recursos, ya que permite que los datos persistan más allá de la vida del contenedor sin necesidad de replicar el almacenamiento dentro de cada contenedor. Esto reduce la sobrecarga de almacenamiento y el consumo de recursos en comparación con el almacenamiento en el sistema de archivos del contenedor. 

•	Escalabilidad:
La elección de un volumen de Docker como almacenamiento facilita la escalabilidad horizontal, ya que los datos almacenados en el volumen pueden ser accesibles para múltiples contenedores. Esto permite que se escale fácilmente agregando más contenedores que acceden a un mismo volumen. 

•	Fiabilidad:
El uso de estrategias de respaldo y restauración para el volumen mejora la fiabilidad del sistema al garantizar que los datos estén protegidos contra pérdidas o corrupción. ***Investigar si se implementa o Docker lo tiene por defecto.*** 
Docker no incluye una solución integrada por defecto para realizar respaldo y restauración, sin embargo, ofrece al usuario diversas alternativas para respaldar y restaurar datos almacenados en volúmenes. Una opción viable son las Docker Volume Backup Tools ***(Investigar las Docker Volume Backup Tools)*** , herramientas diseñadas específicamente con el propósito de realizar respaldos y restauraciones de datos almacenados en volúmenes de Docker. Estas herramientas posibilitan a los usuarios la creación de copias de seguridad de datos persistentes dentro de los contenedores Docker y, en caso necesario, la restauración de dichos datos en un momento posterior.

•	Gestión de carga:
Distribuir la carga de trabajo entre múltiples contenedores que utilizan el mismo volumen de Docker ayuda a equilibrar la carga y evitar la congestión en un solo nodo. Esto mejora la gestión de la carga y garantiza un rendimiento óptimo de la aplicación, especialmente en entornos de alta demanda.
***Investigar cómo implementarlo y si es necesario.***

•	Buscar más

**Alcance:**

Al utilizar un volumen Docker como forma de almacenamiento de datos, puede haber ciertas limitaciones en algunas dimensiones de Big Data. 

En primer lugar, el volumen Docker puede no ser una solución óptima en cuestiones de volúmenes de datos muy elevados. Los volúmenes de Docker están limitados por el espacio de almacenamiento disponible en el sistema de archivos del host.
En segundo lugar, la velocidad podría verse afectada en cierto modo ya que, aunque el volumen de Docker es conocido por su eficiencia y baja sobrecarga, puede introducir una cierta latencia en el acceso a los datos.
A pesar de sacrificar el volumen y la velocidad de los datos, esto simplifica la implementación de la infraestructura en varios aspectos. Uno de ellos es la facilidad de configuración y gestión, la implementación de los volúmenes de Docker es sencilla comparado con otras soluciones más complejas. También proporciona compatibilidad y portabilidad, Docker es compatible con múltiples entornos y un volumen de Docker asegura la portabilidad de la aplicación facilitando su despliegue en diferentes entornos sin necesidad de realizar cambios en la configuración. Por último, conlleva una menor sobrecarga de recursos, los volúmenes de Docker introducen una sobrecarga mínima priorizando la eficiencia y la optimización de recursos. 

## Guía de Despliegue para la Infraestructura

Esta guía proporciona los pasos necesarios para desplegar la infraestructura de la aplicación de manera rápida y eficiente en cualquier entorno.

### Pasos para el Despliegue

1. **Abrir la Terminal:**
   Abra la terminal o línea de comandos en el sistema operativo correspondiente.

2. **Modificar el Archivo Docker Compose:**
   Modifique el archivo `docker-compose.yml`, proporcionando la ruta en el sistema de archivos local donde desea que Docker monte el volumen `/json` del contenedor. Esto se puede realizar utilizando un editor de texto o una herramienta de línea de comandos.

3. **??????** **Construir la Imagen Docker:**  
   Ejecute el siguiente comando para construir la imagen Docker basada en el Dockerfile proporcionado:

   ```bash
   docker build -t extractor .

4. **Ejecutar Docker Compose:** Por último, ejecute el siguiente comando para levantar toda la infraestructura utilizando Docker Compose:

   ```bash
   docker compose up
   ```

Con estos pasos, se ha desplegado con éxito la infraestructura de la aplicación, ya está lista para comenzar a utilizarla. 



