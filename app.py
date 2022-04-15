from tkinter import *
import random
import time
import tkinter.messagebox as mb

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 150
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = random.choice(["#DC143C","#FFFFFF", "#000000"])
BACKGROUND_COLOR = "#008000"
FOODS = ["#FF0000", "#02fa44", "#faf202", "#faf202", "#FB3636", "#F0F961","#D2EC00", "#7AC313", "#FFFFC2"]

class Snake:
    def __init__(self) -> None:
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self) -> None:
        x = random.randint(0, int((GAME_WIDTH/SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT/SPACE_SIZE) - 1))* SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=random.choice(FOODS), tag="food")

def next_turn(snake: Snake, food: Food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y-= SPACE_SIZE
    elif direction == "down":
        y+=SPACE_SIZE
    elif direction == "left":
        x-=SPACE_SIZE
    elif direction == "right":
        x+=SPACE_SIZE
    
    snake.coordinates.insert(0, (x,y))


    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1
        label.config(text=f"Score: {score}")

        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction 

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake: Snake):
    x,y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text="Game Over", font=("Consolas", 70), fill="red")


window = Tk()
window.title("Snake game Tkinter | www.AZIZBEKDEV.com")
window.resizable(False, False)
window.attributes('-topmost',True)


score = 0
direction = 'down'


label = Label(window, text=f"Score: {score}", font=('Consolas', 30))
label.pack()

canvas = Canvas(window, background=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))


def start():
    canvas.delete(ALL)
    snake = Snake()
    food = Food()

    next_turn(snake, food)

start()

window.mainloop()