def loadTable(db, keys, headers, values):

    mydb = db
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS new_schema.AllComputers;")
    mycursor.execute("CREATE TABLE new_schema.AllComputers (" + headers + ");")
    sql = "INSERT INTO new_schema.AllComputers (" + keys + ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = values
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")