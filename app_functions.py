from utils import (
    yaml_to_python,
    suma_ingredientes_recetas,
    suma_listas,
    resta_listas,
    get_src_abspath
)

PRODUCTOS_BASE_PATH = "datamodels/productos_base.yaml"
RECETAS_PATH = "datamodels/recetas.yaml"
REFRI_PATH = "datamodels/refri.yaml"

def genera_lista_compras():
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
        cantidad = detalles["cantidad"]
        unidad = detalles.get("unidad", "pieza")
        f_unidad = "{!s}s".format(unidad) if (cantidad > 1.0) else unidad        

        if round(cantidad) >= 1.0:
            if detalles["seccion"] != ultima_seccion:
                c_seccion = "  -- {!s} --\n".format(detalles["seccion"])
                ultima_seccion = detalles["seccion"]
            else:
                c_seccion = ""

            lista_compras_formateada = lista_compras_formateada + "{!s}{!s} {!s} de {!s}\n".format(
                c_seccion, cantidad, f_unidad, articulo
            )
    return lista_compras_formateada