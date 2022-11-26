from utils.py import mezcla_listas, yaml_to_python

def suma_listas(*argv):
    """
    Mezcla todas las listas que se pasen como parámetro
    y luego suma las cantidades de los articulos compartidos entre las listas    

    DEPENDECY
    ---------
    mezcla_listas(*argv):

    Parameters
    ----------
    argv : list
        lista de diccionarios con el formato de refri.yaml

    Returns
    -------
    Lista mezclada de articulos con cantidades sumadas : dict                
    """
    lista_mezclada = mezcla_listas(argv)
    lista_mezclada_sumada = {}
    for articulo,_ in lista_mezclada:
        for c_list in argv:
            if not lista_mezclada_sumada.get(articulo):
                lista_mezclada_sumada[articulo] = lista_mezclada[articulo]
            lista_mezclada_sumada[articulo]["cantidad"] = lista_mezclada_sumada[articulo].get("cantidad", 0) + c_list[articulo]["cantidad"]

    return lista_mezclada_sumada

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