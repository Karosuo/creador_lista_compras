# Parsea productos_base.yaml y lo guarda como productos_base
# Parsea refri.yaml y lo guarda como articulos_refri
# Parsea recetas.yaml y lo guarda como lista_recetas
#
# Suma las cantidades de recetas y las convierte en una lista de diccionarios (y las guarda en suma_recetas)
# Obtiene la lista de compras como
# lista_compras = productos_base + suma_recetas - articulos_refri

# Usage
# activacate venv '\list_gen_venv\Scripts\activate' (or wherver the venv was created)
# run with 'python generador_lista_compras', where generador_lista_compras is the parent directory
import argparse
from argparse import RawTextHelpFormatter
from utils import (
    yaml_to_python,
    get_src_abspath,
    suma_ingredientes_recetas,
    mezcla_listas,
    suma_listas,
    resta_listas,
    print_lista_de_compras
)

parser = argparse.ArgumentParser(
    prog = "Generador de Recetas", 
    description = '''
    Suma las cantidades de recetas y las convierte en una lista de diccionarios (y las guarda en suma_recetas)\n
    Obtiene la lista de compras como:\n
    lista_compras = productos_base + suma_recetas - articulos_refri\n''',
    epilog = "Software Libre, GPL3",
    formatter_class=RawTextHelpFormatter,  
)
args = parser.parse_args()

productos_base = yaml_to_python(get_src_abspath("productos_base.yaml"))
articulos_refri = yaml_to_python(get_src_abspath("refri.yaml"))
lista_recetas = yaml_to_python(get_src_abspath("recetas.yaml"))
suma_recetas = suma_ingredientes_recetas(lista_recetas)
lista_articulos_completos = suma_listas(productos_base, suma_recetas)
lista_de_compras = resta_listas(lista_articulos_completos, articulos_refri)

print("\n\t...Generador de lista de compras...\n")
print("Suma los articulos de las recetas.yaml con los de productos_base.yaml y le resta lo que hay en el refri.yaml\n")
print("Lista de compras:\n{!s}".format(
    print_lista_de_compras(lista_de_compras)
))