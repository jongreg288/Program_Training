import turtle

screen = turtle.Screen() # Create a screen object to display the turtle graphics
screen.canvheight = 400 # Set the height of the canvas to 400 pixels
screen.canvwidth = 400 # Set the width of the canvas to 400 pixels
screen.bgcolor("#9f9f9f") # Set the background color of the screen to gray

timmy = turtle.Turtle() # Create a turtle object named timmy. timmy = object of the class Turtle
timmy.shape("turtle") # Set the shape of the turtle to "turtle"
timmy.color("blue") # Set the color of the turtle to blue
timmy.forward(100) # Move the turtle forward by 100 units
timmy.left(90) # Turn the turtle left by 90 degrees
timmy.forward(50) # Move the turtle forward by 50 units

screen.exitonclick() # Wait for a mouse click on the screen to exit the program. Method = exitonclick().
