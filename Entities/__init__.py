# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String, TIMESTAMP, Boolean, create_engine, \
    inspect
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Resources.DataBaseProperties import DB_TYPE, DB_DRIVER, DB_USER_NAME, DB_PASSWORD, HOST_NAME, PORT_NAME, DB_NAME, \
    DEV_DB_TYPE
from Resources.Constants import ENVIRONMENT
from Utils.OSUtils.OSOperations import getBaseDir


Base = declarative_base()
metadata = Base.metadata

BASE_URL = getBaseDir()
if ENVIRONMENT == "PROD":
    DB_INIT_STRING = f"{DB_TYPE}+{DB_DRIVER}://{DB_USER_NAME}:{DB_PASSWORD}@{HOST_NAME}:{PORT_NAME}/{DB_NAME}"
else:
    print(BASE_URL)
    DB_INIT_STRING = f"{DEV_DB_TYPE}:///{BASE_URL}\\{DB_NAME}.db"

engine = create_engine(DB_INIT_STRING, echo=True)

def getSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
