#Create a class that represents a simple circle
class Circle():
    def __init__(self,radius): #Put radius as its parameter
        self.radius = radius
    #Make a method that computes the circle's area
    def area(self): #Accepts radius as its parameter
        area = 3.14 * self.radius**2    #Rounding pi to 3.14 for simplicity
        return area
    #Modify the __str__ method to print the details of the circle
    def __str__(self):
        return(f"Circle is with radius {self.radius}")
    #Modify the __add__ method to add two circles together
    def __add__(self,other_circle): #Other circle as a parameter
        return Circle(self.radius + other_circle.radius) #Return a new combined circle object
    #Modify the __gt__ (greater than) to compare which one is bigger
    def __gt__(self,other_circle): #Other circle as a parameter
        if self.radius > other_circle:
            return True
        else:
            return False
    #Modify the __eq__(equal to) based on radius
    def __eq__(self, other_circle):
        if self.radius == other_circle:
            return True
        else:
            return False
    
    #Enable sorting by radius
    def __lt__(self,other_circle):
        return self.radius < other_circle #Now sorted sorts the circles by radius, not alphabets
    
#Test methods
c1 = Circle(200)
c2 = Circle(100)
c3 = Circle(50) 

#Test string output 
print(str(c1)) #Should print Circle is with radius 3
print("Area of c1:", c1.area())  # Should print 28.26
c4 = c1 + c2
print(c4)  # Should be a new Circle with radius 8

#Test equality and comparison:
print(c1 == c3)  # True
print(c1 > c2)   # False
print(c2 > c1)   # True

#Test sorting
circles = [c2, c1, c3]
circles.sort()
for c in circles:
    print(c) # Sorted by radius: 3, 3, 5

#Do bonus
import turtle

# Setup screen
screen = turtle.Screen() #Put a screen for the turtle graphics
screen.bgcolor("white") #Make background color white

pen = turtle.Turtle() #Make pen a turtle object
pen.speed("slowest") #Make the pen speed the slowest

# Start position
x = -200 #Start 200 pixels to the left from the center

for circle in circles: #For each circle
    pen.penup() #Go op until half of circle
    pen.goto(x, 0 - circle.radius)  # Go to position and center the circle vertically
    pen.pendown() #Go down to continue other half of circle
    pen.circle(circle.radius) 
    x += circle.radius * 2 + 10  # Move to the right for the next circle

# This keeps the animation running
screen.mainloop()

    
        