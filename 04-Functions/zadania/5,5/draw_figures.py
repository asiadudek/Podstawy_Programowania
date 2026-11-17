

import turtle
import figures #importujemy nasz wlasny modul z funkcjami rysujacymi figury

# Set up the screen
window = turtle.Screen() #tworzymy okno na ktorym bedzie nasz zolw rysowal
window.bgcolor("lightgreen") #ustawiamy kolor tla na jasnozielony

# Create the turtle
pen = turtle.Turtle() #tworzymy zolwia ktorym bedziemy rysowac
pen.speed(5) #ustawiamy predkosc rysowania

# Side length
side_length = 100 #dlugosc boku kwadratu i trojkata
length_a = 100 #pierwszy bok prostokata
length_b = 50 #drugi bok prostokata

# Draw figures
figures.draw_square(pen, side_length) #wywolujemy funkcje
figures.draw_triangle(pen, side_length)
figures.draw_rectangle(pen, length_a,length_b)

# Hide the turtle and finish
pen.hideturtle() #chowamy ikone zolwia
window.mainloop() #okno pozostaje otwarte dopoki go sami nie zamkniemy