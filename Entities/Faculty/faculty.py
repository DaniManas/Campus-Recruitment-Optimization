#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------
from Entities import *


class Faculty(Base):
    __tablename__ = 'faculty'

    facultyId = Column(Integer, primary_key=True, unique=True)
    facultyRegId = Column(String(10))
    facultyFirstName = Column(String(100))
    facultyLastName = Column(String(100))
    facultyEmail = Column(VARCHAR(320), nullable=False, unique=True)
    facultyMobileNumber = Column(String(100), nullable=False, unique=True)
    facultyCollegeId = Column(ForeignKey('college.collegeId', ondelete='SET NULL'), index=True)
    facultyDepartmentId = Column(ForeignKey('collegedepartments.collegeDepartmentsId', ondelete='SET NULL'), index=True)
    facultyRoleId = Column(ForeignKey('roles.RoleId', ondelete='SET NULL'), index=True)
    facultyisEmailVerified = Column(Boolean)
    facultyisMobileNumberVerified = Column(Boolean)
    username = Column(String(50))
    password = Column(String(300))
    lastLoggedInTimeStamp = Column(TIMESTAMP)
    lastLoggedOutTimeStamp = Column(TIMESTAMP)
    lastModifiedPassword = Column(TIMESTAMP)
    entityIdentifier = Column(String(1))

    college = relationship('College')
    collegedepartment = relationship('Collegedepartment')
    role = relationship('Role')

    def __init__(self,
                 facultyRegId=1,
                 facultyFirstName="DefaultFacultyName",
                 facultyLastName="DefaultFacultyName",
                 facultyEmail="DefaultEmail@xyz.com",
                 facultyMobileNumber="1234567890",
                 facultyCollegeId=1,
                 facultyDepartmentId=1,
                 facultyRoleId=1,
                 facultyisEmailVerified=False,
                 facultyisMobileNumberVerified=False,
                 username="DefaultUsername",
                 password="DefaultPass",
                 lastLoggedInTimeStamp=None,
                 lastLoggedOutTimeStamp=None,
                 lastModifiedPassword=None,
                 entityIdentifier="T"):
        self.__facultyRegId = facultyRegId

        self.__facultyFirstName = facultyFirstName
        self.__facultyLastName = facultyLastName
        self.__facultyEmail = facultyEmail
        self.__facultyMobileNumber = facultyMobileNumber
        self.__facultyCollegeId = facultyCollegeId
        self.__facultyDepartmentId = facultyDepartmentId
        self.__facultyRoleId = facultyRoleId
        self.__facultyisEmailVerified = facultyisEmailVerified
        self.__facultyisMobileNumberVerified = facultyisMobileNumberVerified
        self.__username = username
        self.__password = password
        self.__lastLoggedInTimeStamp = lastLoggedInTimeStamp
        self.__lastLoggedOutTimeStamp = lastLoggedOutTimeStamp
        self.__lastModifiedPassword = lastModifiedPassword
        self.__entityIdentifier = entityIdentifier


def __repr__(self):
    reprString = """
        Faculty Object:
        Faculty Name: {} {}
        Faculty Registration Id: {}
        """.format(self.facultyFirstName, self.facultyLastName, self.facultyRegId)
    return reprString

# ============================================
# =========== GETTERS AND SETTERS ============
# ============================================

