#Rysowanie kwadratu

import turtle

# Set up the screen
window = turtle.Screen() #tworzymy okno na ktorym bedzie nasz zolw rysowal
window.bgcolor("lightgreen") #ustawiamy kolor tla na jasnozielony

# Create the turtle
pen = turtle.Turtle() #tworzymy zolwia ktorym bedziemy rysowac
pen.speed(5) #ustawiamy predkosc rysowania

# Side length
side_length = 100 #dlugosc boku kwadratu

# Draw a square
for i in range(4):
    pen.forward(side_length)
    pen.right(90)

# Hide the turtle and finish
pen.hideturtle() #chowamy nasz pisak czyli zolwia
window.mainloop() #okno pozostaje otwarte dopoki go sami nie zamkniemy