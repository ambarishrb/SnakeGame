import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        score.score_increase()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[5:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()



screen.exitonclick()

