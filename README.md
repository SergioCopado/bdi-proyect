# Proyecto IBD
Grupo 4 - Carla Barbero, Sergio Copado, Rocío Frontaura y Elia González de Heredia

## *PARTE 1*
## Descripción detallada de la infraestructura

En primer lugar, se usará una API para la obtención de datos.

**USO DE LA API:** 

Se trata de una API diseñada para extraer información de libros de diversos géneros literarios (*https://openlibrary.org/*). Esta API descarga archivos JSON que contienen información diversa y detallada de cada libro, como su título, autor, descripción, año de publicación o plataformas de compra disponibles.


**INFRAESTRUCTURA:**

La infraestructura propuesta se basa en el uso de Docker, aprovechando los conocimientos sobre contenedores y volúmenes adquiridos en el aula. Esta plataforma se empleará para gestionar la aplicación y sus dependencias de forma eficiente.

Docker proporciona un entorno aislado y portable para ejecutar la aplicación, lo que facilita su despliegue en diferentes entornos. La capacidad de empaquetar la aplicación y sus dependencias en contenedores ligeros asegura la portabilidad y consistencia del entorno de ejecución. Cada contenedor opera en un entorno aislado propio, asegurando que el rendimiento de la aplicación no se vea afectado por otras instancias en ejecución. Los archivos JSON generados por la aplicación (*data_extractor.py*) se almacenan en un volumen Docker, garantizando su persistencia incluso después de la detención de los contenedores. El uso de volúmenes también permite la compartición de datos entre contenedores distintos, lo que facilita la colaboración entre componentes de la aplicación, como la extracción y el procesamiento de datos.

En cuanto a la configuración del despliegue en un entorno virtualizado, se establecerán los volúmenes necesarios para almacenar y persistir los archivos JSON generados por la aplicación, estos se configurarán de manera que interactúen eficientemente entre sí, facilitando así la extracción y almacenamiento de datos en crudo. 

 A continuación se detalla como se han considerados los retos/requisitos para el manejo de Big Data.

**DATOS**

La estrategia actual de ingesta de datos masivos se fundamenta en realizar solicitudes HTTP a una fuente externa (*Open Library*) para extraer datos. En cuanto al almacenamiento en crudo de datos, la solución actual emplea volúmenes Docker para almacenar los archivos JSON generados por la aplicación. 

En lo que respecta a la garantía de disponibilidad y escalabilidad de los datos: 

•	*Disponibilidad:* se implementan copias del volumen en diversos nodos del clúster para asegurar la continuidad de los datos en caso de fallo de un nodo o contenedor. Esto garantiza que si un nodo experimenta un fallo, los datos permanecerán intactos y las demás instancias continuarán funcionando de manera independiente.

•	*Escalabilidad:* se alcanza aumentando el número de réplicas o añadiendo nuevos nodos al clúster. Aunque la aplicación se limite a la descarga de datos de cuatro géneros literarios por tiempo de ejecución, es posible ampliar la variedad de géneros obteniendo un mayor número de archivos. 

**CALIDAD**

El empleo de volúmenes Docker conlleva una serie de ventajas en diferentes aspectos:

•	*Eficiencia*: utilizar un volumen Docker es eficiente en términos de recursos, ya que permite que los datos persistan más allá de la vida del contenedor sin necesidad de replicar el almacenamiento dentro de cada contenedor. Esto reduce la sobrecarga de almacenamiento y el consumo de recursos en comparación con el almacenamiento en el sistema de archivos del contenedor. 

•	*Escalabilidad*: la elección de un volumen Docker como almacenamiento facilita la escalabilidad horizontal, puesto que los datos almacenados en el volumen pueden ser accesibles por múltiples contenedores. Esto facilita el escalado horizontal de la aplicación, ya que se pueden añadir contenedores que utilicen el mismo volumen si fuera necesario por el volumen de datos manejados. 

•	*Fiabilidad*: implementar estrategias de respaldo y restauración para el volumen mejora la fiabilidad del sistema, asegurando la protección de los datos contra pérdidas o corrupción. Aunque Docker no proporciona una solución integrada por defecto para estas tareas, ofrece al usuario varias alternativas. Una opción viable son las Docker Volume Backup Tools, diseñadas específicamente para realizar respaldos y restauraciones de datos almacenados en volúmenes de Docker. Estas herramientas permiten a los usuarios crear copias de seguridad de datos persistentes dentro de los contenedores Docker y restaurarlos según sea necesario.

•	*Gestión de carga*: distribuir la carga de trabajo entre múltiples contenedores que utilizan el mismo volumen Docker ayuda a equilibrar la carga y evitar la congestión en un solo nodo. Esto mejora la gestión de la carga y garantiza un rendimiento óptimo de la aplicación, especialmente en entornos de alta demanda.


**ALCANCE**

La implementación de esta arquitectura supone la renuncia de ciertos aspectos del Big Data, como son el volumen y la velocidad de los datos. A continuación, se detalla cómo influyen cada una de las cinco dimensiones en nuestra aplicación. 

• *Volumen*: los volúmenes Docker pueden no ser la solución más idónea para manejar grandes volúmenes de datos, ya que su capacidad está restringida por el espacio disponible en el sistema de archivos del host.

• *Velocidad*: la velocidad de acceso a los datos puede verse afectada; aunque los volúmenes Docker son conocidos por su eficiencia y baja sobrecarga, pueden introducir cierta latencia en el acceso a los datos. Esto significa que puede haber una pequeña demora adicional al acceder a los datos almacenados en un volumen de Docker en comparación con el acceso directo desde el sistema de archivos del host.

• *Variedad*: la variedad se determina en función a los distintos tipos de datos guardados en los archivos JSON obtenidos. En esta aplicación, disponemos de diversas categorías dentro de cada archivo en las que encontramos datos de tipo string, de tipo int y de tipo booleano.

• *Valor*: el valor de los datos radica en su capacidad para proporcionar información útil a los usuarios. En el caso de los archivos JSON descargados con la información de distintos libros, estos proporcionan información como las plataformas donde adquirirlos, los autores, el año de publicación o el género/s literarios a los que pertenecen. 

• *Veracidad*: la veracidad de los datos puede verse comprometida debido a que, sin un procesamiento previo, no se puede garantizar la integridad y precisión de los archivos almacenados en los volúmenes Docker, a menos que se conozca la fuente de la que provienen y esta sea fiable y/o oficial. En nuestro caso, se trata de una fuente pública y gratuita utilizada por numerosos usuarios y que contiene información de diversos libros, por lo que hemos considerado que es una fuente fiable.

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

**NOTA:** El archivo 'data_extractor.py' se ha limitado para que descargue archivos JSON de un solo género literario (horror) para que el tiempo de ejecución al probarlo no sea elevado. Para descargar todos los datos, se pueden ampliar los géneros con otros como science fiction, thriller y action. Este conjunto de géneros se descarga aproximadamente en tres horas. Si se quisiera ampliar aún más el volumen de los datos de descarga, hay otros géneros a añadir como romance, fantasy o mystery. 


## *PARTE 2*

## Procesamiento y almacenamiento

**DESCARGA DE LOS DATOS**

Para la obtención de los datos, se ha tenido que reestructurar la infraestructura inicial debido a que el volumen que se utilizó no estaba definido de manera que el resto de los servicios pudieran acceder a él. Es por eso por lo que se ha vuelto a realizar la descarga de los datos, pero con algunas alteraciones para que no conlleve un tiempo excesivo.

La ejecución de data_extractor.py está limitada a dos minutos, debido a que sino el servidor de jupyter se satura y no funciona de manera óptima. Además, de esta forma, el procesamiento, almacenamiento y visualización posteriores no llevan tanto tiempo. El comando que se ha añadido al docker-compose.yaml es:
```sh
command: bash -c "timeout 2m python -u data_extractor.py"
```
Si se quisiera realizar con todos los datos, simplemente habría que eliminar esta línea.
Los datos se almacenan en el volumen shared-workspace, definido en el compose, de forma que son accesibles por el resto de los servicios que usaremos en el proceso.

**PROCESAMIENTO**

Una vez que tenemos los datos en crudo descargados en el volumen compartido shared-workspace, necesitamos procesarlos. Este procesamiento se realizará con Spark a través del jupyter notebook definido como servicio. Para utilizar el notebook es necesario acceder al http://localhost:8889
El primer paso del procesamiento será crear una sesión en Spark. De esta forma, podremos usar las operaciones pertinentes de este servicio para limpiar y gestionar nuestros datos. 

Spark proporciona ventajas para el procesamiento, algunas de ellas son la velocidad con la que realiza las tareas, el procesamiento en memoria y un motor de ejecución optimizado. Además, aporta una gran flexibilidad puesto que Spark puede manejar una gran variedad de formatos de los datos (JSON, Parquet, CSV, …) y facilita la ejecución de consultas sobre Dataframes/Datasets. También cabe destacar el hecho de que permite distribuir el procesamiento de datos a través de múltiples nodos en un clúster lo que supone escalabilidad horizontal y permite manejar grandes volúmenes de datos de manera eficiente realizando operaciones de procesamiento en paralelo.
A continuación, hemos obtenido los campos contenidos en los archivos json, así como los campos que son comunes en todos los archivos descargados. Los archivos contienen mucha información, pero el objetivo será quedarnos con aquella que pueda resultar interesante al usuario.
Una vez que tenemos la sesión iniciada en Spark y sabemos cuáles son los campos comunes, seleccionamos los campos más relevantes de nuestros datos como el título del libro, el nombre del autor, el año de publicación, el idioma en el que está disponible, el género, así como número de páginas, el id de amazon en caso de querer comprarlo online y el promedio de votación (del 1 al 5). Estas características aportan información relevante para cada libro además de proporcionar información útil al usuario.
Una vez que tenemos las características, eliminamos las filas que sean nulas completamente ya que no aportan valor y guardamos en nuestro volumen compartido el nuevo Dataframe ya procesado y listo para ser almacenado. 

**ALMACENAMIENTO**

En cuanto al almacenamiento, se ha utilizado Elasticsearch principalmente porque es compatible con esquemas de datos flexibles, lo que es útil para datos semiestructurados como archivos json, ya que los datos pueden ser indexados sin necesidad de definir previamente todos los campos y tipos. Además, en cuanto a la velocidad, Elasticsearch está diseñado para la búsqueda y consulta rápida de grandes volúmenes de datos, además de ser flexible soportando consultas complejas incluyendo búsquedas con filtros de campos específicos, agregacione, etc.

Para proceder al almacenamiento, se inicia un cliente de Elasticsearch y se cargan los datos guardados en la etapa de procesamiento. Partimos de un Dataframe de pandas, por lo que lo primero será convertir cada fila en un archivo json. Una vez tenemos el formato adecuado, insertamos los datos en el índice que vamos a utilizar. De esta forma, todos los archivos quedan almacenados en el servicio. 
A partir de este momento, podemos realizar queries para obtener información útil y relevante sobre los documentos guardados. Por ejemplo, se puede sacar el número de documentos que hay por autor, buscar aquellos que estén bien valorados, buscar documentos en el que el título tenga una palabra determinada o buscar los libros disponibles en un idioma en concreto o con un año de publicación específico.
Para este servicio, se define un volumen particular. Esto se debe a que en él vamos a guardar los datos finales a lo que el usuario podrá realizar consultas. De esta forma, garantizamos que los datos no se ven perjudicados por el resto de servicios y procesos que se estén realizando al mismo tiempo. 

**RECURSOS**

En este despliegue, hemos utilizado un único Spark Worker para facilitar el despliegue, dados los recursos limitados de nuestras máquinas host. Además, el volumen de datos procesados en esta fase inicial no ha justificado la necesidad de múltiples Spark Workers.

Sin embargo, Spark permite una escalabilidad horizontal sencilla. En caso de un aumento en el volumen de datos o la necesidad de mejorar el rendimiento, se pueden añadir más Spark Workers. Esto permitiría distribuir las tareas de procesamiento en múltiples nodos, aprovechando al máximo las capacidades de procesamiento distribuido de Spark y mejorando la eficiencia general del sistema.

De manera similar, hemos desplegado un único nodo de Elasticsearch, tal y como hicimos en clase, por razones de simplicidad y limitaciones de recursos. Igualmente, la arquitectura de Elasticsearch permite una fácil escalabilidad a múltiples nodos para manejar mayores volúemnes de datos, aunque esto implicaría gestionar la coordinación entre nodos adicionales. Si se añadiesen más nodos, se podrían habilitar réplicas para proporcionar redundancia y alta disponibilidad, asegurando que los datos permanezcan accesibles incluso en caso de fallo de un nodo.

## Nuevos pasos para el Despliegue

### 1. Clonar el Repositorio
Descargue el repositorio de GitHub y asegúrese de que todos los archivos se encuentren en la misma carpeta:
```sh
git clone https://github.com/SergioCopado/bdi-proyect1.git
cd bdi-proyect1/parte_2
```
### 2. Construir la Imagen Docker
Ejecute el siguiente comando para construir la imagen Docker basada en el Dockerfile proporcionado. Aquí extractor es el nombre de la imagen que se creará:
```sh
docker build -t extractor .
```

### 3. Ejecutar Docker Compose
Levante toda la infraestructura utilizando Docker Compose:
```sh
docker-compose up
```

### 4. Acceder a JupyterLab
Una vez que los contenedores estén en funcionamiento, abra su navegador web y acceda a JupyterLab en la siguiente URL:
```sh
http://localhost:8889
```

### 5. Ejecutar el Cuaderno de Jupyter
En JupyterLab, abra el cuaderno procesamiento_almacenamiento_queries.ipynb. Luego, ejecute las celdas del cuaderno para procesar los datos con Spark y almacenarlos en Elasticsearch.

### 6. Realizar Consultas en Elasticsearch
Después de procesar y almacenar los datos, puede realizar algunas consultas en Elasticsearch como se indica en el cuaderno. 
