from turtle import Screen
from Snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time
screen = Screen()
snake = Snake()
food = Food()
Score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My new Snake game")

screen.update()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        Score.increase_score()

    #detect colision with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        Score.reset()
        snake.reset()


    # detect colision with tail
    for segmenst in snake.turtle_list[1:]:

        if snake.head.distance(segmenst)<10:
            Score.reset()
            snake.reset()
screen.exitonclick()

