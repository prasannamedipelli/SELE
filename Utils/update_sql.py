import mysql.connector
conn = None
try:
  conn = mysql.connector.connect(
      host = "localhost",  #loop back ip
      user = "root",
      password ="root",
      database ="saucedemodb"
  )
  cursor = conn.cursor()
  cursor.execute("UPDATE employee set salary =%s where id=%s",(90000,2))
  conn.commit()
  print("updated record successully")
  
except:
    print("database error")
finally: 
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed")

#curser

#execute query

#close connection