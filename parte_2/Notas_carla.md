He conseguido que los datos se suban desde el volumen en Spark y después en Elasticsearch. 

Para usarlo necesitais meter la carpeta data en el mismo sitio donde descargueis los archivos que he dejado. Además, he limitado la descarga de datos a dos minutos que salen uno 2400. Con muchos datos peta y Carlos dijo que podíamos limitarlo. 

La descarga de datos hay que hacerla otra vez porque nosotros no habíamos definido un volumen como tal en docker, por eso no aparecia en el apartado de volúmenes. De esta forma se crea un volumen compartido entre todo. 
