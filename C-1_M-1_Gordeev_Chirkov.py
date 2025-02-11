#This case has been done by Sergey Chirkov and Mihail Gordeev
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

def main(speed): #def for drawing puzzle ang figures
    t.speed(speed)
    size = 80 * m.sqrt(2)

    def puzzle():
        square(0, 0, 80, 45, color='orange')
        triangle(0, 0, 80, 0, color='orchid')
        triangle(0, 0, 160, 180, color='brown2')
        triangle(0, 0, 160, -90, color='yellow2')
        triangle((80/m.sqrt(2)), (80 / m.sqrt(2)), 80, 90, color='darkorchid2')
        triangle((160/m.sqrt(2)), -(160 /m.sqrt(2)), (160/m.sqrt(2)), -135, color='deepskyblue')
        parallelogram(-(80/m.sqrt(2)), -(80 /m.sqrt(2)), 80, 0, 'chartreuse3')

    def rabbit():
        triangle(-200, 1.4*size, 80, 135, color='darkorchid2')
        triangle(-200, 1.4*size, (160/m.sqrt(2))/2, -135, color='deepskyblue')
        triangle(-200 - (160/m.sqrt(2))/2, 1.4*size + 80, 80, 45, color='yellow2')
        triangle(-200, 1.4*size + 80, 80, -135, color='brown2')
        triangle(-200, 1.4*size + 80, 40, -225, color='orchid')
        square(-200, 1.4*size + 180, 40, 0, color='orange')
        parallelogram(-220, 1.4*size + 180, 40, 135, 'chartreuse3')

    def left_person():
        triangle(-202 - (160/m.sqrt(2))/4, -size * 0.8, 40, 90, color='darkorchid2')
        triangle(-160, -size * 0.5, (160/m.sqrt(2))/2, -90, color='deepskyblue')
        triangle(-202, -size * 0.4, 80, -135, color='yellow2')
        triangle(-312, -size * 0.3, 40, 45, color='orchid')
        triangle(-240, size * 0.7, 80, 45, color='brown2')
        square(-220, size *0.72, 40, 135, color='orange')
        parallelogram(-282, size *0.35, 40, 45, 'chartreuse3')

    def fish():
        square(-16, 192, 33.3, 45, color='orange')
        triangle(-16+(size/2.4), 258.6, 66.6, -45, color='brown2')
        triangle(-16+(size/2.4), 125.3, 66.6, -135, color='yellow2')
        triangle(-16+(size/2.4)+m.sqrt(2)*(size/2.4)**2/(2*(size/2.4)), 192, size/2.4, -90, color='deepskyblue')
        parallelogram(-49.3, 192, 33.3, 135, color='chartreuse3')
        triangle(-49.3, 192, 33.3, 45, color='orchid')
        triangle(-49.3, 158.6, 33.3, -135, color='darkorchid2')

    def rocket(): #some x\y position need optimized throw photomath
        triangle(200, -size, 40, 0, color='orchid')
        triangle(228, - size - (160 / m.sqrt(2))/3.8, (160 / m.sqrt(2))/2, -45, color='deepskyblue')
        triangle(228, - size - (160 / m.sqrt(2))/3.8 - (160 / m.sqrt(2))/1.95, 80, -90, color='yellow2')
        triangle(172, - size - (160 / m.sqrt(2))/3.8 - (160 / m.sqrt(2))/0.975, 80, 90, color='brown2')
        square(172, - size - (160 / m.sqrt(2))/3.8 - (160 / m.sqrt(2))/0.955, 40, -45, color='orange')
        triangle(172, - size - (160 / m.sqrt(2))/3.8 - (160 / m.sqrt(2))/0.955 - (160 / m.sqrt(2))/2, 40, -90, color='darkorchid2')
        parallelogram(256, - size - (160 / m.sqrt(2))/3.8 - (160 / m.sqrt(2))/0.955 - (160 / m.sqrt(2))/4, 40, -90, 'chartreuse3')

    def right_person():
        square(220, size * 0.72, 40, 135, color='orange')
        triangle(220, size * 0.72, 80, 45, color='yellow2')
        triangle(220, size * 0.72, 80, -45, color='brown2')
        parallelogram(220, -40, 40, -135, 'chartreuse3')
        triangle(220, -(160/m.sqrt(2))/2, (160 / m.sqrt(2)) / 2, 135, color='deepskyblue')
        triangle(300, -(160/m.sqrt(2))/2, 40, -45, color='darkorchid2')
        triangle(200, -(160/m.sqrt(2))/2-45, 40, -135, color='orchid')

    def peafowl():
        triangle(185, 192, 66.6, 45, color='yellow2')
        triangle(185, 225.3, 66.6, -45, color='brown2')
        triangle(185 - (size / 2.4) * m.sqrt(2) / 2, 225.3 + m.sqrt(2) * (size / 2.4) ** 2 / (2 * (size / 2.4)), size / 2.4, 0, color='deepskyblue')
        parallelogram(118.3, 225.3 - m.sqrt(2) * (33.3), 33.3, 90, color='chartreuse3')
        square(251.6, 192, 33.3, 180, color='orange')
        triangle(243, 225.3 + m.sqrt(2) * (33.3) ** 2 / (66.6), 33.3, 0, color='orchid')
        triangle(206.3, 145, 33.3, 90, color='darkorchid2')

    def cat():
        square(-200, -size*1.5, 40, -45, color='orange')
        triangle(-200, -size*1.485, 40, 90, color='orchid')
        triangle(-200, -size*1.485, 40, -90, color='darkorchid2')
        triangle(-220, -size*2.2, (80/m.sqrt(2)), 90, color='deepskyblue')
        triangle(-122, -size*2.5, 80, -90, color='yellow2')
        triangle(-122, -size*3.23, 80, -135, color='brown2')
        parallelogram(-122, -size*2.9, 40, 45, 'chartreuse3')

    def helicopter():
        triangle(-15+(size/2.4)+m.sqrt(2)*(66.6)**2/(2*66.6), -207, 66.6, -90, color='brown2')
        triangle(-17+(size/2.4)-m.sqrt(2)*(66.6)**2/(2*66.6), -207, 66.6, 90, color='yellow2')
        parallelogram(-9+(size/2.4)+23, -2.4*80+size/2.4, 80/2.4, 0, color='chartreuse3')
        triangle(-25+(size/2.4)-size/(2*2.4), 31-2.4*80+m.sqrt(2)*(80*m.sqrt(2)/2.4)**2/(2*(size/2.4)), size/2.4, 0, color='deepskyblue')
        triangle(-63+(size/2.4), -2.4*80-15, 80/2.4, 0, color='darkorchid2')
        triangle(-41+(size/2.4)-size/2.4, -15-2.4*80-m.sqrt(2)*(33.3)**2/(2*33.3), 33.3, 180, color='orchid')
        square(-97+(size/2.4)-size/2.4, 20-2.4*80-m.sqrt(2)*(33.3)**2/(2*33.3), 33.3, 45, color='orange')

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