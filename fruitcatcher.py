import tkinter as tk
import random
from PIL import Image, ImageTk

# Initialize the main window
window = tk.Tk()
window.title("Fruit Catcher")
window.resizable(False, False)  # Disable window resizing

# Create a canvas for drawing
canvas = tk.Canvas(window, width=400, height=400, bg='lightpink')
canvas.pack()

# Define game variables
fruit_size = 50
fruit_speed = 8
basket_speed = 40
basket_width = 80
basket_height = 20
score = 0
game_over = False
lives_left = 3

# Load and resize the fruit image
fruit_image = Image.open("strawberry.png")
fruit_image = fruit_image.resize((fruit_size, fruit_size), Image.LANCZOS)
fruit_photo = ImageTk.PhotoImage(fruit_image)

# Load and resize the basket image
basket_image = Image.open("basket.png")
basket_image = basket_image.resize((basket_width, basket_height), Image.LANCZOS)
basket_image = ImageTk.PhotoImage(basket_image)

# Create the basket image on the canvas
basket = canvas.create_image(110, 380, anchor='nw', image=basket_image)

# Create labels for lives and score
lives_label = tk.Label(window, text=f"Lives: {lives_left}", bg='pink', font=('Helvetica', 12))
lives_label.pack()

score_label = tk.Label(window, text=f"Score: {score}", bg='pink', font=('Helvetica', 12))
score_label.pack()

# Function to create a new fruit
def create_fruit():
    if not game_over:
        x = random.randint(0, 400 - fruit_size)  # Random x position
        y = 0  # Start at the top
        fruit = canvas.create_image(x, y, anchor='nw', image=fruit_photo)
        return fruit

# Function to move fruits
def move_fruit():
    global score, lives_left, game_over

    if game_over:
        return

    fruits_to_remove = []

    for fruit in list(fruits):
        canvas.move(fruit, 0, fruit_speed)  # Move fruit down
        pos = canvas.coords(fruit)
        basket_pos = canvas.coords(basket)

        # Check if the fruit is caught by the basket
        if (basket_pos and pos[1] + fruit_size >= basket_pos[1] and
            pos[0] + fruit_size >= basket_pos[0] and
            pos[0] <= basket_pos[0] + basket_width):
            fruits_to_remove.append(fruit)
            score += 1
            score_label.config(text=f"Score: {score}")

        # Check if the fruit hits the bottom
        elif pos[1] >= 400 - fruit_size:
            fruits_to_remove.append(fruit)
            lives_left -= 1
            lives_label.config(text=f"Lives: {lives_left}")
            if lives_left == 0:
                game_over = True
                canvas.create_text(200, 200, text="Game Over", font=('Helvetica', 24), fill='red')

    # Remove caught or missed fruits from the canvas and list
    for fruit in fruits_to_remove:
        canvas.delete(fruit)
        fruits.remove(fruit)

    if not game_over:
        window.after(100, move_fruit)  # Repeat the function after 100ms

# Function to move the basket left
def move_left(event):
    if not game_over:
        canvas.move(basket, -basket_speed, 0)

# Function to move the basket right
def move_right(event):
    if not game_over:
        canvas.move(basket, basket_speed, 0)

# Bind the left and right arrow keys to move the basket
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)

# List to store fruits
fruits = []

# Function to create new fruits at intervals
def create_new_fruit():
    fruits.append(create_fruit())
    window.after(2000, create_new_fruit)  # Repeat the function after 2000ms

# Start the game by creating the first fruit and starting the fruit movement
create_new_fruit()
move_fruit()

# Run the Tkinter event loop
window.mainloop()