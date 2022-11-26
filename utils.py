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

def mezcla_listas(resta=False, *argv):
    """
    Le suma o le resta a la lista 0 (argv[0]) la suma de las cantidades existentes en el resto de listas pasadas por parámetros
    Nota que las listas dentro de 'argv' son listas de artículos, pero están representadas por diccionarios en python

    El procedimiento es como sigue:
    - Mezcla todas las listas de ingredientes/articulos pasadas por parámetro
    - Suma todos los valores encontrados por esas llaves de la lista mezclada, excepto el de la lista agrv[0]
    - Si 'resta' es True,
        toma la cantidad del ingrediente/articulo en argv[0] y le resta la suma de las otras listas
        (si es <0 dicho ingrediente se elimina de la lista mezclada)
    - Si 'resta' es False,
        se suma la cantidad del ingrediente/articulo en argv[0] con la usma de las otras listas
        y se guarda en la lista mezclada 
    
    Parameters
    ----------
    argv : list
        Lista de los parametros pasados
        Cada parámetro es un diccionaro de articulos con sus cantidades con el formato de refri.yaml o productos_base.yaml
            
    Returns
    -------
    lista mezclada de articulos : dict
        Diccionario mezclado de todos los diccionarios pasados por parámetro, 
        con el mismo formato que refri.yaml y productos_base.yaml con las cantidades de cada ingrediente
        sumadas o restadas (dependiendo de la bandera 'resta')
    """
    # lista_mezclada = {lista_mezclada}
    # suma_listas_sin_lista_0 = {}    

    # # Mezcla todas las listas de ingredientes/articulos pasadas por parámetro
    # for c_list in argv:
    #     lista_mezclada = lista_mezclada | c_list

    # # Suma todos los valores encontrados por esas llaves de la lista mezclada, excepto el de la lista agrv[0]    
    # for key,_ in lista_mezclada:
    #     for c_list in argv[1:]:
    #         suma_listas_sin_lista_0[key] = c_list[key].get("cantidad", 0) + c_list[key]["cantidad"]
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
    lista_recetas : dictionary
        diccionario de diccionarios con el formato de recetas.yaml
        Que serán mezclados, todos los ingredientes con el mismo nombre, se sumarán sus cantidades
        y se multiplicarán por la cantidad indicada de recetas
            
    Returns
    -------
    ingredientes y la suma de sus cantidades : dict
        Dict con el mismo formato que refri.yaml y productos_base.yaml con todos los ingredientes y sus cantidades
        sumadas dependiendo de su aparición en las recetas    

    Basada en la respuesta de ospahiu en https://stackoverflow.com/questions/39000681/find-the-sum-of-values-within-the-values-of-a-nested-dictionary
    """
    import pdb
    suma_recetas = {}
    for receta, propiedades in lista_recetas.items():
        for ingrediente, detalles in propiedades["ingredientes"].items():
            suma_sin_acumulador = (detalles["cantidad"] * propiedades["cantidad"])
            if not suma_recetas.get(ingrediente, None):
                suma_recetas[ingrediente] = detalles                        
            suma_recetas[ingrediente]["cantidad"] = suma_recetas[ingrediente].get("cantidad", 0) + (detalles["cantidad"] * propiedades["cantidad"])
    return suma_recetas

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