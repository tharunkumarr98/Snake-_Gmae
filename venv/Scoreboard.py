from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as H:
            self.highscore = int(H.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def increase_score(self):
        self.score +=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} HighScore: {self.highscore}", False, align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            
            with open("data.txt", mode="w") as H:
                H.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    # def game_is_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))