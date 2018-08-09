# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random #We'll need this later in the lab
import time
turtle.tracer(1,0)
food_pos = []
food_stamps = []
TIME_STEP = 500
score=0
START_LENGTH = 4
UP=0
SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)
direction = UP
line=turtle.Turtle() #draw the squre
line.penup()
line.goto(250,250)
line.left(180)
line.pendown()
line.pensize(5)
line.forward(500)
line.left(90)
line.forward(500)
line.left(90)
line.forward(500)
line.left(90)
line.forward(500)
line.hideturtle()
turtle.penup()
snake_color=["red","yellow","green","blue","orange","black","purple","light blue","turquoise"]
turtle.color(random.choice(snake_color))
turtle.goto(-350,300)
turtle.write("welcome to the snake game!",font=("Arial",45,"normal"))
turtle.goto(0,0)
def snake_game():
    global turtle
                #size. 
    turtle.penup()

    SQUARE_SIZE = 20

    #Initialize lists
    pos_list = []
    stamp_list = []
    food_pos = []
    food_stamps = []
    snake_color=["red","yellow","green","blue","orange","black","purple","light blue","turquoise"]
    turtle.color(random.choice(snake_color))
   
    #Set up positions (x,y) of boxes that make up the snake
    snake = turtle.clone()
    snake.shape("circle")

    #Hide the turtle object (it's an arrow - we don't need to see it)
    turtle.hideturtle()

    #Draw a snake at the start of the game with a for loop
    #in the snake (i.e. START_LENGTH)
    for i  in range (START_LENGTH) :
        x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
        y_pos=snake.pos()[1]
        x_pos+=SQUARE_SIZE

        my_pos=(x_pos,y_pos) #Store position variables in a tuple
        snake.goto(x_pos,y_pos)
    #Move snake to new (x,y)  
    #Append the new position tuple to pos_list
        pos_list.append(my_pos) 
    #
    #    #Save the stamp ID! You'll need to erase it later. Then append
    #    # it to stamp_list.             
        stamp= snake.stamp()
        stamp_list.append(stamp)


    ###############################################################
    #                    PART 2 -- READ INSTRUCTIONS!!
    ###############################################################
    UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                    #case
    LEFT_ARROW = "Left" #Pay attention to upper and lower case
    DOWN_ARROW = "Down" #Pay attention to upper and lower case
    RIGHT_ARROW = "Right" #Pay attention to upper and lower case
     #Update snake position after this many 
                    #milliseconds
    SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

    UP = 0
    DOWN=1
    LEFT=2
    RIGHT=3
    UP_EDGE = 250
    DOWN_EDGE = -250
    RIGHT_EDGE = 400
    LEFT_EDGE = -400




    turtle.register_shape("trash.gif")
    food = turtle.clone()
    food.shape("trash.gif") 





    def up():
        global direction #snake direction is global (same everywhere)
        direction=UP #Change direction to up
        

    def left(): #LEFT
        global direction
        direction=LEFT
    def right(): #right
        global direction
        direction=RIGHT
        
    def down(): #down
        global direction
        direction=DOWN

    turtle.onkeypress(up,"Up")
    turtle.onkeypress(down,"Down")
    turtle.onkeypress(right,"Right")
    turtle.onkeypress(left,"Left")


        
        


        
    def make_food():
        global food_stamps, food_pos
        #The screen positions go from -SIZE/2 to +SIZE/2
        #But we need to make food pieces only appear on game squares
        #So we cut up the game board into multiples of SQUARE_SIZE.
        min_x=-int(250/2/SQUARE_SIZE)+1
        max_x=int(250/2/SQUARE_SIZE)-1
        min_y=-int(250/2/SQUARE_SIZE)-1
        max_y=int(250/2/SQUARE_SIZE)+1
        
        #Pick a position that is a random multiple of SQUARE_SIZE
        food_x = random.randint(min_x,max_x)*SQUARE_SIZE
        food_y = random.randint(min_y,max_y)*SQUARE_SIZE
        food.goto(food_x,food_y)
        food_pos.append((food_x,food_y))
        a=food.stamp()
        food_stamps.append(a)
        

    def move_snake():
        global food_stamps, food_pos, START_LENGTH,score,TIME_STEP,direction
        x_pos=snake.pos()[0] 
        y_pos=snake.pos()[1]
        if len(food_stamps) <=6 :
            make_food()

        if direction==RIGHT:
            snake.goto(x_pos + SQUARE_SIZE, y_pos)
            
        elif direction==LEFT:
            snake.goto(x_pos - SQUARE_SIZE, y_pos)
            
        elif direction==UP:
            snake.goto(x_pos, y_pos+SQUARE_SIZE)
            
        elif direction==DOWN:
            snake.goto(x_pos, y_pos-SQUARE_SIZE)
            



        new_pos = snake.pos()
        new_x_pos = new_pos[0]
        new_y_pos = new_pos[1]
        my_pos=snake.pos() 
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        if new_x_pos >= 250:
             turtle.goto(-400,150)
             turtle.write("game over! your score is: ", font=("Arial",55 , "normal"))
             turtle.goto(-100,75)
             turtle.write(str(score),font=("Arial", 55, "normal"))
             turtle.done()
        elif new_x_pos <= -250:
             turtle.goto(-400,150)
             turtle.write("game over! your score is: ", font=("Arial",55 , "normal"))
             turtle.goto(-100,75)
             turtle.write(str(score),font=("Arial", 55, "normal"))
             turtle.done()
        elif new_y_pos >= 250:
             turtle.goto(-400,150)
             turtle.write("game over! your score is: ", font=("Arial",55 , "normal"))
             turtle.goto(-100,75)
             turtle.write(str(score),font=("Arial", 55, "normal"))
             turtle.done()
             
        elif new_y_pos <= -250:
            turtle.goto(-400,150)
            turtle.write("game over! your score is: ", font=("Arial",55 , "normal"))
            turtle.goto(-100,75)
            turtle.write(str(score),font=("Arial", 55, "normal"))
            turtle.done()
            
        
    #    ######## SPECIAL PLACE - Remember it for Part 5
        if snake.pos() in food_pos:
            food_ind=food_pos.index(snake.pos())
            #What does this do?
            food.clearstamp(food_stamps[food_ind])
            snake.color(random.choice(snake_color))               
            food_pos.pop(food_ind) 
            food_stamps.pop(food_ind)
            score+=100
            if TIME_STEP >=40:
                TIME_STEP-=40
        else:
            old_stamp = stamp_list.pop(0)
            snake.clearstamp(old_stamp)
            pos_list.pop(0)
            
             #Remove eaten food stamp
        if snake.pos() in pos_list[:-1]:
             turtle.goto(-400,150)
             turtle.write("game over! your score is: ", font=("Arial",55 , "normal"))
             turtle.goto(-100,75)
             turtle.write(str(score),font=("Arial", 55, "normal"))
             turtle.done()
             

            
        turtle.ontimer(move_snake,TIME_STEP)#end loop
    move_snake()

game=input("do you wanna play?")
if game=="yes":
    snake_game()
else:
    quit()

turtle.listen()

