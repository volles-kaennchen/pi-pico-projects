import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['white','red','orange','yellow','green','blue','purple','white'] 

t.speed(0)

for number in range(1600): 
    t.forward(number+1) 
    t.right(89) 
    t.pencolor(colors[number % len(colors)])

    print(f"Schleifenindex: {number}, Farbe: {t.pencolor()}")

turtle.done()
