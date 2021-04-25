import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(10)
COLOR_CUERPO = 'red'
COLOR_CASCO = '#9acedc'

t.width(20)

def cuerpo():
  t.fillcolor(COLOR_CUERPO)
  t.begin_fill()
  t.right(90)
  t.fd(50)
  t.right(180)
  t.circle(40,-180)
  t.right(180)

  t.fd(200)
  t.right(180)

  t.circle(100,-180)
  t.backward(20)
  t.left(15)
  t.circle(500,-20)
  t.backward(20)
  t.circle(40,-180)
  t.left(7)
  t.backward(50)

  t.up()
  t.left(90)
  t.forward(10)
  t.right(90)
  t.down()
  t.right(240)
  t.circle(50, -70)

  t.end_fill()

def casco():
  t.up()
  t.right(230)
  t.forward(100)
  t.left(90)
  t.forward(20)
  t.right(90)
  t.down()

  t.fillcolor(COLOR_CASCO)
  t.begin_fill()
  t.right(150)
  t.circle(90, -55)

  t.right(180)
  t.forward(1)
  t.right(180)
  t.circle(10,-65)

  t.right(180)
  t.forward(110)
  t.right(180)

  t.circle(50,-190)
  t.right(170)
  t.fd(80)
  t.right(180)
  t.circle(45, -30)

  t.end_fill()

def mochila():
  t.up()
  t.right(60)
  t.forward(100)
  t.right(90)
  t.forward(75)
  t.down()

  t.fillcolor(COLOR_CUERPO)
  t.begin_fill()
  t.fd(30)
  t.right(255)
  t.circle(300, -30)
  t.right(260)
  t.fd(30)
  t.end_fill()


cuerpo()
casco()
mochila()
