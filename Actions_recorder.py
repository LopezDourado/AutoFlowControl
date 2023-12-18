class Record:
    def __init__(self,record = []) -> None:
        self.record = record

    def startRecord(self):
        pass

    def removeRecord(self,remove):
        index = self.record.index(remove)
        del self.record[index]


    def updateRecord(self):
        pass

    def addRecord(self,add):
        self.record.append(add)




    def printStatus(self):
        #mouse moving
        #mouse click
        #mouse is clicking
        #mouse release click

        #mouse scroll
        
        #keyboard pressed
        #keyboard pressing
        #keyboard release key

        #time wait
        pass