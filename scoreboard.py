from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self): 
        super().__init__()
        self.score=0 
        self.penup()
        self.hideturtle() 
        self.updatescore()
    
    def updatescore(self): 
        self.clear()
        self.goto(-250,250) 
        self.write(f"Level: {self.score}", align="left", font=FONT) 
    
    def increase(self):
        self.score=self.score+1 
        self.updatescore()
    
    def gameover(self): 
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
    
    