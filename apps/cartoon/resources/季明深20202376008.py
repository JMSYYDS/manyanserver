import turtle as x
import datetime

def drawgap():
    x.penup()
    x.pencolor("skyblue")
    x.fd(0)
def drawline(draw):
    drawgap()
    x.pendown() if draw else x.penup()
    x.fd(40)
    drawgap()
    x.right(90)
def drawdigit(digit):
    x.write('距离毕业还有:', font=("Timesnewromans",50,"normal"))
    x.fd(500)
    i=0
    while i < len(digit):
        if digit[i] >= '0' and digit[i] <= '9':
            digit1 = eval(digit[i])
            drawline(True) if digit1 in [2,3,4,5,6,8,9] else drawline(False)
            drawline(True) if digit1 in [0,1,3,4,5,6,7,8,9] else drawline(False)
            drawline(True) if digit1 in [0,2,3,5,6,8,9] else drawline(False)
            drawline(True) if digit1 in [0,2,6,8] else drawline(False)
            x.left(90)
            drawline(True) if digit1 in [0,4,5,6,8,9] else drawline(False)
            drawline(True) if digit1 in [0,2,3,5,6,7,8,9] else drawline(False)
            drawline(True) if digit1 in [0,1,2,3,4,7,8,9] else drawline(False)
            x.left(180)
            x.penup()
            x.fd(20)
        else:
            break
        i=i+1

def main():
    x.setup(1200,600,200,200)
    x.penup()
    x.fd(-300)
    x.pensize(5)
    x.hideturtle()
    remain = datetime.datetime(2024,6,20) -datetime.datetime.now()
    s = str(remain)
    x.speed(15)
    drawdigit(s)
    x.write('天', font=("Timesnewromans",50,"normal"))
    x.hideturtle()
    x.done()
main()
