# Dobre-praktyki-tworzenia-oprogramowania

# Fruit Catcher Game

A simple and fun fruit-catching game using Python and Tkinter.

## Description

In this game, you control a basket to catch falling fruits. The objective is to catch as many fruits as possible without letting them fall off the screen. You have three lives, and the game ends when you run out of lives.

## Features

- **Basket Movement:** The basket can move left and right to catch the falling fruits.
- **Fruit Falling:** Fruits fall from the top of the screen, and the player must catch them.
- **Score Tracking:** The player's score is displayed on the screen, increasing with each fruit caught.
- **Lives Tracking:** The player has three lives, and the game ends when all lives are lost.
- **Game Over:** A game over message is displayed when the player runs out of lives.

## Getting Started

### Prerequisites

- Python 3.x
- Pillow library

### Installation

1. Clone the repository:

```
    git clone https://github.com/karlosia/Dobre-praktyki-tworzenia-oprogramowania
    cd Fruit_Catcher_Game
```

2. Install the Pillow library:
```
    pip install Pillow
```    

### Running the Game

Run the game script:

python main.py


# Game Controls
Left Arrow Key: Move the basket to the left.

Right Arrow Key: Move the basket to the right.

# Code Overview

The game consists of several main components:

# Main Window Setup
The main window is set up using Tkinter, with a canvas for drawing the game elements.
```
window = tk.Tk()
window.title("Fruit Catcher")
window.resizable(False, False)
canvas = tk.Canvas(window, width=400, height=400, bg='lightpink')
canvas.pack()
```
# Game Variables
Several variables are defined for the game, including fruit size, speeds, basket dimensions, score, and lives.
```
fruit_size = 50
fruit_speed = 8
basket_speed = 40
basket_width = 80
basket_height = 20
score = 0
game_over = False
lives_left = 3
```
# Images and Labels
The fruit and basket images are loaded and resized. Labels for lives and score are created.
```
fruit_image = Image.open("strawberry.png")
fruit_image = fruit_image.resize((fruit_size, fruit_size), Image.LANCZOS)
fruit_photo = ImageTk.PhotoImage(fruit_image)

basket_image = Image.open("basket.png")
basket_image = basket_image.resize((basket_width, basket_height), Image.LANCZOS)
basket_image = ImageTk.PhotoImage(basket_image)

lives_label = tk.Label(window, text=f"Lives: {lives_left}", bg='pink', font=('Helvetica', 12))
lives_label.pack()
score_label = tk.Label(window, text=f"Score: {score}", bg='pink', font=('Helvetica', 12))
score_label.pack()
```
# Game Functions
Several functions are defined to manage the game logic, including creating and moving fruits, handling basket movement, and checking for collisions.
```
create_fruit: Creates a new fruit at a random x position at the top of the screen.
move_fruit: Moves the fruits down the screen and checks for collisions with the basket or bottom of the screen.
move_left and move_right: Handle basket movement.
```
# Event Binding and Game Loop
The arrow keys are bound to the basket movement functions, and the game loop is started.
```
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)

create_new_fruit()
move_fruit()

window.mainloop()
```
# Credits
Graphics: Fruit and basket images are custom made
Sound Effects: No sound effects are used in this version of the game.
Fonts: The game uses the default Tkinter font.



