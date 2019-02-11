from getJamfJSON import getJSON as getJ
from dbConnector import dbConnect as dbCon
import parseJSON as pJ
from tableLoader import loadTable as loadT
import envVar as e

jamfUrl = e.jamf_url
jamfHeaders = {'Accept': 'application/json;charset=UTF-8'}
jamfUsername = e.jamf_user
jamfPassword = e.jamf_pass

dbHost = e.db_host
dbDatabase = e.db_database
dbUser = e.db_user
dbPassword = e.db_pass


def main():

    r = getJ(jamfUrl, jamfHeaders, jamfUsername, jamfPassword)
    key = pJ.getKeys(r)
    val = pJ.getVals(r)
    headers = pJ.getHeaders(r)
    db = dbCon(dbHost, dbDatabase, dbUser, dbPassword)

    loadT(db, key, headers, val)


if __name__ == '__main__':
    main()