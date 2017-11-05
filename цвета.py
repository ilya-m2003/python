import turtle

screen = turtle.Screen()
screen.title('aaa')
screen.colormode(255)
t = turtle.Pen()
clr = (255,128,0)
sz = 10
r = 0
g = 0
b = 0
for n in range(153):
    x = n//51 + 1
    if (x == 1):
        r = r + 5
    elif (x == 2):
        g = g + 5
    else:
        b = b + 5
    clr = (r,g,b)
    t.color(clr)
    t.forward(sz)
    sz = sz+1
    t.left(90)

    
