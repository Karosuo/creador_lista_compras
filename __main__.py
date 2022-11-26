# El caso de uso principal
# Parsea productos_base.yaml y lo guarda como productos_base
# Parsea refri.yaml y lo guarda como articulos_refri
# Parsea recetas.yaml y lo guarda como lista_recetas
# Suma las cantidades de recetas y las convierte en una lista de diccionarios (y las gaurda en suma_recetas)
# Obtiene la lista de compras como
# lista_compras = productos_base + suma_recetas - articulos_refri

from utils import yaml_to_python, get_src_abspath

productos_base = yaml_to_python(get_src_abspath("productos_base.yaml"))
articulos_refri = yaml_to_python(get_src_abspath("refri.yaml"))
lista_recetas = yaml_to_python(get_src_abspath("recetas.yaml"))

print("\nGenerador de lista de compras\n")

print("Contenido productos_base: {!s}, tipo recetas: {!s}".format(
    productos_base, type(productos_base)
))
