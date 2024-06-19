from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# background kind of stuff
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("my_snake_game")
screen.tracer(0)

# creating the objects
food = Food()
snake = Snake()
scoreboard = Scoreboard()

# line of program to run the snake on keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # extension of snake after collision with food
    if snake.head.distance(food) < 15:
        food.regenerate()
        snake.extent()
        scoreboard.update_score()

    # game will over and display the score after collision with the wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # detection of snake with its body
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
