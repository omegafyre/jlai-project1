import turtle
import random
honors=turtle.Turtle()
wn = turtle.Screen()
def randomturn(turtle):
    '''this function will have the turtle face either left, south, or right'''
    a=random.randint(0,2)
    if a==0:
        turtle.setheading(0)
    if a==1:
        turtle.setheading(180)
    if a==2:
        turtle.setheading(270)
def squaredraw(length, turtle):
    '''draws a square with a given length, centered at a given turtle's position'''
    turtle.up()
    turtle.backward(length/2)
    turtle.down()
    turtle.right(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2) 
    turtle.up()
def appender(turtle,steps,alist):
    import random
    '''this function causes the turtle to go backwards a given number of steps,append its current position into a list, and draw a square that is 5 units long'''
    turtle.backward(int(steps))
    b=int(turtle.xcor()),int(turtle.ycor())
    alist.append(b)
    squaredraw(5,turtle)
    turtle.goto(random.randint(-200,200),200)
    turtle.setheading(270)

def DLA_simulator(turtle,particle_amount):
    '''this function will utilize a turtle to simulate the diffusion limiter aggregation phenomenon, showing how dendrites are formed in the natural world, with a given number of particles to simulate'''
    turtle.speed(0)
    turtle.goto(0,0)
    squaredraw(5,turtle)
    turtle.up()
    turtle.goto(0,200)
    turtle.right(90)
    counter=0
    touchedpoints=[(0,0)]
    while counter < particle_amount+1:
        turtle.up()
        randomturn(turtle)
        turtle.forward(int(5))        
        if (int(turtle.xcor()),int(turtle.ycor())) in touchedpoints or int(turtle.ycor())<=-201:
            appender(turtle,5,touchedpoints)
            counter+=1
DLA_simulator(honors,5000)



