from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(15)
def backwards():
    tim.backward(15)

def clockwise_move(): #could be solved by using obj.heading +- 10
    tim.right(15)
def counter_clockwise():
    tim.left(15)
def clear():
    tim.reset()

screen.listen() #Higher order function
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise_move)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
