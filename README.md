# Creador de lista de compras
Un parseador de archivos yaml con el contenido de recetas de comida, lista de compras base y el contenido del refri, que dará como resultado:
**"lista de compras final = lista compras base + la suma de ingredientes en recetas - lo que hay en el refri"**

Es decir algo como lo siguiente
  -- abarrotes --
2 barras de pan
2 botes de queso_parmesano
2 botes de aderezo_ranch
2 bolsas de lenteja
2 porcions de cubito_de_pollo
2 piezas de chile_chipotle
  -- carnes --
6 charolas de pollo
250 gramos de tocino

## No hay conversión de unidades para los artículos
Los articulos tienen unidades, pero estas se usan solamente para que la impresión de la lista sea más amena para lectura humana.
No hay conversión de las mismas de ningún tipo.
Además, se implica que siempre que haya un artículo sin especificar la unidad, esta sería *piezas*
Se espera que el ingreso de datos sea a consciencia de usar siempre la misma unidad para el mismo artículo en todos los archivos yaml.

Por ejemplo
Puede haber muchas instancias de *tomates*, unas sin especificar *unidad*, otras especificando kilogramos y otras especificando piezas, este problema no está resuelto, solo se sumarían/restarían las cantidades de *tomates* y se usaría la *unidad* que se encuentre primero en la lista de recetas o de productos base, por lo que el resultado sería incorrecto.

No tengo idea si después agregaré unidades compuestas, estilo 15 tomates son 1 kg de tomates, para eso una base de datos sería más eficiente, pero por ahora esta implementación me es más que suficiente.


## Requerimientos de llenado de información
Se implica que todos los nombres de artículos están escritos en singular, así como los nombres de las unidades.
Todos los campos de los artículos son obligatorios, excepto "unidad"