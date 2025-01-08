from pynput.mouse import Controller, Button

mouse = Controller()

mouse.position = (970, 500)

for n in range(2000):
    mouse.press(Button.left)
    mouse.release(Button.left)
