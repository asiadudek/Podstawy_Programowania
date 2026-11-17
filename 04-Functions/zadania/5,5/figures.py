
import turtle

def draw_square(pen,length): #kazda funkcja dostaje pen jako pierwszy argument
    for i in range(4): #petla wykona sie 4 razy (kwadrat ma 4 boki)
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen,length): #trojkat rownoboczny
    pen.penup() #podnosimy pisak aby nie rysowac w tym samym miejscu co kwadrat
    pen.goto(-100,100) #przenosimy pisak na takie wspolrzedne
    pen.pendown() #opuszczamy pisak
    for i in range(3): #petla wykona sie 3 razy (trojkat ma 3 boki)
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b): #prostokat
    pen.penup()
    pen.goto(-250,200)
    pen.pendown()
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
        