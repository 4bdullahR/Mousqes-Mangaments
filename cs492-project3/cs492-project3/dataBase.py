import sqlite3

class dataBase:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cur = self.conn.cursor()
        self.cur.execute(" CREATE TABLE IF NOT EXISTS mosque (id INT PRIMARY KEY, name varchar(255) UNIQUE,\
        type varchar(255), address varchar(255), coordinates varchar(255), imamName varchar(255));")
    
    def __del__(self):
        self.conn.close()

    def displayAll(self): 
        self.cur.execute("SELECT * FROM mosque")
        data = self.cur.fetchall()
        return data

    def searchName(self,NAME): 
        self.cur.execute(f"SELECT * FROM mosque where name = '{NAME}'")
        data = self.cur.fetchall()
        if len(data) == 0:
            return 0
        else: 
            return data

    def insertData(self,ID,NAME,TYPE,ADDRESS,COORDINATES,IMAM_NAME): # except sqlite3.IntegrityError:
        self.cur.execute(f"INSERT INTO mosque (id,name,type,address,coordinates,imamName) VALUES ({ID},\
        '{NAME}','{TYPE}','{ADDRESS}','{COORDINATES}','{IMAM_NAME}')")
        self.conn.commit()

    def updateEntry(self,NAME, newImamName): 
        self.cur.execute(f"UPDATE mosque SET imamName = '{newImamName}' where name = '{NAME}' ")
        self.conn.commit()

    def delEntry(self,ID): 
        self.cur.execute(f"SELECT id FROM mosque WHERE id = {ID}")
        data = self.cur.fetchall()
        if len(data) == 0:
            return 0
        self.cur.execute(f"DELETE FROM mosque WHERE id = {ID}")
        self.conn.commit()
    #def excuteSQL(self,s): #for advanced op #for 
    #    self.cur.execute(s)
    #    self.conn.commit()