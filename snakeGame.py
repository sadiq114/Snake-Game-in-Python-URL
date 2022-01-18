# From video but gives error
# URL:https://www.youtube.com/watch?v=8UZqG-MC7Fo

import turtle
import random
import time

delay=0.1
score=0
highestscore=0

# Snake bodies
bodies = []

# Getting a screen/Canvas
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray") # set background color as gray
s.setup(width=600,height=600) # size of the screen


# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()# st means show turtle function


# score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0 | Heighest Score :0")


def moveup():
    if head.direction != "down":
       head.direction = "up"
def movedown():
    if head.direction != "up":
       head.direction = "down"
def moveleft():
    if head.direction != "rigth":
       head.direction = "left"
def moveright():
    if head.direction != "left":
       head.direction = "right"
def movestop():
    head.direction="stop"
def move():
    if head.direction == "up":
       y=head.ycor()
       head.sety(y+20)
    if head.direction == "down":
       y=head.ycor()
       head.sety(y-20)
    if head.direction == "left":
       y=head.xcor()
       head.sety(x-20)
    if head.direction == "rigth":
       y=head.xcor()
       head.sety(x+20)


# Event handling - Key Mappings
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")


# main loop
while True:
    s.update() # This is to update the screen
    # check collision with boarder
    if head.xcor()>290:
       head.setx(-290)
    if head.xcor()< -290:
       head.setx(290)
    if head.ycor()> 290:
       head.sety(-290)
    if head.ycor()< -290:
       head.sety(290)

        
    # check collision with food
    if head.distance(food) < 20:
        # move the food to the new random place
       x = random.randint(-290,290)
       y = random.randint(-290,290)
       food.goto(x,y)


        # increase length of the snake
       body = turtle.Turtle()
       body.speed(0)
       body.penup()
       body.shape("square")
       body.color("red")
       body.fillcolor("black")
       bodies.append(body)# append new body


        # increase the score
       score+=10

        # change delay
       delay-=0.001


        # update the heighest score
       if score>highestscore:
            highestscore=score
       sb.clear()
       sb.write("Score: {} Heighest score : {}".format(score,highestscore))
    # move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
           
        
    # check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            dealy=0.1

            # update score board
            sb.clear()
            sb.write("Score: {} Heighest score : {}".format(score,highestscore))
        time.sleep(dealy)
s.mainloop()

# This is the end of our snake game code 

        
        





