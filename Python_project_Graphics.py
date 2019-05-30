from graphics import *
import random, time
def main():
    win = GraphWin('The Maze', 500, 500)
    
    win.setBackground('black')

    for i in range(50):
        
        drawCir(win)
        time.sleep(.005)
    
    for i in range(5, 30):
        o = Oval(Point(50-i*5,250-i*10), Point(450+i*5,250+i*10))
        o.setFill('black')
        o.draw(win)
        message = Text(Point(250, 250), 'Welcome to the Maze')
        message.setTextColor('white')
        message.setFace('courier')
        message.setStyle('bold')
        message.setSize(i)
        message.draw(win)
        time.sleep(.001)

    instr=Text(Point(250, 350), 'Click anywhere to begin')
    instr.setStyle('italic')
    instr.setTextColor('gray')
    instr.setSize(15)
    instr.draw(win)

    win.getMouse()
    instr.undraw()
    message.undraw()

    color = 'white'
    global life
    while life>0:
        rect=Rectangle(Point(0,0), Point(500,500))
        rect.setFill('black')
        rect.draw(win)

        instr.setText('Choose one way; if nothing happens, choose another.')
        instr.setSize(15)
        instr.draw(win)

        hp = Text(Point(250, 50), 'Lives left:'+str(life))
        hp.setSize(20)
        hp.setFill('white')
        hp.setFace('courier')
        hp.draw(win)
        
        path1=Circle(Point(500/6,250), 60)
        path1.setFill(color)
        path1.draw(win)
        path2=Circle(Point(500/2,250), 60)
        path2.setFill(color)
        path2.draw(win)
        path3=Circle(Point(2500/6,250), 60)
        path3.setFill(color)
        path3.draw(win)
        pathway(hp,win,path1,path2,path3)
        path1.undraw()
        path2.undraw()
        path3.undraw()
        instr.undraw()


    message.setText('Game over')
    message.draw(win)
    for i in range(0,50,5):
        rect.undraw()
        message.undraw()
        r=250-i*5
        color = color_rgb(r, 0, 0)
        a=250-i*5
        color_back = color_rgb(a,a,a)
        rect.setFill(color_back)
        rect.draw(win)
        message.setTextColor(color)
        message.draw(win)
        time.sleep(.025)
    message.undraw()
    message.setTextColor('red')
    message.draw(win)
    instr.setText('Click anywhere to exit')
    instr.draw(win)
    win.getMouse()
    win.close()
def pathway(hp,win,path1,path2,path3):
    global life

    count=0
    correct = random.randint(1,3)
    while count<3:
        
        p = win.getMouse()
        if inside(p, path1) or inside(p, path2) or inside(p, path3):
            count = count + 1
            
            if count==correct and inside(p, path1):
                for i in range(5, 30):
                    path1=Circle(Point(500/6,250), 60+20*i)
                    path1.setFill('white')
                    path1.draw(win)
                    time.sleep(.001)
                life=life+1
                break
            elif count==correct and inside(p, path2):
                for i in range(5, 30):
                    path2=Circle(Point(500/2,250), 60+20*i)
                    path2.setFill('white')
                    path2.draw(win)
                    time.sleep(.001)
                life=life+1
                break
            elif count==correct and inside(p, path3):
                for i in range(5, 30):
                    path3=Circle(Point(2500/6,250), 60+20*i)
                    path3.setFill('white')
                    path3.draw(win)
                    time.sleep(.001)
                life=life+1
                break
            else:
                if inside(p, path1):
                    path1.undraw()
                if inside(p, path2):
                    path2.undraw()
                if inside(p, path3):
                    path3.undraw()
                hp.undraw()
                life=life-1
                hp.setText('Lives left:'+str(life))
                hp.draw(win)
                if life==0:
                    break
def drawCir(win):
        r = random.randrange(10,255)
        b = random.randrange(10,255)
        g = random.randrange(10,255)
        color = color_rgb(r, g, b)
        
        radius = random.randrange(50, 100)
        x = random.randrange(5, 495)
        y = random.randrange(5, 495)

        path=Circle(Point(x,y), radius)
        path.setFill(color)
        path.draw(win)
def inside(p, path):
    return all([p.getX()>=path.getP1().getX(),p.getX()<=path.getP2().getX(), \
                p.getY()>=path.getP1().getY(),p.getY()<=path.getP2().getY()])
life=3
main()
