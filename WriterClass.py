import datetime

class writer:
    PROYECTNUM = int(2000)
    day = datetime.date.today().strftime("%j")
    week = datetime.date.today().strftime("%W")



    #Inititating the instances variables
    def __init__(self, file= "NewProject", title=""):
        self._fileName = file
        self._title = title
        self._num = writer.PROYECTNUM  + 1

    def setFile( self, newFileName):
        self._fileName = newFileName

    def setTitle ( self, newTitle):
        self._title = newTitle
        #Mutators

    def getFile (self):
        return self._fileName

    def getTitle (self):
        return self._title
    def getNum(self):
        return self._num


class DailyEntry(writer):

    def __init__ (self, file= "NewProject", title=""):
        super().__init__(file, title)
        self._date =  datetime.date.today()

class Compiler(writer):
    def __init__ (self, file= "NewProject", title="", num= "1"):
        super().__init__(file, title)
        self._count = int(num)

    def addUp (self):
        self._count += 1
    def getCount (self):
        return self._count
