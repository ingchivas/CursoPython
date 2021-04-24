# Una breve introducción a Python

## Breve recorrido por la historia de Python

Python es el tercer lenguaje de programación más usado en el mundo.

Guido Van Rossum es el creador y responsable de que Python exista. Se trata de un informático de origen holandés que fue el encargado de diseñar Python y de pensar y definir todas las vías posibles de evolución de este popular lenguaje de programación

El nombre de este lenguaje de programación es en honor a los Monty Python, el famoso grupo de cómicos británicos.

En las navidades de 1989 Van Rossum, mientras trabajaba en un centro de investigación holandés (CWI), decidió empezar un nuevo proyecto como pasatiempo personal. Pensó en darle continuidad a ABC, un lenguaje de programación que se desarrollo en el mismo centro en el que estaba trabajando.

![EjABC](https://cdn-blog.adafruit.com/uploads/2020/01/adafruit_2019_3368.jpg)

La historia de Python empieza con Guido Van Rossum empezando su desarrollo en 1989 y empezando a implementarlo en febrero de 1991, momento en el que se publicó la primera versión pública: la 0.9.0.

La versión 1.0, que se publicó en enero de 1994, la versión 2.0 se publicó en octubre de 2000 y la versión 3.0 se publicó en diciembre de 2008.

Esta primera versión de Python ya incluía clases con herencias, manejo de excepciones, funciones y una de sus características fundamentales: funcionamiento modular. Esto permitía que fuese un lenguaje mucho más limpio y accesible para la gente con pocos conocimientos de programación. Una característica que se mantiene hasta el día de hoy.

## Características de Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional.

### Paquetes|Librerías

El Python Package Index (PyPI) o en español significa Índice de paquetes de Python alberga miles de módulos de terceros para Python.
Tanto la biblioteca estándar de Python como los módulos aportados por la comunidad permiten infinitas posibilidades.

- Desarrollo web e Internet.
- Acceso a la base de datos.
- GUIs de escritorio.
- Científico y numérico.
- Educación.
- Programación de red.
- Desarrollo de Software y Juegos.

Revisemos algunos ejemplos de sintaxis:

```python
print("Bienvenidos a Python")
```

Por ejemplo, este sencillo programa de "Hello World" en C++ se haría de esta forma:

```c++
#include <iostream>
int main() {
    std::cout << "Hola Mundo"<<endl;
    return 0;
}
```

<br>

Ejemplo de pequeño programa:

```python
bool = True

a = 1
b = 5

suma = a + b
print(suma)

if suma == 6 and bool == True:
  print("La suma es 6")
else:
  print("La suma no es 6")

```

Ejemplo de función:

```python

def sumadedosnumeros(a,b):
  '''
  Esta función toma dos números: a y b y los suma.
  '''
  return (a+b)
```

### Tipos de datos en Python

<table border="1" class="docutils">
<colgroup>
<col width="24%" />
<col width="16%" />
<col width="60%" />
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Categoría de tipo</strong></td>
<td><strong>Nombre</strong></td>
<td><strong>Descripción</strong></td>
</tr>
<tr class="row-even"><td rowspan="5"><em>Números inmutables</em></td>
<td><code class="docutils literal notranslate"><span class="pre">int</span></code></td>
<td><a class="reference internal" href="tipo_numericos.html#python-num-entero"><span class="std std-ref">entero</span></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">long</span></code></td>
<td><a class="reference internal" href="tipo_numericos.html#python-num-entero-long"><span class="std std-ref">entero long</span></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">float</span></code></td>
<td><a class="reference internal" href="tipo_numericos.html#python-num-float"><span class="std std-ref">coma flotante</span></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">complex</span></code></td>
<td><a class="reference internal" href="tipo_numericos.html#python-num-complex"><span class="std std-ref">complejo</span></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">bool</span></code></td>
<td><a class="reference internal" href="tipo_booleanos.html#python-bool"><span class="std std-ref">booleano</span></a></td>
</tr>
<tr class="row-odd"><td rowspan="4"><em>Secuencias
inmutables</em></td>
<td><code class="docutils literal notranslate"><span class="pre">str</span></code></td>
<td><a class="reference internal" href="tipo_cadenas.html#python-str"><span class="std std-ref">cadena de caracteres</span></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">unicode</span></code></td>
<td><a class="reference internal" href="tipo_cadenas.html#python-unicode-cls"><span class="std std-ref">cadena de caracteres Unicode</span></a></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">tuple</span></code></td>
<td><a class="reference internal" href="tipo_tuplas.html#python-tuple"><span class="std std-ref">tupla</span></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">xrange</span></code></td>
<td><a class="reference internal" href="../leccion5/funciones_integradas.html#python-fun-xrange"><span class="std std-ref">rango inmutable</span></a></td>
</tr>
<tr class="row-odd"><td rowspan="2"><em>Secuencias mutables</em></td>
<td><code class="docutils literal notranslate"><span class="pre">list</span></code></td>
<td><a class="reference internal" href="tipo_listas.html#python-list"><span class="std std-ref">lista</span></a></td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">range</span></code></td>
<td><a class="reference internal" href="../leccion5/funciones_integradas.html#python-fun-range"><span class="std std-ref">rango mutable</span></a></td>
</tr>
<tr class="row-odd"><td><em>Mapeos</em></td>
<td><code class="docutils literal notranslate"><span class="pre">dict</span></code></td>
<td><a class="reference internal" href="tipo_diccionarios.html#python-dict"><span class="std std-ref">diccionario</span></a></td>
</tr>
<tr class="row-even"><td><em>Conjuntos mutables</em></td>
<td><code class="docutils literal notranslate"><span class="pre">set</span></code></td>
<td><a class="reference internal" href="tipo_conjuntos.html#python-set"><span class="std std-ref">conjunto mutable</span></a></td>
</tr>
<tr class="row-odd"><td><em>Conjuntos inmutables</em></td>
<td><code class="docutils literal notranslate"><span class="pre">frozenset</span></code></td>
<td><a class="reference internal" href="tipo_conjuntos.html#python-set"><span class="std std-ref">conjunto inmutable</span></a></td>
</tr>
</tbody>
</table>

### Bibliografía

`https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion1/introduccion.html`
`https://www.tokioschool.com/noticias/historia-python/`