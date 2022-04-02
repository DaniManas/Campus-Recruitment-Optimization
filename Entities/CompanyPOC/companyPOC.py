#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

from Entities import *


class Companypoc(Base):
    __tablename__ = 'companypoc'

    CompanyPOCId = Column(Integer, primary_key=True, index=True)
    companyPOCRoleId = Column(ForeignKey('roles.RoleId', ondelete='SET NULL'), index=True)
    companyPOCCompanyId = Column(ForeignKey('company.companyId', ondelete='SET NULL'), index=True)
    companyPOCCollegeId = Column(ForeignKey('college.collegeId', ondelete='SET NULL'), index=True)
    companyPOCFirstName = Column(String(100))
    companyPOCLastName = Column(String(100))
    companyPOCEmail = Column(VARCHAR(320), nullable=False, unique=True)
    companyPOCMobileNumber = Column(String(100), nullable=False, unique=True)
    companyPOCDesignation = Column(String(30))
    companyPOCEmailVerified = Column(Boolean)
    companyPOCMobileNumberVerified = Column(Boolean)
    username = Column(String(50))
    password = Column(String(300))
    companyPOClastLoggedInTimeStamp = Column(TIMESTAMP)
    companyPOClastLoggedOutTimeStamp = Column(TIMESTAMP)
    companyPOClastModifiedPassword = Column(TIMESTAMP)
    companyPOCentityIdentifier = Column(String(1))

    college = relationship('College')
    company = relationship('Company')
    role = relationship('Role')

    def __init__(self):
        self.__CompanyPOCId = "DefaultCompanyPOCId"
        self.__companyPOCRoleId = "DefaultcompanyPOCRoleId"
        self.__companyPOCCompanyId = "DefaultcompanyPOCCompanyId"
        self.__companyPOCCollegeId = "DefaultcompanyPOCCollegeId"
        self.__companyPOCFirstName = "DefaultcompanyPOCFirstName"
        self.__companyPOCLastName = "DefaultcompanyPOCLastName"
        self.__companyPOCEmail = "DefaultcompanyPOCEmail"
        self.__companyPOCMobileNumber = "DefaultcompanyPOCMobileNumber"
        self.__companyPOCDesignation = "DefaultcompanyPOCDesignation"
        self.__companyPOCEmailVerified = "DefaultcompanyPOCEmailVerified"
        self.__companyPOCMobileNumberVerified = "DefaultcompanyPOCMobileNumberVerified"
        self.__username = "Defaultusername"
        self.__password = "Defaultpassword"
        self.__companyPOClastLoggedInTimeStamp = "DefaultcompanyPOClastLoggedInTimeStamp"
        self.__companyPOClastLoggedOutTimeStamp = "DefaultcompanyPOClastLoggedOutTimeStamp"
        self.__companyPOClastModifiedPassword = "DefaultcompanyPOClastModifiedPassword"
        self.__companyPOCentityIdentifier = "DefaultcompanyPOCentityIdentifier"

    def __repr__(self):
        reprString = """
        CompanyPOC Object:
        companyPOC Id: {}
        companyPOC Name: {} {}
        companyPOC CollegeId: {}
        """.format(self.__CompanyPOCId, self.__companyPOCFirstName, self.__companyPOCLastName,
                   self.__companyPOCCollegeId)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================

    # # property --> CompanyPOCId
    # @property
    # def CompanyPOCId(self):
    #     return self.__CompanyPOCId
    #
    # @CompanyPOCId.setter
    # def CompanyPOCId(self, CompanyPOCId):
    #     self.__CompanyPOCId = CompanyPOCId
    #
    # @CompanyPOCId.deleter
    # def CompanyPOCId(self):
    #     del self.__CompanyPOCId
    #
    # # property --> companyPOCRoleId
    # @property
    # def companyPOCRoleId(self):
    #     return self.__companyPOCRoleId
    #
    # @companyPOCRoleId.setter
    # def companyPOCRoleId(self, companyPOCRoleId):
    #     self.__companyPOCRoleId = companyPOCRoleId
    #
    # @companyPOCRoleId.deleter
    # def companyPOCRoleId(self):
    #     del self.__companyPOCRoleId
    #
    # # property --> companyPOCCompanyId
    # @property
    # def companyPOCCompanyId(self):
    #     return self.__companyPOCCompanyId
    #
    # @companyPOCCompanyId.setter
    # def companyPOCCompanyId(self, companyPOCCompanyId):
    #     self.__companyPOCCompanyId = companyPOCCompanyId
    #
    # @companyPOCCompanyId.deleter
    # def companyPOCCompanyId(self):
    #     del self.__companyPOCCompanyId
    #
    # # property --> companyPOCCollegeId
    # @property
    # def companyPOCCollegeId(self):
    #     return self.__companyPOCCollegeId
    #
    # @companyPOCCollegeId.setter
    # def companyPOCCollegeId(self, companyPOCCollegeId):
    #     self.__companyPOCCollegeId = companyPOCCollegeId
    #
    # @companyPOCCollegeId.deleter
    # def companyPOCCollegeId(self):
    #     del self.__companyPOCCollegeId
    #
    # # property --> companyPOCFirstName
    # @property
    # def companyPOCFirstName(self):
    #     return self.__companyPOCFirstName
    #
    # @companyPOCFirstName.setter
    # def companyPOCFirstName(self, companyPOCFirstName):
    #     self.__companyPOCFirstName = companyPOCFirstName
    #
    # @companyPOCFirstName.deleter
    # def companyPOCFirstName(self):
    #     del self.__companyPOCFirstName
    #
    # # property --> companyPOCLastName
    # @property
    # def companyPOCLastName(self):
    #     return self.__companyPOCLastName
    #
    # @companyPOCLastName.setter
    # def companyPOCLastName(self, companyPOCLastName):
    #     self.__companyPOCLastName = companyPOCLastName
    #
    # @companyPOCLastName.deleter
    # def companyPOCLastName(self):
    #     del self.__companyPOCLastName
    #
    # # property --> companyPOCEmail
    # @property
    # def companyPOCEmail(self):
    #     return self.__companyPOCEmail
    #
    # @companyPOCEmail.setter
    # def companyPOCEmail(self, companyPOCEmail):
    #     self.__companyPOCEmail = companyPOCEmail
    #
    # @companyPOCEmail.deleter
    # def companyPOCEmail(self):
    #     del self.__companyPOCEmail
    #
    # # property --> companyPOCMobileNumber
    # @property
    # def companyPOCMobileNumber(self):
    #     return self.__companyPOCMobileNumber
    #
    # @companyPOCMobileNumber.setter
    # def companyPOCMobileNumber(self, companyPOCMobileNumber):
    #     self.__companyPOCMobileNumber = companyPOCMobileNumber
    #
    # @companyPOCMobileNumber.deleter
    # def companyPOCMobileNumber(self):
    #     del self.__companyPOCMobileNumber
    #
    # # property --> companyPOCDesignation
    # @property
    # def companyPOCDesignation(self):
    #     return self.__companyPOCDesignation
    #
    # @companyPOCDesignation.setter
    # def companyPOCDesignation(self, companyPOCDesignation):
    #     self.__companyPOCDesignation = companyPOCDesignation
    #
    # @companyPOCDesignation.deleter
    # def companyPOCDesignation(self):
    #     del self.__companyPOCDesignation
    #
    # # property --> companyPOCEmailVerified
    # @property
    # def companyPOCEmailVerified(self):
    #     return self.__companyPOCEmailVerified
    #
    # @companyPOCEmailVerified.setter
    # def companyPOCEmailVerified(self, companyPOCEmailVerified):
    #     self.__companyPOCEmailVerified = companyPOCEmailVerified
    #
    # @companyPOCEmailVerified.deleter
    # def companyPOCEmailVerified(self):
    #     del self.__companyPOCEmailVerified
    #
    # # property --> companyPOCMobileNumberVerified
    # @property
    # def companyPOCMobileNumberVerified(self):
    #     return self.__companyPOCMobileNumberVerified
    #
    # @companyPOCMobileNumberVerified.setter
    # def companyPOCMobileNumberVerified(self, companyPOCMobileNumberVerified):
    #     self.__companyPOCMobileNumberVerified = companyPOCMobileNumberVerified
    #
    # @companyPOCMobileNumberVerified.deleter
    # def companyPOCMobileNumberVerified(self):
    #     del self.__companyPOCMobileNumberVerified
    #
    # # property --> username
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
    # # property --> password
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
    # # property --> companyPOClastLoggedInTimeStamp
    # @property
    # def companyPOClastLoggedInTimeStamp(self):
    #     return self.__companyPOClastLoggedInTimeStamp
    #
    # @companyPOClastLoggedInTimeStamp.setter
    # def companyPOClastLoggedInTimeStamp(self, companyPOClastLoggedInTimeStamp):
    #     self.__companyPOClastLoggedInTimeStamp = companyPOClastLoggedInTimeStamp
    #
    # @companyPOClastLoggedInTimeStamp.deleter
    # def companyPOClastLoggedInTimeStamp(self):
    #     del self.__companyPOClastLoggedInTimeStamp
    #
    # # property --> companyPOClastLoggedOutTimeStamp
    # @property
    # def companyPOClastLoggedOutTimeStamp(self):
    #     return self.__companyPOClastLoggedOutTimeStamp
    #
    # @companyPOClastLoggedOutTimeStamp.setter
    # def companyPOClastLoggedOutTimeStamp(self, companyPOClastLoggedOutTimeStamp):
    #     self.__companyPOClastLoggedOutTimeStamp = companyPOClastLoggedOutTimeStamp
    #
    # @companyPOClastLoggedOutTimeStamp.deleter
    # def companyPOClastLoggedOutTimeStamp(self):
    #     del self.__companyPOClastLoggedOutTimeStamp
    #
    # # property --> companyPOClastModifiedPassword
    # @property
    # def companyPOClastModifiedPassword(self):
    #     return self.__companyPOClastModifiedPassword
    #
    # @companyPOClastModifiedPassword.setter
    # def companyPOClastModifiedPassword(self, companyPOClastModifiedPassword):
    #     self.__companyPOClastModifiedPassword = companyPOClastModifiedPassword
    #
    # @companyPOClastModifiedPassword.deleter
    # def companyPOClastModifiedPassword(self):
    #     del self.__companyPOClastModifiedPassword
    #
    # # property --> companyPOCentityIdentifier
    # @property
    # def companyPOCentityIdentifier(self):
    #     return self.__companyPOCentityIdentifier
    #
    # @companyPOCentityIdentifier.setter
    # def companyPOCentityIdentifier(self, companyPOCentityIdentifier):
    #     self.__companyPOCentityIdentifier = companyPOCentityIdentifier
    #
    # @companyPOCentityIdentifier.deleter
    # def companyPOCentityIdentifier(self):
    #     del self.__companyPOCentityIdentifier
