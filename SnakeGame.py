from tkinter import *
import random

SIZE = 20
WIDTH, HEIGHT = 400, 400
SPEED = 100

class SnakeGame:
    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.new_food()
        root.bind("<Key>", self.change_direction)
        self.update()

    def new_food(self):
        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)
        return (x, y)

    def change_direction(self, event):
        dirs = {"Up","Down","Left","Right"}
        if event.keysym in dirs:
            # avoid 180° turns
            if (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

    def update(self):
        x, y = self.snake[0]
        if self.direction == "Up":    y -= SIZE
        if self.direction == "Down":  y += SIZE
        if self.direction == "Left":  x -= SIZE
        if self.direction == "Right": x += SIZE
        new_head = (x, y)

        # collision
        if (x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT or new_head in self.snake):
            self.canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="red", font=20)
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.new_food()
        else:
            self.snake.pop()

        self.draw()
        self.canvas.after(SPEED, self.update)

    def draw(self):
        self.canvas.delete("all")
        # snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill="lime")
        # food
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+SIZE, fy+SIZE, fill="yellow")

root = Tk()
game = SnakeGame(root)
root.mainloop()