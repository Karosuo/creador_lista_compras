from utils import yaml_to_python

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