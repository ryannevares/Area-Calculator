"""
Author: Ryan Nevares
Version 2.6
Date: 11/2/2017
Area Calculator
This program will calculate the areas of various shapes.  First we will prompt the user for which shape they want to use, then ask for the measurements we need to calculate the area of the shape.  This is a complete rewrite of one of my earliest Python programs and attempts to do the exact same thing it did with ~100 fewer lines and fewer bugs :)
Enjoy!

Please report any bugs or suggestions to ryannevares@gmail.com
"""
# start by importing the commands we will need from other libraries
from math import pi, sqrt
from time import sleep
from datetime import datetime
from textwrap import fill
from sys import stdout
now = datetime.now() # simply print time & date when program starts

def print_slow(string):
    for letter in fill(string):
        stdout.write(letter)
        stdout.flush()
        sleep(.03)

# Print initial message to the user
print ""
print_slow ("Area Calculator started successfully!")
sleep(.5)
print "\nThe current time and date are: %s/%s/%s %s:%s \n" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

# This function will give the user a list of options
def printoptions():
    print "Options:"
    sleep(.5)
    option_list = ["C for circle", "T for triangle", "R for rectangle", "S for square", "P for parallelogram", "TD for trapazoid", "E for ellipse", "SR for sphere", "CN for cone", "CY for cylinder", "CB for cube", "Q to QUIT"]
    for i in option_list:
        print i
        sleep(.09)

def print_hint(): # This is repeated several times, so we define it only once
    sleep(0.2)
    print_slow ("Don't forget to check your units!")
    print "\n\n"

# Define functions for each possible shape
# Inputs must be in the form of floats, we will make sure they are floats later
def circle(radius):
    area = pi * (radius**2)
    return return_area(area)

def triangle(base, height):
    area = 0.5 * base * height
    return return_area(area)

def rectangle(length, width):
    area = length * width
    return return_area(area)

def square(side):
    area = side**2
    return return_area(area)

def para(base, height):
    area = base * height
    return return_area(area)

def trap(top, bottom, height):
    area = ((top+bottom)/2) * height
    return return_area(area)

def ellipse(longrad, shortrad):
    area = pi * longrad * shortrad
    return return_area(area)

def sphere(radius):
    area = pi * (radius**2)
    return return_area(area)

def cone(radius, height):
    area = (pi*radius)*(radius+sqrt((height**2)+(radius**2)))
    return return_area(area)

def cylinder(radius, height):
    area = (2*pi*radius*height) + (2*pi*(radius**2))
    return return_area(area)

def cube(sidelength):
    area = 6 * (sidelength**2)
    return return_area(area)

# The last 3 lines of all the last 11 functions are the same, lets change that
def return_area(area):
    print_slow ("Calculating...")
    print ""
    sleep(1.5)
    return area

# Define a function to get user's input
def get_input():
    print ""
    option = raw_input("Enter shape here: ")
    option = option.upper()
    return option

# ask the user if they want to continue or quit
def again():
    playagain = raw_input("Perform another calculation? (y/n): ")
    if playagain == "y" or playagain == "Y":
        print_slow ("Alright!  Let's go!")
        print "\n\n\n"
        sleep(1.5)
        calculate()
    elif playagain == "n" or playagain == "N":
        print_slow ("Sorry to see you go.")
        print "\n\n\n\n"
        print_slow ("exiting now ....")
        print "\n\n"
        sleep(.4)
        exit()
    else:
        print_slow ("Please choose y or n")
        print "\n\n"
        sleep (1)
        return again()

# Deals with bad values for shape dimensions
def bad_value():
    print_slow ("ERROR: Invalid values entered!")
    print ""
    return calculate()
