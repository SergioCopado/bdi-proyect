import os
import json
import requests
import re

def limpiar_titulo(titulo):
    # Reemplazar espacios con barras bajas
    titulo_limpio = titulo.replace(' ', '_')
    # Eliminar caracteres especiales y espacios adicionales del título
    titulo_limpio = re.sub(r'[^\w\s]', '', titulo_limpio)
    titulo_limpio = re.sub(r'\s+', ' ', titulo_limpio).strip()
    return titulo_limpio

def buscar_libros(parametros):
    url = 'http://openlibrary.org/search.json'
    resultados_totales = 0

    try:
        # Crear la carpeta json si no existe
        if not os.path.exists('json'):
            os.makedirs('json')
            
        # Realizar la primera solicitud para obtener el número total de resultados
        response = requests.get(url, params=parametros)
        data = response.json()

        if response.status_code == 200:
            resultados_totales = data['numFound']
            print(f"Se encontraron un total de {resultados_totales} resultados.")

            # Iterar sobre todas las páginas de resultados
            for pagina in range(1, (resultados_totales // 100) + 2):  # + 2 para asegurarse de obtener la última página
                parametros['page'] = pagina
                response = requests.get(url, params=parametros)
                data = response.json()

                if response.status_code == 200:
                    if data['docs']:
                        for libro in data['docs']:
                            titulo = libro.get('title', 'No disponible')
                            titulo_limpio = limpiar_titulo(titulo)
                            with open(f'/json/{titulo_limpio}.json', 'w', encoding='utf-8') as file:
                                json.dump(libro, file, indent=4)
                    else:
                        print(f"No se encontraron libros en la página {pagina}.")
                else:
                    print(f"No se pudo obtener la página {pagina} de resultados.")
        else:
            print("No se encontraron libros con los criterios especificados.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
parametros_busqueda = {'q': 'horror'}
buscar_libros(parametros_busqueda)