import mouse
import keyboard
import pyautogui

class MouseClick:
    def __init__(self,mouseX =None ,mouseY = None):
        self.mouseX = mouseX
        self.mouseY = mouseY

    def get_mouse_position(self):
        mouse_pos = pyautogui.position()
        return mouse_pos
    
    def mouse_is_clicked(self,buttonMouse):
        return mouse.is_pressed(button=buttonMouse)
    
    def apply(self):
        pyautogui.leftClick(x=self.mouseX,y=self.mouseY)




class keyboardPress:#in progress
    def __init__(self,key):
        self.key = key

    def apply(self):
        pyautogui.press()