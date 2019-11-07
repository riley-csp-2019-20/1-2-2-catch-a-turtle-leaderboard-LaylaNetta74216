# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
shape = "classic"
size = 5
color = "green"
score = 0

#-----initialize turtle-----
t = trtl.Turtle (shape = shape)
t.color (color)
t.shapesize (size)
t.speed(0)

num_ber = trtl.Turtle()
num_ber.speed(0)

num_ber.penup()
num_ber.ht()
num_ber.goto(-350,250)

font = ( "Comic sans", 35, "bold")
num_ber.write(score, font = font)

counter =  trtl.Turtle()
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter.ht()
counter.penup()
counter.goto(300,-250)
counter.speed(0)


#-----game functions--------
def turtle_clicky(x,y): 
    print("T had a clicky")
    move_ment()
    score_count()

def move_ment():
    t.penup()
    t.hideturtle()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    t.goto(new_xpos, new_ypos)
    t.showturtle()

def score_count():
    global score
    score += 1  
    print(score)  
    num_ber.clear()
    num_ber.write(score, font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
def game_over(): 
  # Here are two customizations
    wn.bgcolor("purple")
    t.stamp()
    counter.ht()
    counter.goto(-450,0)
    #This is another customization
    counter.write("Game over. You did great!", font= font)

#-----events----------------
t.onclick(turtle_clicky)
wn = trtl.Screen()
# This is one customization
wn.bgcolor("blue")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()