# bdi-proyect1
The first proyect of the Big Data Infrastructure subject

# Practice 1: Container-based Infrastructure

1. **Detailed Description** of the infrastructure, justifying its design.

    * Identify and describe the key components of the infrastructure, including the container services to be used.

        - Data Extraction: A Docker container will be used to act as a data extractor. This container will obtain TXT files from the specified source. It will be a script or application that downloads or copies TXT files from the source and stores them locally in the container's file system.

        - Storage System: We can utilize a simple storage system to store the raw files. It can be a local file system within the container or a shared volume mounted in the container.

    * Explain how each component contributes to efficient data management and how they integrate with each other.

2. Brief **guide** to facilitate deployment in any environment.


INFORMACIÓN RECOPILADA:

**Uso de la API:** 
Se trata de una API que permite extraer información de libros de distintos géneros literarios. Se descargan archivos JSON que contienen distintas características de cada libro como el título, el autor, una descripción, el año de publicación o las plataformas de compra en las que se pueden obtener.
Almacenamiento: Se almacenarán los datos dentro de un volumen creado en un contenedor de Docker.

**Infraestructura:**
Para la infraestructura se utilizarán los conocimientos sobre contenedores y volúmenes de Docker implementados en clase. 
Docker contiene y ejecuta la aplicación creada en un entorno aislado y portable, permite empaquetar la aplicación y todas sus dependencias en un contenedor ligero de forma que se garantice la portabilidad en cualquier entorno en el que Docker esté instalado. Además, cada contenedor tiene un entorno aislado propio, lo que garantiza que su funcionamiento no afectará a otras aplicaciones que se ejecuten en el mismo sistema.
En cuanto al volumen utilizado, donde se guardarán los archivos JSON generados por la aplicación, permite el acceso y persistencia de los datos más allá del tiempo de vida del contenedor. En nuestro caso de almacenamiento de datos en crudo, se almacenarán los datos en un volumen para garantizar su persistencia, ya que posteriormente se necesitará acceder a ellos para procesarlos. Además, el uso de volúmenes permite compartir datos entre diferentes contenedores, por ejemplo, si tenemos una aplicación que extrae los datos y otra que los procesa. 

**Datos:**
•	Disponibilidad
Para garantizar la disponibilidad de los datos, se pueden crear réplicas del volumen en varios nodos del clúster, de forma que los datos estén disponibles, aunque alguno de los nodos falle. Esto hay que mirarlo porque habría que implementarlo.

•	Escalabilidad
En la aplicación, se ha limitado la descarga de los datos a 4 géneros literarios por tiempo de ejecución, sin embargo, se pueden ampliar los géneros obteniendo un mayor número de archivos. Algunos ejemplos de esto son romance, fantasy….

**Calidad:**
•	Eficiencia
Utilizar un volumen Docker es eficiente en términos de recursos, ya que permite que los datos persistan más allá de la vida del contenedor sin necesidad de replicar el almacenamiento dentro de cada contenedor. Esto reduce la sobrecarga de almacenamiento y el consumo de recursos en comparación con el almacenamiento en el sistema de archivos del contenedor. 

•	Escalabilidad
La elección de un volumen de Docker como almacenamiento facilita la escalabilidad horizontal, ya que los datos almacenados en el volumen pueden ser accesibles para múltiples contenedores. Esto permite que se escale fácilmente agregando más contenedores que acceden a un mismo volumen. 

•	Fiabilidad
El uso de estrategias de respaldo y restauración para el volumen mejora la fiabilidad del sistema al garantizar que los datos estén protegidos contra pérdidas o corrupción. ***Investigar si se implementa o Docker lo tiene por defecto.***

•	Gestión de carga
Distribuir la carga de trabajo entre múltiples contenedores que utilizan el mismo volumen de Docker ayuda a equilibrar la carga y evitar la congestión en un solo nodo. Esto mejora la gestión de la carga y garantiza un rendimiento óptimo de la aplicación, especialmente en entornos de alta demanda.
***Investigar cómo implementarlo y si es necesario.***

•	Buscar más

**Alcance:**
Al utilizar un volumen Docker como forma de almacenamiento de datos, puede haber ciertas limitaciones en algunas dimensiones de Big Data. 
En primer lugar, el volumen Docker puede no ser una solución óptima en cuestiones de volúmenes de datos muy elevados. Los volúmenes de Docker están limitados por el espacio de almacenamiento disponible en el sistema de archivos del host.
En segundo lugar, la velocidad podría verse afectada en cierto modo ya que, aunque el volumen de Docker es conocido por su eficiencia y baja sobrecarga, puede introducir una cierta latencia en el acceso a los datos.
A pesar de sacrificar el volumen y la velocidad de los datos, esto simplifica la implementación de la infraestructura en varios aspectos. Uno de ellos es la facilidad de configuración y gestión, la implementación de los volúmenes de Docker es sencilla comparado con otras soluciones más complejas. También proporciona compatibilidad y portabilidad, Docker es compatible con múltiples entornos y un volumen de Docker asegura la portabilidad de la aplicación facilitando su despliegue en diferentes entornos sin necesidad de realizar cambios en la configuración. Por último, conlleva una menor sobrecarga de recursos, los volúmenes de Docker introducen una sobrecarga mínima priorizando la eficiencia y la optimización de recursos. 