# PROPERTY --> facultyRegId
# @property
# def facultyRegId(self):
#     return self.__facultyRegId
#
# @facultyRegId.setter
# def facultyRegId(self, facultyRegId):
#     self.__facultyRegId = facultyRegId
#
# @facultyRegId.deleter
# def facultyRegId(self):
#     del self.__facultyRegId
#
#
# # PROPERTY --> facultyFirstName
# @property
# def facultyFirstName(self):
#     return self.__facultyFirstName
#
# @facultyFirstName.setter
# def facultyFirstName(self, facultyFirstName):
#     self.__facultyFirstName = facultyFirstName
#
# @facultyFirstName.deleter
# def facultyFirstName(self):
#     del self.__facultyFirstName
#
# # PROPERTY --> facultyLastName
# @property
# def facultyLastName(self):
#     return self.__facultyLastName
#
# @facultyLastName.setter
# def facultyLastName(self, facultyLastName):
#     self.__facultyLastName = facultyLastName
#
# @facultyLastName.deleter
# def facultyLastName(self):
#     del self.__facultyLastName
#
# # PROPERTY --> facultyEmail
# @property
# def facultyEmail(self):
#     return self.__facultyEmail
#
# @facultyEmail.setter
# def facultyEmail(self, facultyEmail):
#     self.__facultyEmail = facultyEmail
#
# @facultyEmail.deleter
# def facultyEmail(self):
#     del self.__facultyEmail
#
# # PROPERTY --> facultyMobileNumber
# @property
# def facultyMobileNumber(self):
#     return self.__facultyMobileNumber
#
# @facultyMobileNumber.setter
# def facultyMobileNumber(self, facultyMobileNumber):
#     self.__facultyMobileNumber = facultyMobileNumber
#
# @facultyMobileNumber.deleter
# def facultyMobileNumber(self):
#     del self.__facultyMobileNumber
#
# # PROPERTY --> facultyCollegeId
# @property
# def facultyCollegeId(self):
#     return self.__facultyCollegeId
#
# @facultyCollegeId.setter
# def facultyCollegeId(self, facultyCollegeId):
#     self.__facultyCollegeId = facultyCollegeId
#
# @facultyCollegeId.deleter
# def facultyCollegeId(self):
#     del self.__facultyCollegeId
#
# # PROPERTY --> facultyDepartmentId
# @property
# def facultyDepartmentId(self):
#     return self.__facultyDepartmentId
#
# @facultyDepartmentId.setter
# def facultyDepartmentId(self, facultyDepartmentId):
#     self.__facultyDepartmentId = facultyDepartmentId
#
# @facultyDepartmentId.deleter
# def facultyDepartmentId(self):
#     del self.__facultyDepartmentId
#
# # PROPERTY --> facultyRoleId
# @property
# def facultyRoleId(self):
#     return self.__facultyRoleId
#
# @facultyRoleId.setter
# def facultyRoleId(self, facultyRoleId):
#     self.__facultyRoleId = facultyRoleId
#
# @facultyRoleId.deleter
# def facultyRoleId(self):
#     del self.__facultyRoleId
#
# # PROPERTY --> facultyisEmailVerified
# @property
# def facultyisEmailVerified(self):
#     return self.__facultyisEmailVerified
#
# @facultyisEmailVerified.setter
# def facultyisEmailVerified(self, facultyisEmailVerified):
#     self.__facultyisEmailVerified = facultyisEmailVerified
#
# @facultyisEmailVerified.deleter
# def facultyisEmailVerified(self):
#     del self.__facultyisEmailVerified
#
# # PROPERTY --> facultyisMobileNumberVerified
# @property
# def facultyisMobileNumberVerified(self):
#     return self.__facultyisMobileNumberVerified
#
# @facultyisMobileNumberVerified.setter
# def facultyisMobileNumberVerified(self, facultyisMobileNumberVerified):
#     self.__facultyisMobileNumberVerified = facultyisMobileNumberVerified
#
# @facultyisMobileNumberVerified.deleter
# def facultyisMobileNumberVerified(self):
#     del self.__facultyisMobileNumberVerified
#
# # PROPERTY --> username
# @property
# def username(self):
#     return self.__username
#
# @username.setter
# def username(self, username):
#     self.__username = username
#
# @username.deleter
# def username(self):
#     del self.__username
#
# # PROPERTY --> password
# @property
# def password(self):
#     return self.__password
#
# @password.setter
# def password(self, password):
#     self.__password = password
#
# @password.deleter
# def password(self):
#     del self.__password
#
# # PROPERTY --> lastLoggedInTimeStamp
# @property
# def lastLoggedInTimeStamp(self):
#     return self.__lastLoggedInTimeStamp
#
# @lastLoggedInTimeStamp.setter
# def lastLoggedInTimeStamp(self, lastLoggedInTimeStamp):
#     self.__lastLoggedInTimeStamp = lastLoggedInTimeStamp
#
# @lastLoggedInTimeStamp.deleter
# def lastLoggedInTimeStamp(self):
#     del self.__lastLoggedInTimeStamp
#
# # PROPERTY --> lastLoggedOutTimeStamp
# @property
# def lastLoggedOutTimeStamp(self):
#     return self.__lastLoggedOutTimeStamp
#
# @lastLoggedOutTimeStamp.setter
# def lastLoggedOutTimeStamp(self, lastLoggedOutTimeStamp):
#     self.__lastLoggedOutTimeStamp = lastLoggedOutTimeStamp
#
# @lastLoggedOutTimeStamp.deleter
# def lastLoggedOutTimeStamp(self):
#     del self.__lastLoggedOutTimeStamp
#
# # PROPERTY --> lastModifiedPassword
# @property
# def lastModifiedPassword(self):
#     return self.__lastModifiedPassword
#
# @lastModifiedPassword.setter
# def lastModifiedPassword(self, lastModifiedPassword):
#     self.__lastModifiedPassword = lastModifiedPassword
#
# @lastModifiedPassword.deleter
# def lastModifiedPassword(self):
#     del self.__lastModifiedPassword
#
# # PROPERTY --> entityIdentifier
# @property
# def entityIdentifier(self):
#     return self.__entityIdentifier
#
# @entityIdentifier.setter
# def entityIdentifier(self, entityIdentifier):
#     self.__entityIdentifier = entityIdentifier
#
# @entityIdentifier.deleter
# def entityIdentifier(self):
#     del self.__entityIdentifier
