import turtle

def draw_circle_out_of_square():
  brad = turtle.Turtle()
  brad.shape('turtle')
  brad.color('yellow')
  brad.speed(5)

  for j in range(0, 36):
    for i in range(0, 4):
      brad.forward(100)
      brad.right(90)
    brad.right(10)


def main():
  window = turtle.Screen()
  window.bgcolor('red')

  draw_circle_out_of_square()

  window.exitonclick()

main()