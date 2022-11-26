import yaml
from os import path
import pathlib
from os.path import abspath, join

SRC_BASE_PATH = pathlib.Path(__file__).parent.resolve()

def print_lista_de_compras(lista_compras):
    """
    Parsea la lista recibida por parámetro y la convierte en una secuencia de strings
    divididas por saltos de linea con el siguiente formato}
        cantidad_articulos, nombre_articulo

    
    Parameters
    ----------
    lista_compras : list
        Lista de articulos con sus cantidades (lista de diccionarios), con el formato de refri.yaml        
            
    Returns
    -------
    lista de compras : string
    """
    pass

def suma_listas(*argv):
    """
    Va agregando a una lista nueva los ingredientes/articulos y sus cantidades de cada una de las listas pasadas por parámetro
    Si los nombres de los ingredientes/articulos coinciden, se suman sus cantidades
    
    Parameters
    ----------
    argv : list
        Lista de articulos con sus cantidades (lista de diccionarios), con el formato de refri.yaml        
            
    Returns
    -------
    lista de diccionarios : list
        Lista con el mismo formato que refri.yaml y productos_base.yaml con todos los ingredientes y sus cantidades
        sumadas dependiendo de su aparición en las listas pasadas por parámetro    
    """
    pass

def resta_listas(*argv):
    """
    Va agregando a una lista nueva los ingredientes/articulos y sus cantidades de cada una de las listas pasadas por parámetro
    Si los nombres de los ingredientes/articulos coinciden, se RESTAN sus cantidades
    
    Si la resta de los articulos es <=0, entonces ese artículo no se incluye en la lista final (o se elimina si ya estaba)

    Parameters
    ----------
    argv : list
        Lista de articulos con sus cantidades (lista de diccionarios), con el formato de refri.yaml        
            
    Returns
    -------
    lista de diccionarios : list
        Lista con el mismo formato que refri.yaml y productos_base.yaml con todos los ingredientes y sus cantidades
        RESTADAS dependiendo de su aparición en las listas pasadas por parámetro
    """
    pass

def get_recetas():
    """
    Obtiene una lista de todos los nombres de las recetas que existen en recetas.yaml
    
    Parameters
    ----------
    None 

    Returns
    -------
    Lista de recetas : list
        Lista de los nombres de todas las recetas
    """
    recetas = yaml_to_python(get_src_abspath("recetas.yaml"))
    return [item["nombre"] for _,item in recetas.items()]    

def suma_ingredientes_recetas(lista_recetas):
    """
    Suma los ingredientes de todas las recetas y los pone en una lista de diccionarios con el mismo
    formato que tienen refri.yaml y productos_base.yaml
    
    Parameters
    ----------
    lista_recetas : list
        Lista de diccionarios con el formato de recetas.yaml
        Que serán mezclados, todos los ingredientes con el mismo nombre, se sumarán sus cantidades
        y se multiplicarán por la cantidad indicada de recetas
            
    Returns
    -------
    lista de diccionarios : list
        Lista con el mismo formato que refri.yaml y productos_base.yaml con todos los ingredientes y sus cantidades
        sumadas dependiendo de su aparición en las recetas    
    """
    pass

def yaml_to_python(yaml_fp):
    """
    Lee un archivo yaml y lo parsea usando el paquete 'pyyaml'    
    Parameters
    ----------
    yaml_fp : string
        El filepath del archivo yaml a ser parseado
            
    Returns
    -------
    pyyaml object
        Dictionary if the yaml element is a hash
        List if the yaml element is a list
        NoneType if nothing is in the input file
    Exception
        (FileNotFoundError) If file doesn't exist
        (ScannerError) If the file provided is not parsable, for ex. binary or not yaml
    """
    parsed_yaml = {}
    with open(yaml_fp, 'r') as yaml_file:
        parsed_yaml = yaml.safe_load(yaml_file)

    return parsed_yaml

def get_src_abspath(yaml_name):
    """
    Obtiene la abspath de cualquiera de los archivos yaml en este directorio
    
    Parameters
    ----------
    yaml_name : string
        El nombre del archivo del cual se necesita el abspath
            
    Returns
    -------
    an absolute path : string
        La ruta absoluta (abspath) del archivo yaml dado por yaml_name
    
    Nota:
        No se revisa si la ruta es correcta o no
    """
    return abspath(join(SRC_BASE_PATH, yaml_name))