import sqlite3
from django.db import connection
#cursor = connection.cursor()

conexion=sqlite3.connect("db")
cursor = conexion.cursor()  
res = cursor.execute( 'SELECT * FROM sqlite_master WHERE type = "table" ')
                
res.fetchone()
print("ok")                    
