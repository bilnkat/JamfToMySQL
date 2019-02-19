def loadTable(db, keys, headers, values):

    mydb = db
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS jamf_database.AllComputers;")
    mycursor.execute("CREATE TABLE jamf_database.AllComputers (" + headers + ");")
    sql = "INSERT INTO jamf_database.AllComputers (" + keys + ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = values
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")