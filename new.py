def left(self):
    pos = [self.pos[0]-1, self.pos[1]]
    if not self.cancas.hitsWall(pos):
        self.draw(pos)

def drawSquare(self, size):
    i = 0
    while i < size:
        self.right()
        i += 1
    i = 0
    while i < size:
        self.down()
        i += 1
    i = 0
    while i < size:
        self.left()
        i += 1
    i = 0
    while i < size:
        self.up()
        i += 1



def draw(self, pos):
    self.canvas.setPos(self.pos, self.trail)
    self.pos = pos
    self.canvas.setPos(self.pos, colored(self.mark, 'red'))
    self.canvas.print()
    time.sleep(self.framerate)        
        
canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

scribe.drawSquare(20)
