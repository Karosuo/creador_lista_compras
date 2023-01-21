# Help text
help_description = '''
Suma las cantidades de recetas y las convierte en una lista de diccionarios (y las guarda en suma_recetas)\n
Obtiene la lista de compras como:\n
lista_compras = productos_base + suma_recetas - articulos_refri\n
\n
Los archivos yaml necesitan estar en la raiz del directorio 
y necesitan tener los siguientes nombres:\n
"recetas.yaml", "refri.yaml" and "productos_base.yaml"\n
Vea: "formato_contenido.yaml" para saber el formato con el que se puede llenar dichos archivos
\n
'''

# Execution text
exec_title = "\n\t...Generador de lista de compras...\n"
exec_desc = "Suma los articulos de las recetas.yaml con los de productos_base.yaml y le resta lo que hay en el refri.yaml\n"