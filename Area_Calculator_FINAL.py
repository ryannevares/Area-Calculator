"""
Author: Ryan Nevares
Version 2.5
Date: 10/17/2017
Area Calculator
This program will calculate the areas of various shapes.  First we will prompt the user for which shape they want to use, then ask for the measurements we need to calculate the area of the shape.  This is a complete rewrite of one of my earliest Python programs and attempts to do the exact same thing it did with ~100 fewer lines and fewer bugs :)
Enjoy!
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
        sleep(.09)

# Print initial message to the user
print ""
print_slow ("Area Calculator started successfully!")
sleep(.5)
print "The current time and date are: %s/%s/%s %s:%s \n" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

################# FUNCTION DEFINITIONS #################################
# This function will give the user a list of options
def printoptions():
    print "Options:"
    sleep(.5)
    option_list = ["C for circle", "T for triangle", "R for rectangle", "S for square", "P for parallelogram", "TD for trapazoid", "E for ellipse", "SR for sphere", "CN for cone", "CY for cylinder", "CB for cube"]
    for i in option_list:
        print i
        sleep(.1)
def print_hint(): # This is repeated several times, so we define it only once
    sleep(0.2)
    print "Don't forget to check your units!\n"
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
    print "Calculating...\n"
    sleep(2)
    return area

# Define a function to get user's input
def getInput():
    print ""
    option = raw_input("Enter shape here: ")
    option = option.upper()
    return option

# ask the user if they want to continue or quit
def again():
    playagain = raw_input("Perform another calculation? (y/n): ")
    if playagain == "y" or playagain == "Y":
        print "Alright!  Let's go! \n "
        sleep(1.5)
        calculate()
    elif playagain == "n" or playagain == "N":
        print " \nSorry to see you go, exiting now ...."
        sleep(.4)
        exit()
    else:
        print "Please choose y or n: \n"
        sleep (1)
        return again()

# Deals with bad values for shape dimensions
def bad_value():
    print "ERROR: Invalid values entered! \n"
    return calculate()
# Finally the main function!
def calculate():
    printoptions()
    option = getInput()
    """ For each possible option, make sure the input can be converted to a float.
    If it can, pass the float to the corresponding function.
    If not, call the calculate function.
    """
    if option == "C":
        print "You have selected CIRCLE"
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        if radius.isdigit():
            radius = float(radius)
            print "\nThe area of the circle is %.2f" % circle(radius)
            print_hint()
        else: bad_value()
    elif option == "T":
        print "You have selected TRIANGLE"
        sleep (.4)
        base = raw_input("Enter the length of the base: ")
        height = raw_input("Enter the height: ")
        if base.isdigit() and height.isdigit():
            base = float(base)
            height = float(height)
            print "\nThe area of the triangle is %.2f" % triangle(base, height)
            print_hint()
        else: bad_value()
    elif option == "R":
        print "You have selected RECTANGLE"
        sleep(.4)
        length = raw_input("Enter the length: ")
        width = raw_input("Enter the width: ")
        if length.isdigit() and width.isdigit():
            length = float(length)
            width = float(width)
            print "\nThe area of the rectangle is %.2f" % rectangle(length, width)
            print_hint()
        else: bad_value()
    elif option == "S":
        print "You have selected SQUARE"
        sleep(.4)
        side = raw_input("Enter the length of one side: ")
        if side.isdigit():
            side = float(side)
            print "\nThe area of the square is %.2f" % square(side)
            print_hint()
        else: bad_value()
    elif option == "P":
        print "You have selected PARALLELOGRAM"
        sleep(.4)
        base = raw_input("Enter the base: ")
        height = raw_input("Enter the height: ")
        if base.isdigit() and height.isdigit():
            base = float(base)
            height = float(height)
            print "\nThe area of the parallelogram is %.2f" % para(base,height)
            print_hint()
        else: bad_value()
    elif option == "TD":
        print "You have selected TRAPAZOID"
        sleep(.4)
        top = raw_input("Enter the length of the top: ")
        bottom = raw_input("Enter the length of the bottom: ")
        height = raw_input("Enter the height: ")
        if top.isdigit() and bottom.isdigit() and height.isdigit():
            top = float(top)
            bottom = float(bottom)
            height = float(height)
            print "\nThe area of the trapazoid is %.2f" % trap(top,bottom,height)
            print_hint()
        else: bad_value()
    elif option == "E":
        print "You have selected ELLIPSE"
        sleep(.4)
        longrad = raw_input("Enter the radius on the long axis: ")
        shortrad = raw_input("Enter the radius on the short axis: ")
        if longrad.isdigit() and shortrad.isdigit():
            longrad = float(longrad)
            shortrad = float(shortrad)
            print "\nThe area of the ellipse is %.2f" % ellipse(longrad,shortrad)
            print_hint()
        else: bad_value()
    elif option == "SR":
        print "You have selected SPHERE"
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        if radius.isdigit():
            radius = float(radius)
            print "\nThe surface area of the sphere is %.2f" % sphere(radius)
            print_hint()
        else: bad_value()
    elif option == "CN":
        print "You have selected CONE"
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        height = raw_input("Enter the height: ")
        if radius.isdigit() and height.isdigit():
            radius = float(radius)
            height = float(height)
            print "\nThe surface area of the cone is %.2f" % cone(radius,height)
            print_hint()
        else: bad_value()
    elif option == "CY":
        print "You have selected CYLINDER"
        sleep(.4)
        radius = raw_input("Enter the radius: ")
        height = raw_input("Enter the height: ")
        if radius.isdigit() and height.isdigit():
            radius = float(radius)
            height = float(height)
            print "\nThe surface area of the cylinder is %.2f" % cylinder(radius,height)
            print_hint()
        else: bad_value()
    elif option == "CB":
        print "You have selected CUBE"
        sleep(.4)
        side = raw_input("Enter the length of one side: ")
        if side.isdigit():
            side = float(side)
            print "\nThe surface area of the cube is %.2f" % cube(side)
            print_hint()
        else: bad_value()
    else: bad_value()
    return again()

# Call the main function
calculate()
