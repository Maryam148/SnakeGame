import turtle as t
from snake import Snake
from food import Food
from scoreBoard import Scoreboard
import time
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreBoard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreBoard.score_rate()
    # detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        scoreBoard.game_over()
    # collision with tail
    # trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
screen.exitonclick()