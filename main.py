from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_length()
        scoreboard.increase_score()

    snake.move()
    snake_position = snake.current_position()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 250 or snake.head.ycor() <= -300:
        snake.reset_snake()
        scoreboard.reset_score()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
