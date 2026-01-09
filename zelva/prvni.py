from turtle import forward, left, right, exitonclick

def domecek(a):
    left(a)
    forward(10)
    left(90)
    forward(a)
    left(90)
    forward(7)
    right(90)
    forward(14)
    right()

domecek(10)

exitonclick()