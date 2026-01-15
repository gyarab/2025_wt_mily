from turtle import forward, right, left, exitonclick

def domecek(a):
  
    forward(a)

    left(135)
    forward(a * sqrt(2))

    right(135)
    forward(a)

    right(135)
    forward(a * sqrt(2))

    left(135)
    forward(a)

    left(45)
    forward(a * sqrt(2) / 2)

    left(90)
    forward(a * sqrt(2) / 2)

    left(45)
    forward(a)

    left(90)

setheading(0)

pocet_domecku = 36
uhel = 360 / pocet_domecku

for i in range(pocet_domecku):
    velikost = randint(30, 55)
    domecek(velikost)

    forward(10)

    left(uhel)

exitonclick()
