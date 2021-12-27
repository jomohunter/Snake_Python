import curses
from random import randint

from tes import WINDOW_HEIGHT, WINDOW_WIDTH 

# window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(True)
# character snake and food

snake = [(4,10),(4,9),(4,8)]  # y then x  dunno why
food = (10,20)
#game
score = 0
win.addch(food[0], food[1], '.')

Esc = 27
key = curses.KEY_RIGHT

while key != Esc:
    win.addstr(0, 2, 'Score' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) //10 %120 )
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key
    if key not in [curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, Esc]:
        key = prev_key
    

    # Calculate next cords
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1
    snake.insert(0, (y, x))

    #border hit 
    if y == 0 : break
    if y == WINDOW_HEIGHT-1 : break
    if x == 0 : break
    if x == WINDOW_WIDTH-1 : break
    #snake ate himself
    if snake[0] == snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,WINDOW_HEIGHT-2), randint(1,WINDOW_WIDTH -2))
            if food in snake:
                food == ()
        win.addch(food[0], food[1], '.')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')
    
    

curses.endwin
print(f"Game Over \n your final score = {score}")

