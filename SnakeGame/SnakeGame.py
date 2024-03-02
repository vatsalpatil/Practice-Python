import turtle
import time
import random

delay = 0.2
score = 0

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")

# Create a snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "right"

# Create a snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Create a scoreboard
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Function to go up
def go_up():
    if head.direction != "down":
        head.direction = "up"

# Function to go down
def go_down():
    if head.direction != "up":
        head.direction = "down"

# Function to go left
def go_left():
    if head.direction != "right":
        head.direction = "left"

# Function to go right
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
    win.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "right"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        score_board.clear()
        score_board.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 1
        score_board.clear()
        score_board.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "right"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # Reset the score
            score = 0
            score_board.clear()
            score_board.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

win.mainloop()
