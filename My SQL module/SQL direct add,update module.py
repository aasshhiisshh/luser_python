import MySQLdb

db=MySQLdb.connect("localhost","root","tiger","student")
cursor=db.cursor()

class student:
    def __init__(self):
        pass
        
    def insert(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        cursor.execute("""insert into info values (%s,%s,%s)""",(self.fname,self,lname,self.age))
        db.commit()
        db.close()
        
    def select(self):
        count=0
        cursor.execute("select * from info;")
        for row in cursor:
            print row
            count=count+1
        #print count
        db.close()
       
    def update(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        cursor.execute("""update info set name=%s where id=%s""",(self.fname,self.lname))
        db.commit()
        db.close()    

if __name__ == "__main__":
    print "pakku"

s = student # always assign object to class name.
#s.insert("as","pa","123")
