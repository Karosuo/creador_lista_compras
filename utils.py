import yaml
from os import path
import pathlib
from os.path import abspath, join

SRC_BASE_PATH = pathlib.Path(__file__).parent.resolve()

def suma_ingredientes_recetas(lista_recetas):
    """
    Suma los ingredientes de todas las recetas y los pone en una lista de diccionarios con el mismo
    formato que tienen refri.yaml y productos_base.yaml
    
    Parameters
    ----------
    lista_recetas : list
        Lista de diccionarios con el formato
        - nombre: ""
          ingredientes:
          - nombre: ""
            cantidad: n
          cantidad: n
        Que serán mezclados, todos los ingredientes con el mismo nombre, se sumarán sus cantidades y se multiplicarán por la cantidad
        indicada de recetas
            
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