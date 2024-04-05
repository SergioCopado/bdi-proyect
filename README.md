# IBD - Práctica 1

## Descripción detallada de la infraestructura

**USO DE LA API:** 

Se trata de una API diseñada para extraer información de libros de diversos géneros literarios (*https://openlibrary.org/*). Esta API descarga archivos JSON que contienen información detallada de cada libro, como su título, autor, descripción, año de publicación o plataformas de compra disponibles.


**INFRAESTRUCTURA:**

La infraestructura propuesta se basa en el uso de Docker, aprovechando los conocimientos sobre contenedores y volúmenes adquiridos en el aula. Esta plataforma se empleará para gestionar la aplicación y sus dependencias de forma eficiente.

Docker proporciona un entorno aislado y portable para ejecutar la aplicación, lo que facilita su despliegue en diferentes entornos. La capacidad de empaquetar la aplicación y sus dependencias en contenedores ligeros asegura la portabilidad y consistencia del entorno de ejecución. Cada contenedor opera en un entorno aislado propio, asegurando que el rendimiento de la aplicación no se vea afectado por otras instancias en ejecución. Los archivos JSON generados por la aplicación (*data_extractor.py*) se almacenan en un volumen Docker, garantizando su persistencia incluso después de la detención de los contenedores. El uso de volúmenes también permite la compartición de datos entre contenedores distintos, lo que facilita la colaboración entre componentes de la aplicación, como la extracción y el procesamiento de datos.

En cuanto a la configuración del despliegue en un entorno virtualizado, se establecerán los volúmenes necesarios para almacenar y persistir los archivos JSON generados por la aplicación. Los contenedores se configurarán de manera que interactúen eficientemente entre sí, facilitando así la extracción, procesamiento y almacenamiento de datos en crudo. 
 

**DATOS**

La estrategia actual de ingesta de datos masivos se fundamenta en realizar solicitudes HTTP a una fuente externa (*Open Library*) para extraer datos. En cuanto al almacenamiento en crudo de datos, la solución actual emplea volúmenes Docker para almacenar los archivos JSON generados por la aplicación. 

En lo que respecta a la garantía de disponibilidad y escalabilidad de los datos: 

•	*Disponibilidad:* se implementan copias del volumen en diversos nodos del clúster para asegurar la continuidad de los datos en caso de fallo de un nodo o contenedor. Esto garantiza que si un nodo experimenta un fallo, los datos permanecerán intactos y las demás instancias continuarán funcionando de manera independiente.

•	*Escalabilidad:* se alcanza aumentando el número de réplicas o añadiendo nuevos nodos al clúster. Aunque la aplicación se limite a la descarga de datos de cuatro géneros literarios por tiempo de ejecución, es posible ampliar la variedad de géneros obteniendo un mayor número de archivos. Algunos ejemplos de géneros literarios con los que se podría ampliar el número de archivos son romance o fantasy. 

**CALIDAD**

El empleo de volúmenes Docker conlleva una serie de ventajas en diferentes aspectos:

•	*Eficiencia*: utilizar un volumen Docker es eficiente en términos de recursos, ya que permite que los datos persistan más allá de la vida del contenedor sin necesidad de replicar el almacenamiento dentro de cada contenedor. Esto reduce la sobrecarga de almacenamiento y el consumo de recursos en comparación con el almacenamiento en el sistema de archivos del contenedor. 

•	*Escalabilidad*: la elección de un volumen Docker como almacenamiento facilita la escalabilidad horizontal, puesto que los datos almacenados en el volumen pueden ser accesibles para múltiples contenedores. Esto facilita el escalado horizontal de la aplicación, ya que se pueden añadir contenedores que utilicen el mismo volumen si fuera necesario por el volumen de datos manejados. 

•	*Fiabilidad*: implementar estrategias de respaldo y restauración para el volumen mejora la fiabilidad del sistema, asegurando la protección de los datos contra pérdidas o corrupción. Aunque Docker no proporciona una solución integrada por defecto para estas tareas, ofrece al usuario varias alternativas. Una opción viable son las Docker Volume Backup Tools, diseñadas específicamente para realizar respaldos y restauraciones de datos almacenados en volúmenes de Docker. Estas herramientas permiten a los usuarios crear copias de seguridad de datos persistentes dentro de los contenedores Docker y restaurarlos según sea necesario.

•	*Gestión de carga*: distribuir la carga de trabajo entre múltiples contenedores que utilizan el mismo volumen Docker ayuda a equilibrar la carga y evitar la congestión en un solo nodo. Esto mejora la gestión de la carga y garantiza un rendimiento óptimo de la aplicación, especialmente en entornos de alta demanda.


**ALCANCE**

La implementación de esta arquitectura conlleva la renuncia a ciertos aspectos del Big Data.

• *Volumen*: los volúmenes Docker pueden no ser la solución más idónea para manejar grandes volúmenes de datos, ya que su capacidad está restringida por el espacio disponible en el sistema de archivos del host.

• *Velocidad*: la velocidad de acceso a los datos puede verse afectada; aunque los volúmenes Docker son conocidos por su eficiencia y baja sobrecarga, pueden introducir cierta latencia en el acceso a los datos. Esto significa que puede haber una pequeña demora adicional al acceder a los datos almacenados en un volumen de Docker en comparación con el acceso directo desde el sistema de archivos del host.

• *Variedad*: la variedad se determina en función a los distintos tipos de datos guardados en los archivos JSON obtenidos. En esta aplicación, disponemos de diversas categorías dentro de cada archivo en las que encontramos datos de tipo string, de tipo int y de tipo booleano.

• *Valor*: el valor de los datos radica en su capacidad para proporcionar información útil a los usuarios. En el caso de los archivos JSON descargados con la información de distintos libros, estos proporcionan información como las plataformas donde adquirirlos, los autores, el año de publicación o el género/s literarios a los que pertenecen. 

• *Veracidad*: la veracidad de los datos puede verse comprometida debido a que, sin un procesamiento previo, no se puede garantizar la integridad y precisión de los archivos almacenados en los volúmenes Docker.

A pesar de estas limitaciones en términos de volumen y velocidad de los datos, la elección de utilizar volúmenes Docker simplifica la implementación de la infraestructura en varios aspectos. Por un lado, ofrece facilidad en la configuración y gestión, siendo su implementación más sencilla en comparación con otras soluciones más complejas. Además, proporciona compatibilidad y portabilidad, ya que Docker es compatible con múltiples entornos, y un volumen Docker garantiza la portabilidad de la aplicación, facilitando su despliegue en diferentes entornos sin necesidad de realizar cambios significativos en la configuración. Por último, implica una menor sobrecarga de recursos, ya que los volúmenes Docker introducen una sobrecarga mínima, priorizando la eficiencia y la optimización de recursos.

## Guía de Despliegue para la Infraestructura

Esta guía proporciona los pasos necesarios para desplegar la infraestructura de la aplicación de manera rápida y eficiente en cualquier entorno.

### Pasos para el Despliegue

1. **Descargar el repositorio de GitHub y asegurarse de que todos los archivos se encuentran en la misma carpeta:**
    ```bash
   git clone https://github.com/SergioCopado/bdi-proyect1.git
   ```
    
2. **Abrir la Terminal:**
   Abra la terminal o línea de comandos en el sistema operativo correspondiente. Acceda en la terminal a la carpeta donde se han guardado los documentos descargados.

3. **Construir la Imagen Docker:**
   Ejecute el siguiente comando para construir la imagen Docker basada en el Dockerfile proporcionado, donde *extractor* es el nombre de la imagen que se creará:

   ```bash
   docker build -t extractor .
   ```

4. **Ejecutar Docker Compose:**
   Ejecute el siguiente comando para levantar toda la infraestructura utilizando Docker Compose:

   ```bash
   docker-compose up
   ```

Con estos pasos, se ha desplegado con éxito la infraestructura de la aplicación; ya está lista para comenzar a utilizarla. Para comprobar que ha funcionado correctamente, acceda al directorio especificado para crear la carpeta '/json' y verifique que se encuentran los archivos JSON con la información de los libros descargados.


