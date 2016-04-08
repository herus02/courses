import turtle

def draw_cricle():
  angie = turtle.Turtle()
  angie.shape('arrow')
  angie.color('blue')
  angie.speed(1)

  angie.circle(100)

def draw_square():
  brad = turtle.Turtle()
  brad.shape('turtle')
  brad.color('yellow')
  brad.speed(1)

  for i in range(0, 4):
    brad.forward(100)
    brad.right(90)

def main():
  window = turtle.Screen()
  window.bgcolor('red')

  # desenha um quadrado
  draw_square()

  # desenha um circulo
  draw_cricle()

  window.exitonclick()

main()