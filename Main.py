import time
import threading


import Acctions

acctionsList = []
acctionMouse = Acctions.MouseClick()

timePrint = False


class MainClass:
    def __init__(self) -> None:
        #thread 1
        self.runThread = threading.Thread(target=self.run)
        self.runThread.start()

        #thread 0
        self.printThread = threading.Thread(target=self.timePrint)
        self.printThread.start()



    def run(self): #run code here
        global timePrint
        while True:            
            if acctionMouse.mouse_is_clicked('left'):
                timePrint = True



    def timePrint(self): #use to print
        global timePrint
        while True:
            if timePrint == True:
                timePrint = False
                print('pro_time')
            time.sleep(1)


AutoFlowControl = MainClass()