# Help text
help_description = '''
Obtiene la lista de compras como:\n
lista_compras = productos_base + suma_recetas - articulos_refri\n
\n
Dichos elementos están representados por archivos yaml, que deben tener los siguientes nombres:\n
"productos_base.yaml", "recetas.yaml" y "refri.yaml" respectivamente\n
* Los productos_base son aquellos que usualmente se agregan a la lista de compras encima de las recetas, como limpieza para el hogar o similar
* El contenido del refri, representa lo que ya no se necesita comprar de la lista original
Vea: "formato_contenido.yaml" para saber el formato con el que se puede llenar dichos archivos\n
'''
help_epilog = "Software Libre, GPL3"
help_prog = "python generador_lista_compras"
subcommands_desc = "Externaliza una API de comandos para acciones específicas"

# generator subparser
main_refri_checklist_help = '''
Genera lo que debería haber en el refri y lo pone en refri.yaml\n
Es decir:\n
Borra todo lo que haya en refri.yaml, combina los productos de productos_base.yaml y
recetas.yaml y los pega en refri.yaml, usando el formato esperado para refri.yaml.\n
Toma en cuenta la cantidad de instancias de recetas y no redondea las cantidades combinadas
'''

main_lista_recetas_help = '''
Lista los nombres de todos las recetas que estén disponibles en recetas.yaml
'''

# Execution text
exec_title = "\n\t...Generador de lista de compras...\n"
exec_desc = "Suma los articulos de las recetas.yaml con los de productos_base.yaml y le resta lo que hay en el refri.yaml\n"