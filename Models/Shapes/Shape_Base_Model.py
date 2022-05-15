


class ShapeBase:
    def __init__(self,size,color:tuple,location:tuple) -> None:
        self.__BaseSetup(size,color,location)
    def __BaseSetup(self,size,color:tuple,location:tuple):
        self.Size = size
        self.Color = color
        self.Location = location
        self.Visible = True
    def ToggleVisibility(self):
        self.Visible = not self.Visible
    def MoveTo(self, x_loc,y_loc):
        self.Location = (x_loc,y_loc)

    def Move_Y(self,change):
        self.MoveTo(self.Location[0],self.Location[1] + change)
    def Move_X(self,change):
        self.MoveTo(self.Location[0] + change,self.Location[1])
    def ChangeSize(self, change):
        self.Size = self.Size + change
        if self.Size < 0 :
            self.Size = 0
    def SetSize(self, size):
        self.Size = size
        if self.Size < 0:
            self.Size = 0
