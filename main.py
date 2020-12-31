import turtle
# from PIL import Image


# img = Image.open("betty.gif")
# smaller = img.resize((img.width // 4, img.height // 4))

# smaller.save("small_betty.gif")


t = turtle.Turtle()


scr = t.getscreen()
scr.setup(500,500)
scr.bgcolor("silver")
# scr.title("title")
# scr.register_shape("small_betty.gif")

# t.shape("small_betty.gif")
# t.resizemode("user")
# t.shapesize(2, 2, 1)

# t.tilt(75)

# t.forward(100)

# t.tilt(90)

t.penup()
t.hideturtle()

t2 = turtle.Turtle()

t2.color("green")

t2.penup()
t2.hideturtle()

t2.goto(50,50)




def what():
  print ("what")

def hello(x,y):
  print ("hello", x, y)

scr.onclick(hello)

scr.onkey(what, "G")

scr.listen()

scr.tracer(0)




while True:
  t.clear()
  t2.clear()
  t.forward(1)
  t2.forward(1)
  t.dot(10)
  t2.dot(20)
  if (t.xcor() > 250):
    t.setx(t.xcor() - 500)
  if (t2.xcor() > 250):
    t2.setx(t2.xcor() - 500)
  scr.update()
  # print (t.position())