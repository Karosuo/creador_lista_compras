# creador_lista_compras
Un parseador básico de archivos yaml con el contenido de recetas de comida, lista de compras base y el contenido del refri, que dará como resultado:
"lista de compras final = lista compras base + la suma de ingredientes en recetas - lo que hay en el refri"

## No hay unidades para los artículos
Solo hay nombre de articulo y cantidad de articulos.
Por ejemplo, si el artículo es *tomates*, entonces se implica que la cantidad *3* usa la unidad *piezas*, pero si el artículo dice *barra_pan*, se implica que es una bolsa de pan de barra.

No tengo idea si después agregaré unidades compuestas, estilo 15 tomates son 1 kg de tomates, para eso una base de datos sería más eficiente
