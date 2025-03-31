from turtle import Turtle, Screen
from Snake import snake
from Scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

Snake = snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Snake.up,"Up")
screen.onkey(Snake.down,"Down")
screen.onkey(Snake.left,"Left")
screen.onkey(Snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()


    if Snake.head.distance(food) < 15:
        food.refresh()
        Snake.extend()
        scoreboard.inc_score()

    if Snake.head.xcor() > 295 or Snake.head.xcor() < -300 or Snake.head.ycor() > 300 or Snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    for segment in Snake.segments:
        if segment == Snake.head:
            pass
        elif Snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()


