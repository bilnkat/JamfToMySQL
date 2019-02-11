import mysql.connector

def dbConnect(hst, db, usr, pw):
    mydb = mysql.connector.connect(
            user=usr,
            password=pw,
            host=hst,
            database=db,
            auth_plugin='mysql_native_password'
        )

    return mydb