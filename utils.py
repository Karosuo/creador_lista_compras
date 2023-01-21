import yaml
from os import path
import pathlib
from os.path import abspath, join

SRC_BASE_PATH = pathlib.Path(__file__).parent.resolve()

def suma_listas(*argv):
    """
    Mezcla todas las listas que se pasen como parámetro
    y luego suma las cantidades de los articulos compartidos entre las listas    

    Parameters
    ----------
    argv : list
        lista de diccionarios con el formato de refri.yaml

    Returns
    -------
    Lista mezclada de articulos con cantidades sumadas : dict                
    """
    lista_mezclada = {}
    for c_list in argv:
        lista_mezclada = lista_mezclada | c_list

    lista_mezclada_sumada = {}
    for articulo, _ in lista_mezclada.items():
        for c_list in argv:
            if not lista_mezclada_sumada.get(articulo):
                lista_mezclada_sumada[articulo] = dict(lista_mezclada[articulo])
                lista_mezclada_sumada[articulo]["cantidad"] = float(0)
            
            if c_list.get(articulo):
                lista_mezclada_sumada[articulo]["cantidad"] = float(lista_mezclada_sumada[articulo]["cantidad"]) + float(c_list[articulo]["cantidad"])
    return lista_mezclada_sumada


def resta_listas(lista_A, lista_B):
    """
    Resta las cantidades de los articulos en la lista_B de la lista_A (lista_A - lista_B)

    La resta solo ocurre si el artículo de la lista_A existe en la lista_B, para poder obtener ambos factores de la operación
    Si un articulo en lista_A no existe en lista_B, se ignorará la operación
    Si un artículo en la lista_B no existe en la lista_A, ni siquiera se buscará porque se está usando lista_A como referencia de llaves de búsqueda

    ¡Importante!
    Si la resta (lista_A - lista_B) <= 0, ese artículo no será agregado a la lista final que la función regrese    
    
    Parameters
    ----------
    lista_A : dict
        Lista de la que se van a restar las cantidades de los articulos y de la que se usarán las llaves de búsqueda
    lista_B : dict
        Lista que proporcionará las cantidades a restar de los articulos

    Returns
    -------
    lista_A con las cantidades de lista_B restadas: dict     
    """
    lista_restada = dict(lista_A)
    for articulo, detalles in lista_restada.items():
        if lista_B.get(articulo):
            restaAB = float(lista_restada[articulo]["cantidad"]) - float(lista_B[articulo]["cantidad"])
            lista_restada[articulo]["cantidad"] = restaAB                
    return lista_restada

   
def mezcla_listas(*argv):
    """
    Mezcla todas las listas que se pasen por parámetro
    Nota que es una lista de diccionarios python, no una lista de listas
    Se usa la palabra "lista", debido a que cada diccionario representa una lista de artículos
    
    ¡Importante!
    El diccionario que está en argv[0] se toma como el base, así que se va a mezclar al final para
    que sus valores sean los que prevalezcan.
    Esto tomando en cuenta que la mezcla con el operador "|" reemplaza los valores de la lista en la izquierda,
    por los de la derecha
    ex.
        dictA | dictB, tiene como efecto que los valores de dictB prevalezcan sobre los de A en las propiedades compartidas

    Parameters
    ----------
    argv : list
        lista de diccionarios con el formato de refri.yaml

    Returns
    -------
    Lista mezclada de articulos : dict
        Se mezclan las listas usando el operador "|"        
    """
    lista_mezclada = {}
    for c_list in argv:
        lista_mezclada = lista_mezclada | c_list
    return lista_mezclada

def python_to_yaml(yaml_fp, data_object):
    """
    Escribe una lista de diccionarios python en un archivo de texto en formato YAML
    en el nombre y path del archivo pasado por parámetro

    Es un wrapper de la función safe_dump() de PyYaml
    
    Para más detalles, ver https://pyyaml.org/wiki/PyYAMLDocumentation 
    ----------
    yaml_fp : string
        El filepath del archivo que será escrito en formato yaml        
    
    data_object : 
        Datos que se van a convertir a YAML en el archivo

    Returns
    -------
        No return

    Exception
        (FileNotFoundError) If file doesn't exist    
    """
    parsed_yaml = {}
    with open(yaml_fp, 'w') as yaml_file:
        yaml.dump(data=data_object, stream=yaml_file, encoding="utf-8", indent=2)

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

def subcommand(args=[], parent=None, subcmd_desc=""):
    '''
    Abstraction of a subparser to use as a decorator
    Based on https://mike.depalatis.net/blog/simplifying-argparse.html
    
    Parameters
    ----------
    args : tuple (or list)
        Espera una tupla (o lista de 2 elementos), el primero es una lista y el segundo un diccionaro
        Esto para poder pasar un modelo de parameteros como *args,**kargs
    parent: subparser
        Subparser generado por ArgumentParser().add_subparsers()
    subcmd_desc: string
        El texto que se va a mostrar como descripción en la ayuda para el sub comando en cuestión
            
    Returns
    -------
    function reference
        La referencia a la función interna "decorator"            
    '''
    def decorator(func):
        parser = parent.add_parser(name=func.__name__, help=subcmd_desc)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
    return decorator

def arguments(*name_or_flags, **kwargs):    
    '''
    Convierte el formato *args,**kargs en el formato ([*name_or_flags], kwargs) necesario
    para la función subcommand()

    Usage:
        @subcommand([argument("-d", help="Debug mode", action="store_true")])
        def test(args):
            print(args)
    Based on https://mike.depalatis.net/blog/simplifying-argparse.html
    
    Parameters
    ----------
    name_or_flags : list        
    kwargs: dict        
            
    Returns
    -------
        Tuple
            Mismos valores que se recibieron pero desempacados en una tupla que tenga (*args, **kwargs)        
    '''
    return ([*name_or_flags], kwargs)

def weird_round(number):
    '''
    Wrapper para la función estándar de python round()
    Excepto cuando el número está entre 0 y 1 inclusivo en la izquierda, siempre va a redondear a 1
    El resto de valores siempre usaran round()
    
        
    Parameters
    ----------
    number: float       
            
    Returns
    -------
        numero : float
        El número redondeado
    '''
    if (number < 1) and (number >= 0):
        number = 1.0
    
    return round(number)