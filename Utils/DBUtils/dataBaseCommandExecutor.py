#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

import mysql.connector as mysqlConnector
from Resources.DataBaseProperties import HOST_NAME, DB_NAME, DB_USER_NAME, PORT_NAME, DB_PASSWORD
from Resources.DataBaseProperties import SQL_FILE_PREFIX
from Utils.OSUtils.OSOperations import getOSPath
from Resources.VariableConstants import BASE_DIR


# RETURN ERROR DETAILS STRING FOR LOGGING
def getErrorDetails(errorObject):
    return "{} \n {} \n {} \n {}".format(
        "Exception Occurred while Operating on Database: {}".format(errorObject),
        "Error Code: {}".format(errorObject.errno),
        "SQL_STATE: {}".format(errorObject.sqlstate),
        "Error Message: {}".format(errorObject.msg)
    )


# EXECUTE INSERT COMMAND
def executeInsertCommand(command):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    try:
        # Execute Command
        mySQLCursor.execute(command)

        # Insert into DB
        sqlConnector.commit()

        # # Fetch from Table and return one Row
        # returnOneRow = mySQLCursor.fetchone()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()


# EXECUTE GET COMMAND
def executeGetCommand(command):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    try:
        # Execute Command
        mySQLCursor.execute(command)

        # Fetch from Table and return one Row
        returnOneRow = mySQLCursor.fetchall()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()

    # Return one Row
    return returnOneRow


# EXECUTE TABLE CREATION
def executeSQLFile(SQLFilePath):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    # READ SQL FILE AND EXECUTE IT
    try:
        with open(SQLFilePath, 'r') as fileObject:
            sqlScript = fileObject.read()
            for sqlStatements in sqlScript.split(";\n"):
                if sqlStatements == "":
                    continue
                else:
                    mySQLCursor = sqlConnector.cursor()
                    mySQLCursor.execute(sqlStatements)
                    sqlConnector.commit()
                    mySQLCursor.close()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    sqlConnector.close()


# EXECUTE TABLE CREATION
def createDBBootUp(fileNameList):
    for fileName in fileNameList:
        FullFilePath = BASE_DIR + SQL_FILE_PREFIX + fileName
        FullFilePath = getOSPath(FullFilePath)
        print("Executing File: {}".format(FullFilePath))
        executeSQLFile(FullFilePath)