# Finally the main function!
def calculate():
    printoptions()
    option = get_input()

    """ For each possible option, make sure the input can be converted to a float.
    If it can, pass the float to the corresponding function.
    If not, call the calculate function.
    """

    if option == "C":
        print_slow ("You have selected CIRCLE")
        print ""
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        if radius.isdigit():
            radius = float(radius)
            print ""
            print_slow ("The area of the circle is %.2f" % circle(radius))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "T":
        print_slow ("You have selected TRIANGLE")
        print ""
        sleep (.4)
        base = raw_input("Enter the length of the base: ")
        height = raw_input("Enter the height: ")
        if base.isdigit() and height.isdigit():
            base = float(base)
            height = float(height)
            print ""
            print_slow ("The area of the triangle is %.2f" % triangle(base, height))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "R":
        print_slow ("You have selected RECTANGLE")
        print ""
        sleep(.4)
        length = raw_input("Enter the length: ")
        width = raw_input("Enter the width: ")
        if length.isdigit() and width.isdigit():
            length = float(length)
            width = float(width)
            print ""
            print_slow ("The area of the rectangle is %.2f" % rectangle(length, width))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "S":
        print_slow ("You have selected SQUARE")
        print ""
        sleep(.5)
        side = raw_input("Enter the length of one side: ")
        if side.isdigit():
            side = float(side)
            print ""
            print_slow ("The area of the square is %.2f" % square(side))
            print ""
            print_hint()
        else: bad_value()
    elif option == "P":
        print_slow ("You have selected PARALLELOGRAM")
        print ""
        sleep(.4)
        base = raw_input("Enter the base: ")
        height = raw_input("Enter the height: ")
        if base.isdigit() and height.isdigit():
            base = float(base)
            height = float(height)
            print ""
            print_slow ("The area of the parallelogram is %.2f" % para(base,height))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "TD":
        print_slow ("You have selected TRAPAZOID")
        print ""
        sleep(.4)
        top = raw_input("Enter the length of the top: ")
        bottom = raw_input("Enter the length of the bottom: ")
        height = raw_input("Enter the height: ")
        if top.isdigit() and bottom.isdigit() and height.isdigit():
            top = float(top)
            bottom = float(bottom)
            height = float(height)
            print ""
            print_slow ("The area of the trapazoid is %.2f" % trap(top,bottom,height))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "E":
        print_slow ("You have selected ELLIPSE")
        print ""
        sleep(.4)
        longrad = raw_input("Enter the radius on the long axis: ")
        shortrad = raw_input("Enter the radius on the short axis: ")
        if longrad.isdigit() and shortrad.isdigit():
            longrad = float(longrad)
            shortrad = float(shortrad)
            print ""
            print_slow ("The area of the ellipse is %.2f" % ellipse(longrad,shortrad))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "SR":
        print_slow ("You have selected SPHERE")
        print ""
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        if radius.isdigit():
            radius = float(radius)
            print ""
            print_slow ("The surface area of the sphere is %.2f" % sphere(radius))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "CN":
        print_slow ("You have selected CONE")
        print ""
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        height = raw_input("Enter the height: ")
        if radius.isdigit() and height.isdigit():
            radius = float(radius)
            height = float(height)
            print ""
            print_slow ("The surface area of the cone is %.2f" % cone(radius,height))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "CY":
        print_slow ("You have selected CYLINDER")
        print ""
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        height = raw_input("Enter the height: ")
        if radius.isdigit() and height.isdigit():
            radius = float(radius)
            height = float(height)
            print ""
            print_slow ("The surface area of the cylinder is %.2f" % cylinder(radius,height))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "CB":
        print_slow ("You have selected CUBE")
        print ""
        sleep(.4)
        side = raw_input("Enter the length of one side: ")
        if side.isdigit():
            side = float(side)
            print ""
            print_slow ("The surface area of the cube is %.2f" % cube(side))
            print ""
            print_hint()
            sleep(.5)
        else: bad_value()
    elif option == "Q":
        print_slow ("Sorry to see you go.")
        print "\n\n\n\n"
        print_slow ("exiting now ....")
        print "\n\n"
        sleep(.4)
        exit()
    else: bad_value()
    return again()

# Call the main function
calculate()
