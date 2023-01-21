#!/usr/bin/env/ python

# Author: Rafael Karosuo

# Subcomandos basado en la solución de Mike
# https://gist.github.com/mivade/384c2c41c3a29c637cb6c603d4197f9f

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

from argparse import RawTextHelpFormatter, ArgumentParser
import text_descriptions as tdesc
from utils import (
    print_lista_de_compras,
    subcommand,
    arguments
)
from app_functions import (
    genera_lista_compras
)

# Create parser for cli params and the subparser for subcommands
parser = ArgumentParser(
    prog = tdesc.help_prog, 
    description = tdesc.help_description,
    epilog = tdesc.help_epilog,
    formatter_class=RawTextHelpFormatter,  
)
subparsers = parser.add_subparsers(description=tdesc.subcommands_desc)

@subcommand(parent=subparsers, subcmd_desc=tdesc.main_refri_checklist_help)
def refri_checklist():
    print("\nJust a dummy function for the subcommand...\n")

# Parse arguments and execute the subcommands if any
args = parser.parse_args()

# If no commands, just print the list
if hasattr(args, "func"):
    args.func()    
else:
    lista_de_compras = genera_lista_compras()

    print(tdesc.exec_title)
    print(tdesc.exec_desc)
    print("Lista de compras:\n{!s}".format(
        print_lista_de_compras(lista_de_compras)
    ))