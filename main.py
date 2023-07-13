from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

tim = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # collission with food
    if snake.segment[0].distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    # collission with wall
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or \
            snake.segment[0].ycor() < -280:
        game_on = False
        score.game_over()

    #colission with tail
    for segments in snake.segment[1::]:
        if snake.segment[0].distance(segments) < 10:
            game_on = False
            score.game_over()





screen.exitonclick()