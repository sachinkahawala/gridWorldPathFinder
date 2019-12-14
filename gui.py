from tkinter import *
from main import *
class Cell():
    BlOCKED_COLOR_BG = "green"
    TARGET_COLOR_BG = "blue"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size,colour):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= colour
        self.xmin = self.abs * self.size
        self.xmax = self.xmin + self.size
        self.ymin = self.ord * self.size
        self.ymax = self.ymin + self.size
        self.a,self.b=(self.xmin+self.xmax)/2,(self.ymin+self.ymax)/2
    def _switch(self,t):
        """ Switch if the cell is filled or not. """
        self.fill= t

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        if self.master != None :

            if self.fill==0:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER
            if self.fill==1:
                fill = Cell.BlOCKED_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER
            if self.fill==2:
                fill = Cell.TARGET_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER


            self.master.create_rectangle(self.xmin, self.ymin, self.xmax, self.ymax, fill = fill, outline = outline)

    def drawArrow(self,type):
        if type==0:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
        if type==1:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
        if type==2:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
        if type==3:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
        if type==4:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
        if type==5:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
        if type==6:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
        if type==7:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
        if type==8:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
        if type==9:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
        if type==10:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
        if type==11:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
        if type==12:
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
        if type==13:
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
        if type==14:
            #top arrow
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= FIRST)
            #bottom arrow
            self.master.create_line(self.a, self.ymin, self.a, self.ymax, arrow= LAST)
            #left arrow
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= FIRST)
            #right arrow
            self.master.create_line(self.xmin, self.b, self.xmax, self.b, arrow= LAST)
class CellGrid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber + 200, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize,0))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.blocked = []
        self.targets = []
        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        #self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()



    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch(para)
        cell.draw()
        if para==1:
            self.blocked.append(cell)
        if para==2:
            self.targets.append(cell)


    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.blocked or cell not in self.targets:
            cell._switch(para)
            cell.draw()
            if para==1:
                self.blocked.append(cell)
            if para==2:
                self.targets.append(cell)
def generateobs():


    global para,obs

    obs=set([( i.ord,i.abs) for i in grid.blocked ])
    para=2
    #print(obs)
def calculateType(pi,i,j):
    gI=(np.argwhere(pi[i,j] ==np.amax(pi[i,j]))).tolist()
    #print(gI,"sdad")
    if len(gI)==1:
        return gI[0][0]
    elif len(gI)==2:

        P=set([i[0] for i in gI])
        if P==set([0,1]):
            return 4
        if P==set([1,2]):
            return 5
        if P==set([2,3]):
            return 6
        if P==set([0,3]):
            return 7
        if P==set([0,2]):
            return 8
        if P==set([1,3]):
            return 9

    elif len(gI)==3:
        P=set([i[0] for i in gI])
        if P==set([0,1,2]):
            return 10
        if P==set([1,2,3]):
            return 11
        if P==set([0,2,3]):
            return 12
        if P==set([0,1,3]):
            return 13

    else:
        return 14

def generatetargets():

    targets=set([( i.ord,i.abs) for i in grid.targets ])

    pi=np.full((x,y,4),0.25)
    reward=np.full((x,y),-1)
    for t in obs:reward[t]=-1000
    values = np.zeros((x,y))
    theta=0.001
    gamma=1
    e=env(x,y)
    V, pi=policy_iteration(e,values,pi, gamma, theta,reward,targets)
    for i,j in e.S:
        if (i,j) not in targets and (i,j) not in obs:

            grid.grid[i][j].drawArrow(calculateType(pi,i,j))


def initialize():
    app = Tk()
    global grid,para
    para=1
    grid = CellGrid(app, x, y, 60)

    label = Label(grid, text= '1 . Mark the obstacles ' ,font=('helvetica', 10))
    grid.create_window(y*60/2, x*60+20, window=label)

    button2 = Button(grid,text='Obstacles marked', command=generateobs, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    grid.create_window(y*60/2, x*60+50, window=button2)

    label1 = Label(grid, text= '2 . Mark the targets ' ,font=('helvetica', 10))
    grid.create_window(y*60/2, x*60+80, window=label1)

    button3 = Button(grid,text='Targets marked', command=None, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    grid.create_window(y*60/2, x*60+110, window=button3)

    button4 = Button(grid,text='Calculate optimal path', command=generatetargets, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    grid.create_window(y*60/2, x*60+140, window=button4)

    grid.pack()
    app.mainloop()

def getSquareRoot ():
    global x,y
    x = int(entry1.get())
    y = int(entry2.get())
    initialize()


root= Tk()
canvas1 = Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
label2 = Label(root, text='Enter height:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)
entry1 = Entry (root)
canvas1.create_window(200, 75, window=entry1)
label3 = Label(root, text='Enter width:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label3)
entry2 = Entry (root)
canvas1.create_window(200, 125, window=entry2)
button1 = Button(text='Build grid', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()
