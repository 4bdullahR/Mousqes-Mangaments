class Mosque(object):
    def __init__(self, id, name, type, address, coordinates, imamName):
        self.id = id
        self.name = name
        self.type = type
        self.address = address
        self.coordinates = coordinates
        self.imamName = imamName

    def __del__(self):
      print (f"Object id:{self.getID()} {id(self)} was destroyed");

    def getAll(self):
        info = f"ID: {self.getID()} \nName: {self.getName()} \nType: {self.getType()} \nAddress: {self.getAddress()} \nCoordinates: {self.getCoordinates()}"
        return info

    def setID(self,id):
        self.id = id
    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setType(self,type):
        self.type = type
    def getType(self):
        return self.type

    def setAddress(self,address):
        self.address = address
    def getAddress(self):
        return self.address

    def setCoordinates(self,coordinates):
        self.coordinates = coordinates
    def getCoordinates(self):
        return self.coordinates

    def imamName(self,imamName):
        self.imamName = imamName
    def getImamName(self):
        return self.imamName