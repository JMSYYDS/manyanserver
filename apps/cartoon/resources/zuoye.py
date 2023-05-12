from datetime import datetime
import turtle

name = []


def drawLine(draw):  # 绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawLine1(draw):  # 绘制单段数码管1
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(20)


def drawtdown1(draw):  # 斜线
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(44.7)


def drawDigit(digit):  # 根据数字绘制七段数码管
    # 横1笔
    drawLine1(True) if digit in [2, 4, 5, 6, 8, 9, 'A', 'E', 'F', 'H', 'K', 'P', 'R', 'S'] else drawLine1(False)

    # 横2笔
    drawLine1(True) if digit in [2, 3, 4, 5, 6, 8, 9, 'F', 'A', 'B', 'G', 'H', 'P,'R',S'] else drawLine1(False)

    # 第3笔
    turtle.right(90)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'D', 'G', 'H', 'J', 'M', 'N', 'O', 'Q', 'S', 'U',
                                'W'] else drawLine(False)

    # 第4笔
    drawLine(True) if digit in ['L', 0, 2, 3, 5, 6, 8, 9, 'B', 'C', 'D', 'E', 'G', 'I', 'U', 'J', 'O', 'Q', 'S',
                                'Z'] else drawLine(False)

    # 第5笔
    drawLine(True) if digit in ['L', 0, 2, 6, 8, 'A', 'C', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'U', 'V', 'W'] else drawLine(False)

    # 第6笔（因为会右转，这里调节第五笔为向上直线）
    turtle.left(90)
    drawLine(True) if digit in ['L', 0, 4, 5, 6, 8, 9, 'A', 'C', 'E', 'F', 'G', 'H', 'K', 'M', 'N', 'O', 'P', 'Q', 'R',
                                'S', 'U', 'V', 'W'] else drawLine(False)

    # 第7笔
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'O', 'P', 'Q', 'R', 'I', 'S',
                                'T', 'Z'] else drawLine(False)

    # 第8笔
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9, 'A', 'B', 'D', 'H', 'J', 'M', 'N', 'O', 'P', 'Q', 'R', 'U',
                                'W'] else drawLine(False)

    # 第9笔
    turtle.left(90)
    turtle.penup()
    turtle.fd(40)
    turtle.right(90 + 63.4)
    drawtdown1(True) if digit in ['K', 'N', 'Q', 'K', 'N', 'Q', 'R', 'W', 'X'] else drawtdown1(False)

    # 第10笔********************
    drawtdown1(True) if digit in ['M', 'N', 'X', 'Y'] else drawtdown1(False)

    # 第11笔********************
    turtle.right(90 + 26.6)
    turtle.penup()
    turtle.fd(20)
    turtle.right(90)
    drawLine(True) if digit in ['B', 'D', 'I', 'T'] else drawLine(False)

    # 第12笔***********
    turtle.left(90)
    drawLine(True) if digit in ['B', 'D', 'I', 'T', 'Y'] else drawLine(False)

    # 第13笔
    turtle.penup()
    turtle.fd(20)
    turtle.right(90 + 26.6)
    drawtdown1(True) if digit in ['V', 'X', 'Z', 'W', 0] else drawtdown1(False)

    # 第14笔
    drawtdown1(True) if digit in ['M', 'V', 'X', 'Y', 'Z', 'K', 0, 1] else drawtdown1(False)
    turtle.right(90 + 63.4)
    turtle.penup()
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(20)


def drawDate(date):
    turtle.pencolor("black")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 25, "normal"))
            turtle.pencolor("black")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 25, "normal"))
            turtle.pencolor("black")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 25, "normal"))
        else:
            drawDigit(eval(i))


def drawname():
    name = ['J', 'M', 'S']
    for i in name:
        drawDigit(i)


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.goto(-300, 50)
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.speed(0)
    nowTime = datetime.now().strftime("%Y-%m=%d+")
    drawDate(nowTime)
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pencolor('red')
    drawname()
    turtle.hideturtle()
    turtle.exitonclick()


main()
