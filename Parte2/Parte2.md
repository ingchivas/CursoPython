# Parte 2:
## Turtle en Python
### Introducción a turtle

En 1967 Wally Feurzeig y Seymour Papert crearon Logo, un lenguaje de programación con fines educativos. Ese lenguaje incluía las llamadas "gráficas tortuga".

![Turtle1](https://pythonturtle.org/images/screenshot.gif)

La "tortuga" de Logo es un cursor al que se le pueden dar órdenes de movimiento (avance, retroceso o giro) y que puede ir dejando un rastro sobre la pantalla. Moviendo adecuadamente la tortuga se pueden conseguir dibujar todo tipo de figuras.

Python incluye un módulo llamado "turtle" que permite crear gráficos de tortuga. Este módulo viene builtin dentro de los módulos que tiene incluida la instalación de python.

Igualmente turtle está construida sobre tkinter, el módulo de python que nos permite hacer interfaces gráficas o GUIs.
```python
import turtle
```
Recordemos que hay diferentes formas de importar librerías, por comodidad, turtle se puede importar de forma total, aunque en lo personal prefiero importar el módulo como "te".

```python
#Importación como te [Como objeto (POO)]
import turtle as te
```
```python
#Importación completa [No POO]
from turtle import *
```

Turtle se basa en un plano cartesiano de 2 dimensiones. (x,y)
![plano](https://st4.depositphotos.com/10018754/30949/v/600/depositphotos_309491620-stock-illustration-cartesian-coordinate-system-in-the.jpg)
![plano2](https://www.mclibre.org/consultar/python/img/turtle/turtle-ejes.png)

Por defecto, la ventana tiene dimensiones de (450x450px)

### Ejemplos
Como primer ejemplo, hagamos un cuadrado.

```python
import turtle
t = turtle.Turtle()

for i in range(4):
	t.forward(50)
	t.right(90)
turtle.done()
```

Ahora, una estrella:

```python
import turtle
t = turtle.Turtle()

for i in range(50):
	t.forward(50)
	t.right(144)
	
turtle.done()
```

Ahora un pequeño generador de polígonos regulares

```python
import turtle
t = turtle.Turtle()

num_lados = 6
m_lados = 70
angulo = 360.0 / num_lados

for i in range(num_lados):
	t.forward(m_lados)
	t.right(angulo)
	
turtle.done()
```

Podemos modificar un poquito nuestro código y hacer una función que nos permita generar un polígono de n lados.

```python
import turtle
t = turtle.Turtle()

def p_regular(num_lados,m_lados):
    angulo = 360.0 / num_lados
    
    for i in range(num_lados):
    	t.forward(m_lados)
    	t.right(angulo)

```

Existen diversos métodos que nos permiten hacer nuestra ventana más personal, por ejemplo le podemos cambiar el nombre, la forma de la tortuga, el grosor de la línea, entre otros.

```python
import turtle
turtle.title("Nombre de la tortuga")
t = turtle.Turtle()
t.pensize(5)
t.shape('turtle')
```

Podemos esconder a nuestra tortuga si queremos.

```python
t.ht()
```

Aquí tenemos una lista de los comandos principales de nuestra tortuga.

<table><thead><tr><th>Método</th><th>Parámetro/s</th><th>Descripción</th></tr></thead><tbody><tr><td>Turtle()</td><td>None</td><td>Creates and returns a new tutrle object</td></tr><tr><td>forward()</td><td>amount</td><td>Moves the turtle forward by the specified amount</td></tr><tr><td>backward()</td><td>amount</td><td>Moves the turtle backward by the specified amount</td></tr><tr><td>right()</td><td>angle</td><td>Turns the turtle clockwise</td></tr><tr><td>left()</td><td>angle</td><td>Turns the turtle counter clockwise</td></tr><tr><td>penup()</td><td>None</td><td>Picks up the turtle’s Pen</td></tr><tr><td>pendown()</td><td>None</td><td>Puts down the turtle’s Pen</td></tr><tr><td>up()</td><td>None</td><td>Picks up the turtle’s Pen</td></tr><tr><td>down()</td><td>None</td><td>Puts down the turtle’s Pen</td></tr><tr><td>color()</td><td>Color name</td><td>Changes the color of the turtle’s pen</td></tr><tr><td>fillcolor()</td><td>Color name</td><td>Changes the color of the turtle will use to fill a polygon</td></tr><tr><td>heading()</td><td>None</td><td>Returns the current heading</td></tr><tr><td>position()</td><td>None</td><td>Returns the current position</td></tr><tr><td>goto()</td><td>x, y</td><td>Move the turtle to position x,y</td></tr><tr><td>begin_fill()</td><td>None</td><td>Remember the starting point for a filled polygon</td></tr><tr><td>end_fill()</td><td>None</td><td>Close the polygon and fill with the current fill color</td></tr><tr><td>dot()</td><td>None</td><td>Leave the dot at the current position</td></tr><tr><td>stamp()</td><td>None</td><td>Leaves an impression of a turtle shape at the current location</td></tr><tr><td>shape()</td><td>shapename</td><td>Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’</td></tr></tbody></table>

Nuestro último ejemplo:

```python
import turtle
colores = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed('fastest')
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colores[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)

```
