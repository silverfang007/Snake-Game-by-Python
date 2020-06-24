import turtle
import time
import random

delay=0.1
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)   # Turns off animation

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"


# Snake Food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Create List for snake body
segments=[]


# Functions

def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"

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

# Keyboard Binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    wn.update()

    # Check for collision with the border.....

    if ((head.xcor()> 290) or (head.xcor()< -290) or (head.ycor()> 290) or (head.ycor()< -290)):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # Hide the Segments as after hitting the wall also, they are re-born with previous length.....
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segment list.....
        segments.clear()


    # This is where we check for collision with the food
    if head.distance(food) <20:
        # Move the food to random location
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #Add a segment

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) # This is where the greyed part (after eating the food) gets appended to the main list


        # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

        # Move segement 0 to where the head is, because what about the 0th position segment { can't do 0 minus(-) 1 }
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()

    time.sleep(delay)




wn.mainloop()