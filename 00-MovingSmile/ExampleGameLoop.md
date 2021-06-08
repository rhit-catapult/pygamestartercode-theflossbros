---
layout: page
---


<!-- vim-markdown-toc GFM -->

* [Introduction: ExampleGameLoop](#introduction-examplegameloop)
  * [Setup](#setup)
* [Step 0: The prelude](#step-0-the-prelude)
* [Step 1: The initialization phase](#step-1-the-initialization-phase)
* [Step 2: The game loop](#step-2-the-game-loop)

<!-- vim-markdown-toc -->

# Introduction: ExampleGameLoop

In this small exercise, we will write our first python program that displays an
empty screen with a title. We will see how to tell pygame the size of our
screen, and then check how pygame captures every event on the screen.

## Setup

In pycharm, open up the file `ExampleGameLoop.py` in your repository, it is
under the `00-MovingSmile` directory.


# Step 0: The prelude

Our example code starts with the following two lines:
```python
import pygame
import sys
```
This of these two lines as being the tools needed for our recipe.  When we bake
a cake, we first need to make sure that we have the right set of tools (e.g., a
stand mixer, a spatula, etc.). In our case, we need two tools (or modules, or
libraries), the first being `pygame` while the second is `sys`.

`pygame` is a box that contains numerous tools that the instructions in our
recipe are going to require. We will spend most of our time dealing with the
content of `pygame` to make games and capture events. 

`sys` on the other hand is another tool box that allows python to communicate
with the part of your computer that actually runs python, i.e., the operating
system.

# Step 1: The initialization phase

Next, we will need to initialize our python environment to use pygame and set a
few configuration options, which is why we need the following lines of code
```python
pygame.init()
pygame.display.set_caption("Hello World")
```

The first line, `pygame.init()`, sets up pygame for us to use. Alternatively,
you can think of this as turning on your game console before you start any game.

The second line, `pygame.display.set_caption("Hello World")`, accesses the
`display` tool in the pygame toolbox, and asks it to set the caption of our game
to be `Hello World`. Note that the phrase `Hello World` is placed between
quotes, why is that? It is because `Hello World` is actually a __string__, i.e.,
a non code piece of text. Generally, any set of characters surrounded with
quotes (single or double) form a string.

Then, we create our universe, the game screen! To do that, we use the following
line of code
```python
screen = pygame.display.set_mode((640, 480))
```
What does this do? I am glad you asked. It first accesses the `display` tool
from the pygame toolbox and asks to create a screen for us with height 640
pixels and width 480 pixels. What are pixels you may ask? You can think about
them as the smallest unit of measurement on a computer screen. 

But wait, what's with all those parentheses? There are two things that we should
be aware of:
1. First, `set_mode` is a __function__ that we are __calling__, thus we refer to
   this statement as a _function call_. Everytime we call a function, we must
   open and close a pair of parentheses. 
2. Okay, but what about the second pair? The second pair of parentheses actually
   creates a tuple off of the numbers 640 and 480. In other words, the numbers
   640 (for the height) and 480 (for the width) are grouped together in a single
   tuple and then used as input to the function `set_mode`. 
   
Question: How many arguments (inputs) are we providing to the function
`set_mode` when we called it from our code?

# Step 2: The game loop
