#绘制四面国旗
import turtle as t
t.speed(10)
def face(x,y):
    t.penup()
    #t.goto(-300,200)
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.color("black","red")
    t.begin_fill()
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.end_fill()

#大星星
def big_star(x,y):
    t.penup()
    #t.goto(-280,160)
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.color("yellow")
    t.begin_fill()
    t.forward(57)    #大星星边长57
    t.right(180-36)
    t.forward(57)
    t.right(180-36)
    t.forward(57)
    t.right(180-36)
    t.forward(57)
    t.right(180-36)
    t.forward(57)
    t.end_fill()
    t.hideturtle()
#big_star(-280,160)
    
#小星星
def small_star(x,y,angle,jiao):
    t.penup()
    #t.goto(-200,180)
    t.color("yellow")
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.forward(10)    #小星星外接圆半径10
    t.seth(jiao)
    for i in range(5):
        t.left(180-36)
        t.forward(19)
    t.end_fill()
'''
small_star(-200,180,-149,-131)
small_star(-180,160,-172,-154)
small_star(-180,130,163.96,181.6)
small_star(-200,110,140.19,158.19)
'''
def flag(a,b,x,y,x0,y0,x1,y1,x2,y2,x3,y3):
    face(a,b)
    face(a+300,b)
    face(a,b-200)
    face(a+300,b-200)
    
    big_star(x,y)
    big_star(x+300,y)
    big_star(x,y-200)
    big_star(x+300,y-200)
    
    small_star(x0,y0,-149,-131)
    small_star(x1,y1,-172,-154)
    small_star(x2,y2,163.96,181.6)
    small_star(x3,y3,140.19,158.19)
    
    small_star(x0+300,y0,-149,-131)
    small_star(x1+300,y1,-172,-154)
    small_star(x2+300,y2,163.96,181.6)
    small_star(x3+300,y3,140.19,158.19)
    
    small_star(x0,y0-200,-149,-131)
    small_star(x1,y1-200,-172,-154)
    small_star(x2,y2-200,163.96,181.6)
    small_star(x3,y3-200,140.19,158.19)
    
    small_star(x0+300,y0-200,-149,-131)
    small_star(x1+300,y1-200,-172,-154)
    small_star(x2+300,y2-200,163.96,181.6)
    small_star(x3+300,y3-200,140.19,158.19)

flag(-300,200,-280,160,-200,180,-180,160,-180,130,-200,110)   



