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
    lista_compras_formateada = ""
    for articulo,detalles in lista_compras.items():
        cantidad = detalles["cantidad"]
        unidad = detalles.get("unidad", "pieza")
        f_unidad = "{!s}s".format(unidad) if (cantidad > 1.0) else unidad        

        lista_compras_formateada = lista_compras_formateada + "{!s} {!s} de {!s}\n".format(
            cantidad, f_unidad, articulo
        )
    return lista_compras_formateada

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
                lista_mezclada_sumada[articulo]["cantidad"] = 0
            
            if c_list.get(articulo):
                lista_mezclada_sumada[articulo]["cantidad"] = lista_mezclada_sumada[articulo]["cantidad"] + c_list[articulo]["cantidad"]
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
            restaAB = lista_restada[articulo]["cantidad"] - lista_B[articulo]["cantidad"]
            if restaAB > 0:                
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
    suma_recetas = {}
    for receta, propiedades in lista_recetas.items():
        for ingrediente, detalles in propiedades["ingredientes"].items():
            suma_sin_acumulador = (detalles["cantidad"] * propiedades["cantidad"])
            if not suma_recetas.get(ingrediente):
                suma_recetas[ingrediente] = dict(detalles)
                suma_recetas[ingrediente]["cantidad"] = suma_sin_acumulador
            else:
                suma_recetas[ingrediente]["cantidad"] = suma_recetas[ingrediente].get("cantidad", 0) + suma_sin_acumulador
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