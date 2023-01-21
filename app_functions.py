from utils import (
    yaml_to_python,    
    suma_listas,
    resta_listas,
    get_src_abspath,
    weird_round
)

PRODUCTOS_BASE_PATH = "datamodels/productos_base.yaml"
RECETAS_PATH = "datamodels/recetas.yaml"
REFRI_PATH = "datamodels/refri.yaml"

def get_recetas_path():
    return get_src_abspath(RECETAS_PATH)

def get_productos_base_path():
    return get_src_abspath(PRODUCTOS_BASE_PATH)

def get_refri_path():
    return get_src_abspath(REFRI_PATH)

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
            suma_sin_acumulador = (float(detalles["cantidad"]) * float(propiedades["cantidad"]))
            if not suma_recetas.get(ingrediente):
                suma_recetas[ingrediente] = dict(detalles)
                suma_recetas[ingrediente]["cantidad"] = suma_sin_acumulador
            else:
                suma_recetas[ingrediente]["cantidad"] = float(suma_recetas[ingrediente].get("cantidad", 0)) + suma_sin_acumulador
    return suma_recetas

def genera_lista_compras():
    """
    Genera la lista de compras final, función principal del programa    
    
    DEPENDECY
    ---------
    yaml_to_python(yaml_fp)
    get_src_abspath()
    suma_ingredientes_recetas()
    suma_listas()
    resta_listas()

    Parameters
    ----------
    None 

    Returns
    -------
    Lista de recetas : list
        Lista de diccionarios, la lista de compras final
        lista_compras = productos_base + suma_recetas - articulos_refri
    """
    productos_base = yaml_to_python(get_src_abspath(PRODUCTOS_BASE_PATH))
    articulos_refri = yaml_to_python(get_src_abspath(REFRI_PATH))
    lista_recetas = yaml_to_python(get_src_abspath(RECETAS_PATH))
    suma_recetas = suma_ingredientes_recetas(lista_recetas)
    lista_articulos_completos = suma_listas(productos_base, suma_recetas)    
    return resta_listas(lista_articulos_completos, articulos_refri)

def get_recetas():
    """
    Obtiene una lista de todos los nombres de las recetas que existen en recetas.yaml
    
    DEPENDECY
    ---------
    yaml_to_python(yaml_fp)

    Parameters
    ----------
    None 

    Returns
    -------
    Lista de recetas : list
        Lista de los nombres de todas las recetas
    """
    recetas = yaml_to_python(get_src_abspath(RECETAS_PATH))
    return [item["nombre"] for _,item in recetas.items()]

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
    lista_compras_ordenada = sorted(lista_compras.items(), key=lambda x: x[1]["seccion"])
    lista_compras_ordenada = dict(lista_compras_ordenada)
    ultima_seccion = ""
    for articulo,detalles in lista_compras_ordenada.items():
        cantidad = float(detalles["cantidad"])
        unidad = detalles.get("unidad", "pieza")        

        if cantidad >= 1:
            if detalles["seccion"] != ultima_seccion:
                c_seccion = "  -- {!s} --\n".format(detalles["seccion"])
                ultima_seccion = detalles["seccion"]
            else:
                c_seccion = ""
            
            rounded_cantidad = weird_round(cantidad)
            f_unidad = "{!s}s".format(unidad) if (rounded_cantidad > 1.0) else unidad
            lista_compras_formateada = lista_compras_formateada + "{!s}{!s} {!s} de {!s}\n".format(
                c_seccion, rounded_cantidad, f_unidad, articulo
            )
    return lista_compras_formateada

def genera_lista_refri():
    """
    Genera la lista que terminará en refri.yaml, sumando todos los productos en productos_base.yaml y recetas.yaml
    
    DEPENDECY
    ---------
    yaml_to_python(yaml_fp)
    get_src_abspath()
    suma_ingredientes_recetas()
    suma_listas()    

    Parameters
    ----------
    None 

    Returns
    -------
    Lista de productos : list
        Lista de diccionarios con formato de refri.yaml
        productos_base + productos en recetas
    """
    productos_base = yaml_to_python(get_src_abspath(PRODUCTOS_BASE_PATH))    
    lista_recetas = yaml_to_python(get_src_abspath(RECETAS_PATH))
    suma_recetas = suma_ingredientes_recetas(lista_recetas)
    return suma_listas(productos_base, suma_recetas)