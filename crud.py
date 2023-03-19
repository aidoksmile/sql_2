import mysql.connector
 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database = "less1"
)
 
mycursor=db.cursor()

try:  
   mycursor.execute("select * from student")  
   result=mycursor.fetchall()   
   for i in result:    
      print(i)  
except:   
   print('Error:Unable to fetch data.')  

db.close()