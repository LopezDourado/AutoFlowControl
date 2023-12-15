import time

import Acctions

acctionsList = []
acctionMouse = Acctions.MouseClick()

class MainClass:
    def __init__(self) -> None:
        pass

    def run(self):
        while True:
            if acctionMouse.mouse_is_clicked('left'):
                print('teste')

            pass

    def timePrint(self):
        pass


AutoFlowControl = MainClass()
AutoFlowControl.run()