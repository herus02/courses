import turtle

def draw_first_letter_name():
  window = turtle.Screen()
  window.bgcolor('yellow')

  felipe = turtle.Turtle()
  felipe.shape('arrow')
  felipe.color('blue')
  felipe.speed(1)

  felipe.left(90)
  felipe.forward(100)
  felipe.right(90)
  felipe.forward(50)
  felipe.right(180)
  felipe.forward(50)
  felipe.left(90)
  felipe.forward(36)
  felipe.left(90)
  felipe.forward(50)

  window.exitonclick()

draw_first_letter_name()