# El caso de uso principal
# - Sumas todas las recetas y lo guardas en "suma_recetas"
# - A "productos_base" le sumas "suma_recetas" y le restas "refri"

from utils import yaml_to_python, SRC_BASE_PATH
from os.path import abspath, join

print("\nGenerador de lista de compras\n")

print("Contenido productos_base: {!s}".format(
    yaml_to_python(abspath(join(SRC_BASE_PATH, "productos_base.yaml")))
    
))
