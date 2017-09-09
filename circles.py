import Tkinter # built-in Python graphics library
import random

game_objects = []

class Shape:
    def __init__(self, x, y):
        '''Create a new circle at the given x,y point with a random speed, color, and size.'''
        self.x = x
        self.y = y
        self.x_speed = random.randint(-5,5)
        self.y_speed = random.randint(-5,5)

        if (self.x_speed == 0) and (self.y_speed == 0):
            self.x_speed == 1
            self.y_speed == 1

        # this creates a random hex string between #000000 and #ffffff
        # we draw it with an outline, so we'll be able to see it on a white background regardless
        self.color = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.size = random.randint(5,75)
        self.shape = random.randint(1,2)

    def update(self):
        '''Update current location by speed.'''

        self.x += self.x_speed
        self.y += self.y_speed

        if self.x < 0 :
            self.x_speed = random.randint(0,5)
        if self.x > (400 - self.size) :
            self.x_speed = random.randint(-5,0)
        if self.y < 0:
            self.y_speed = random.randint(0,5)
        if self.y > (400 - self.size):
            self.y_speed = random.randint(-5,0)


class Circle(Shape):

    def draw(self, canvas):
        '''Draw self on the canvas.'''
        canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")

class Square(Shape):
    def draw(self, canvas):
        '''Draw self on the canvas.'''
        canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")
class SpecialSquare(Shape):

    def update(self):
        '''Update current location by speed.'''

        self.x += self.x_speed
        self.y += self.y_speed

        if self.x_speed < 20 and self.y_speed < 20:
            if self.x < 0 :
                self.x_speed = self.x_speed * -1.4
            if self.x > (400 - self.size) :
                self.x_speed = self.x_speed * -1.4
            if self.y < 0:
                self.y_speed = self.y_speed * -1.4
            if self.y > (400 - self.size):
                self.y_speed = self.y_speed * -1.4
        else:
            self.x_speed = 5
            self.y_speed = 5




    
    def draw(self, canvas):



        canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")

        
def addShape(event):
    '''Add a new circle where the user clicked.'''

    global game_objects

    shapeX = random.randint(0,350)
    shapeY = random.randint(0,350)

    
    constructor = random.choice((Circle, Square))
    game_objects.append(constructor(shapeX, shapeY))


def addSpecialSquare(event):
    '''Add a new circle where the user clicked.'''

    global game_objects




    x = random.randint(0,350)
    y = random.randint(0,350)
    game_objects.append(SpecialSquare(x, y))
    
 
    

def reset(event):
    '''Clear all game objects.'''

    global game_objects
    game_objects = []


def draw(canvas):
    '''Clear the canvas, have all game objects update and redraw, then set up the next draw.'''

    canvas.delete(Tkinter.ALL)

    global game_objects
    for game_object in game_objects:
        game_object.update()
        game_object.draw(canvas)

    delay = 33 # milliseconds, so about 30 frames per second
    canvas.after(delay, draw, canvas) # call this draw function with the canvas argument again after the delay

# this is a standard Python thing: definitions go above, and any code that will actually
# run should go into the __main__ section. This way, if someone imports the file because
# they want to use the functions or classes you've defined, it won't start running your game
# automatically
if __name__ == '__main__':



    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=400, height=400)
    canvas.pack()

    # if the user presses a key or the mouse, call our handlers
    root.bind('<Key-r>', reset)
    root.bind('<Key-space>', addShape)
    root.bind('<Key-space>', addShape)
    root.bind('<Key-c>', addSpecialSquare)
 

    # start the draw loop
    draw(canvas)

    root.mainloop() # keep the window open
