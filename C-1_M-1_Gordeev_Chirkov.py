#This case has been done by Mihail Gordeev and Sergey Chirkov
import turtle as t # main modul for drawing
import math as m #support modul for calculation with triangle's ang parallelogram's

def square(x, y, l, angle, color): #x,y - coordinates, l - length
    t.up()
    t.pen(pencolor='white', fillcolor=color, pensize=1) #settings of pen
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90 + angle) #rotating back for another figures
    t.end_fill()
    t.up()

def triangle(x, y, l, angle, color): #x,y - coordinates, l - length
    t.pen(pencolor='white', fillcolor=color, pensize=1) #settings of pen
    t.setposition(x, y)
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.right(45)
    t.forward(l)
    t.right(135)
    t.forward(l * m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45 + angle) #rotating back for another figures
    t.end_fill()
    t.up()

def parallelogram(x, y, l, angle, color): #x,y - coordinates, l - length
    t.up()
    t.pen(pencolor='white', fillcolor=color, pensize=1)
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.forward(l*m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45)
    t.forward(l*m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45+angle) #rotating back for another figures
    t.up()
    t.end_fill()

def main(speed):
#def for drawing puzzle ang figures
#some x\y position has been chosen by calculus and selection
#size of figure - 33.3 for small triangle and, 66.6 for middle triangle
    t.speed(speed)
    size = 80 * m.sqrt(2) #hypotenuse for the middle triangle in puzzle

    def puzzle():
        square(0, 0, 80, 45, 'orange')
        triangle(0, 0, 80, 0, 'orchid')
        triangle(0, 0, 160, 180, 'brown2')
        triangle(0, 0, 160, -90, 'yellow2')
        triangle((80/m.sqrt(2)), (80 / m.sqrt(2)), 80, 90, 'darkorchid2')
        triangle((160/m.sqrt(2)), -(160 /m.sqrt(2)), (160/m.sqrt(2)), -135, 'deepskyblue')
        parallelogram(-(80/m.sqrt(2)), -(80 /m.sqrt(2)), 80, 0, 'chartreuse3')

    def rabbit():
        triangle(-251.6, 158.6, 66.6, 45, 'yellow2')
        triangle(-185, 159.6, 66.6, -135, 'brown2')
        triangle(-160, 158.6, 33.3, -90, 'orchid')
        square(-185, 239.2, 33.3, 0, 'orange')
        parallelogram(-201.6, 239.2, 33.3, 135, 'chartreuse3')
        triangle(-250.6+size/2.4, 92, size/2.4, -135, 'deepskyblue')
        triangle(-249.6+size/2.4, 92, 33.3, 135, 'darkorchid2')

    def left_person():
        triangle(-204.3, -109.7, 33.3, 90, 'darkorchid2')
        triangle(-146.3, -75.7, size/2.4, -90, 'deepskyblue')
        triangle(-181.3, -71.7, 66.6, -135, 'yellow2')
        triangle(-271.2, -60.7, 33.3, 45, 'orchid')
        triangle(-206.3, 38.3, 66.6, 45, 'brown2')
        square(-195.3, 38.3, 33.3, 135, 'orange')
        parallelogram(-240.3, 6.3, 33.3, 45, 'chartreuse3')

    def right_person():
        square(206.3, 38.3, 33.3, 135, 'orange')
        triangle(207.3, 38.3, 66.6, 45, 'yellow2')
        triangle(206.3, 38.3, 66.6, -45, 'brown2')
        parallelogram(206.3, -60.6, 33.3, -135, 'chartreuse3')
        triangle(207.3, -28.3-size/2.4, size/2.4, 135, 'deepskyblue')
        triangle(222.3+size/2.4, -29.3-size/2.4, 33.3, -45, 'darkorchid2')
        triangle(186.3, -67.6-size/2.4, 33.3, -135, 'orchid')

    def fish():
        square(-16, 192, 33.3, 45, 'orange')
        triangle(-16+(size/2.4), 258.6, 66.6, -45, 'brown2')
        triangle(-16+(size/2.4), 125.3, 66.6, -135, 'yellow2')
        triangle(-16+(size/2.4)+m.sqrt(2)*(size/2.4)**2/(2*(size/2.4)), 192, size/2.4, -90, 'deepskyblue')
        parallelogram(-49.3, 192, 33.3, 135, 'chartreuse3')
        triangle(-49.3, 192, 33.3, 45, 'orchid')
        triangle(-49.3, 158.6, 33.3, -135, 'darkorchid2')

    def rocket():
        triangle(200, -size, 33.3, 0, 'orchid')
        triangle(223, - size - (133.2 / m.sqrt(2))/3.8, (133.2 / m.sqrt(2))/2, -45, 'deepskyblue')
        triangle(223, - size - (133.2 / m.sqrt(2))/3.8 - (133.2 / m.sqrt(2))/1.95, 66.6, -90, 'yellow2')
        triangle(176, - size - (133.2 / m.sqrt(2))/3.8 - (133.2 / m.sqrt(2)), 66.6, 90, 'brown2')
        square(176, - size - (133.2 / m.sqrt(2))/3.8 - (133.2 / m.sqrt(2)), 33.3, -45, 'orange')
        triangle(176, - size - (133.2 / m.sqrt(2))/3.8 - (133.2 / m.sqrt(2)) - (133.2 / m.sqrt(2))/2, 33.3, -90,
                 'darkorchid2')
        parallelogram(247, - size - (133.2 / m.sqrt(2))/3.8 - (133.2 / m.sqrt(2)) - (133.2 / m.sqrt(2))/4, 33.3,
                      -90, 'chartreuse3')

    def peafowl():
        triangle(185, 192, 66.6, 45, 'yellow2')
        triangle(185, 225.3, 66.6, -45, 'brown2')
        triangle(185 - (size / 2.4) * m.sqrt(2) / 2, 225.3 + m.sqrt(2) * (size / 2.4) ** 2 / (2 * (size / 2.4)),
                 size / 2.4, 0, 'deepskyblue')
        parallelogram(118.3, 225.3 - m.sqrt(2) * 33.3, 33.3, 90, 'chartreuse3')
        square(251.6, 192, 33.3, 180, 'orange')
        triangle(243, 225.3 + m.sqrt(2) * 33.3 ** 2 / 66.6, 33.3, 0, 'orchid')
        triangle(210.3, 149, 33.3, 90, 'darkorchid2')

    def cat():
        square(-200, -size*1.5, 33.3, -45, 'orange')
        triangle(-200, -size*1.5, 33.3, 90, 'orchid')
        triangle(-200, -size*1.5, 33.3, -90, 'darkorchid2')
        triangle(-220, -size*2.1, (66.6/m.sqrt(2)), 90, 'deepskyblue')
        triangle(-140, -size*2.4, 66.6, -90, 'yellow2')
        triangle(-140, -size*3, 66.6, -135, 'brown2')
        parallelogram(-140, -size*2.70, 33.3, 45, 'chartreuse3')

    def helicopter():
        triangle(-16+(size/2.4)+m.sqrt(2)*66.6**2/(2*66.6), -207, 66.6, -90, 'brown2')
        triangle(-17+(size/2.4)-m.sqrt(2)*66.6**2/(2*66.6), -207, 66.6, 90, 'yellow2')
        parallelogram(-9+(size/2.4)+17, -2.4*80+size/2.4+7, 80/2.4, 0, 'chartreuse3')
        triangle(-25+(size/2.4)-size/(2*2.4), 31-2.4*80+m.sqrt(2)*(80*m.sqrt(2)/2.4)**2/(2*(size/2.4)), size/2.4,
                 0, 'deepskyblue')
        triangle(-63+(size/2.4), -2.4*80-15, 80/2.4, 0, 'darkorchid2')
        triangle(-41+(size/2.4)-size/2.4, -15-2.4*80-m.sqrt(2)*33.3**2/66.6, 33.3, 180, 'orchid')
        square(-97+(size/2.4)-size/2.4, 20-2.4*80-m.sqrt(2)*33.3**2/66.6, 33.3, 45, 'orange')

    puzzle()

    rabbit()
    fish()
    peafowl()
    right_person()
    rocket()
    helicopter()
    cat()
    left_person()

    t.mainloop()

main(100) #speed of drawing
