import turtle
s=turtle.Turtle()
s.speed(50)
turtle.bgcolor("black")
s.color("white")
for i in range(4):
    s.forward(100)
    s.left(90)
    s.shape("square")
turtle.mainloop()
