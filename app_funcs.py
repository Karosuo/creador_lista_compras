from utils import (
    yaml_to_python,
    suma_ingredientes_recetas,
    suma_listas,
    resta_listas,
    get_src_abspath
)
def genera_lista_compras():
    productos_base = yaml_to_python(get_src_abspath("productos_base.yaml"))
    articulos_refri = yaml_to_python(get_src_abspath("refri.yaml"))
    lista_recetas = yaml_to_python(get_src_abspath("recetas.yaml"))
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
    recetas = yaml_to_python(get_src_abspath("recetas.yaml"))
    return [item["nombre"] for _,item in recetas.items()]    