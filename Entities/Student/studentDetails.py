#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

from Entities import *


class Studentdetail(Base):
    __tablename__ = 'studentdetails'

    studentId = Column(Integer, primary_key=True, unique=True)
    studentRegistrationId = Column(String(11), nullable=False, unique=True)
    studentRollNumber = Column(Integer, nullable=False, unique=True)
    studentGender = Column(String(1))
    studentNationality = Column(String(20))
    studentRoleId = Column(ForeignKey('roles.RoleId', ondelete='SET NULL'), index=True)
    studentFirstName = Column(String(100))
    studentFathersName = Column(String(300))
    studentMothersName = Column(String(300))
    studentLastName = Column(String(100))
    studentEmail = Column(VARCHAR(320), nullable=False, unique=True)
    studentMobileNumber = Column(String(100), nullable=False, unique=True)
    studentAadhar = Column(String(100), nullable=False, unique=True)
    studentPAN = Column(String(100), unique=True)
    studentPassport = Column(String(100), unique=True)
    studentPermanantAddress = Column(String(500))
    studentResidentialAddress = Column(String(500))
    studentisAadhar = Column(Boolean)
    studentisPAN = Column(Boolean)
    studentisPassport = Column(Boolean)
    studentisIndian = Column(Boolean)
    isEmailVerified = Column(Boolean)
    isMobileNumberVerified = Column(Boolean)
    studentCollegeId = Column(ForeignKey('college.collegeId', ondelete='SET NULL'), index=True)
    studentDepartmentId = Column(ForeignKey('collegedepartments.collegeDepartmentsId', ondelete='SET NULL'), index=True)
    studentCompanyId = Column(ForeignKey('company.companyId', ondelete='SET NULL'), index=True)
    isPlaced = Column(Boolean)
    placementTime = Column(TIMESTAMP)
    placementSalary = Column(Float)
    username = Column(String(50))
    password = Column(String(300))
    lastLoggedInTimeStamp = Column(TIMESTAMP)
    lastLoggedOutTimeStamp = Column(TIMESTAMP)
    lastModifiedPassword = Column(TIMESTAMP)
    studentisDocumentVerified = Column(Boolean)
    studentDocumentUpdateTimestamp = Column(TIMESTAMP)
    studentDocumentCreateTimestamp = Column(TIMESTAMP)
    studentProfileCreationTimestamp = Column(TIMESTAMP)
    studentProfileUpdateTimestamp = Column(TIMESTAMP)
    studentDeleteProfileFlag = Column(Boolean)
    entityIdentifier = Column(String(1))
    studentLinkedInUsername = Column(String(30))
    studentHackerRankUsername = Column(String(30))
    studentCodeChefUsername = Column(String(30))
    studentResume = Column(String(50))

    college = relationship('College')
    company = relationship('Company')
    collegedepartment = relationship('Collegedepartment')
    role = relationship('Role')

    def __init__(self, studentId=None,
                 studentRegistrationId=None,
                 studentRollNumber=None,
                 studentGender=None,
                 studentNationality=None,
                 studentRoleId=None,
                 studentFirstName=None,
                 studentFathersName=None,
                 studentMothersName=None,
                 studentLastName=None,
                 studentEmail=None,
                 studentMobileNumber=None,
                 studentAadhar=None,
                 studentPAN=None,
                 studentPassport=None,
                 studentPermanantAddress=None,
                 studentResidentialAddress=None,
                 studentisAadhar=None,
                 studentisPAN=None,
                 studentisPassport=None,
                 studentisIndian=None,
                 isEmailVerified=None,
                 isMobileNumberVerified=None,
                 studentCollegeId=None,
                 studentDepartmentId=None,
                 studentCompanyId=None,
                 isPlaced=None,
                 placementTime=None,
                 placementSalary=None,
                 username=None,
                 password=None,
                 lastLoggedInTimeStamp=None,
                 lastLoggedOutTimeStamp=None,
                 lastModifiedPassword=None,
                 studentisDocumentVerified=None,
                 studentDocumentUpdateTimestamp=None,
                 studentDocumentCreateTimestamp=None,
                 studentProfileCreationTimestamp=None,
                 studentProfileUpdateTimestamp=None,
                 studentDeleteProfileFlag=None,
                 entityIdentifier=None,
                 studentLinkedInUsername=None,
                 studentHackerRankUsername=None,
                 studentCodeChefUsername=None,
                 studentResume=None,
                 ):
        self.__studentId = studentId
        self.__studentRegistrationId = studentRegistrationId
        self.__studentRollNumber = studentRollNumber
        self.__studentGender = studentGender
        self.__studentNationality = studentNationality
        self.__studentRoleId = studentRoleId
        self.__studentFirstName = studentFirstName
        self.__studentFathersName = studentFathersName
        self.__studentMothersName = studentMothersName
        self.__studentLastName = studentLastName
        self.__studentEmail = studentEmail
        self.__studentMobileNumber = studentMobileNumber
        self.__studentAadhar = studentAadhar
        self.__studentPAN = studentPAN
        self.__studentPassport = studentPassport
        self.__studentPermanantAddress = studentPermanantAddress
        self.__studentResidentialAddress = studentResidentialAddress
        self.__studentisAadhar = studentisAadhar
        self.__studentisPAN = studentisPAN
        self.__studentisPassport = studentisPassport
        self.__studentisIndian = studentisIndian
        self.__isEmailVerified = isEmailVerified
        self.__isMobileNumberVerified = isMobileNumberVerified
        self.__studentCollegeId = studentCollegeId
        self.__studentDepartmentId = studentDepartmentId
        self.__studentCompanyId = studentCompanyId
        self.__isPlaced = isPlaced
        self.__placementTime = placementTime
        self.__placementSalary = placementSalary
        self.__username = username
        self.__password = password
        self.__lastLoggedInTimeStamp = lastLoggedInTimeStamp
        self.__lastLoggedOutTimeStamp = lastLoggedOutTimeStamp
        self.__lastModifiedPassword = lastModifiedPassword
        self.__studentisDocumentVerified = studentisDocumentVerified
        self.__studentDocumentUpdateTimestamp = studentDocumentUpdateTimestamp
        self.__studentDocumentCreateTimestamp = studentDocumentCreateTimestamp
        self.__studentProfileCreationTimestamp = studentProfileCreationTimestamp
        self.__studentProfileUpdateTimestamp = studentProfileUpdateTimestamp
        self.__studentDeleteProfileFlag = studentDeleteProfileFlag
        self.__entityIdentifier = entityIdentifier
        self.__studentLinkedInUsername = studentLinkedInUsername
        self.__studentHackerRankUsername = studentHackerRankUsername
        self.__studentCodeChefUsername = studentCodeChefUsername
        self.__studentResume = studentResume

    def __repr__(self):
        reprString = """
        Student Details Object:
        Student Id: {}
        Student Name: {}
        Student Group: {}
        """.format(self.RoleName, self.RoleGroup, self.RoleGroup)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================
    # # property --> studentRegistrationId
    # @property
    # def studentRegistrationId(self):
    #     return self.__studentRegistrationId
    #
    # @studentRegistrationId.setter
    # def studentRegistrationId(self, studentRegistrationId):
    #     self.__studentRegistrationId = studentRegistrationId
    #
    # @studentRegistrationId.deleter
    # def studentRegistrationId(self):
    #     del self.__studentRegistrationId
    #
    # # property --> studentRollNumber
    # @property
    # def studentRollNumber(self):
    #     return self.__studentRollNumber
    #
    # @studentRollNumber.setter
    # def studentRollNumber(self, studentRollNumber):
    #     self.__studentRollNumber = studentRollNumber
    #
    # @studentRollNumber.deleter
    # def studentRollNumber(self):
    #     del self.__studentRollNumber
    #
    # # property --> studentGender
    # @property
    # def studentGender(self):
    #     return self.__studentGender
    #
    # @studentGender.setter
    # def studentGender(self, studentGender):
    #     self.__studentGender = studentGender
    #
    # @studentGender.deleter
    # def studentGender(self):
    #     del self.__studentGender
    #
    # # property --> studentNationality
    # @property
    # def studentNationality(self):
    #     return self.__studentNationality
    #
    # @studentNationality.setter
    # def studentNationality(self, studentNationality):
    #     self.__studentNationality = studentNationality
    #
    # @studentNationality.deleter
    # def studentNationality(self):
    #     del self.__studentNationality
    #
    # # property --> studentRoleId
    # @property
    # def studentRoleId(self):
    #     return self.__studentRoleId
    #
    # @studentRoleId.setter
    # def studentRoleId(self, studentRoleId):
    #     self.__studentRoleId = studentRoleId
    #
    # @studentRoleId.deleter
    # def studentRoleId(self):
    #     del self.__studentRoleId
    #
    # # property --> studentFirstName
    # @property
    # def studentFirstName(self):
    #     return self.__studentFirstName
    #
    # @studentFirstName.setter
    # def studentFirstName(self, studentFirstName):
    #     self.__studentFirstName = studentFirstName
    #
    # @studentFirstName.deleter
    # def studentFirstName(self):
    #     del self.__studentFirstName
    #
    # # property --> studentFathersName
    # @property
    # def studentFathersName(self):
    #     return self.__studentFathersName
    #
    # @studentFathersName.setter
    # def studentFathersName(self, studentFathersName):
    #     self.__studentFathersName = studentFathersName
    #
    # @studentFathersName.deleter
    # def studentFathersName(self):
    #     del self.__studentFathersName
    #
    # # property --> studentMothersName
    # @property
    # def studentMothersName(self):
    #     return self.__studentMothersName
    #
    # @studentMothersName.setter
    # def studentMothersName(self, studentMothersName):
    #     self.__studentMothersName = studentMothersName
    #
    # @studentMothersName.deleter
    # def studentMothersName(self):
    #     del self.__studentMothersName
    #
    # # property --> studentLastName
    # @property
    # def studentLastName(self):
    #     return self.__studentLastName
    #
    # @studentLastName.setter
    # def studentLastName(self, studentLastName):
    #     self.__studentLastName = studentLastName
    #
    # @studentLastName.deleter
    # def studentLastName(self):
    #     del self.__studentLastName
    #
    # # property --> studentEmail
    # @property
    # def studentEmail(self):
    #     return self.__studentEmail
    #
    # @studentEmail.setter
    # def studentEmail(self, studentEmail):
    #     self.__studentEmail = studentEmail
    #
    # @studentEmail.deleter
    # def studentEmail(self):
    #     del self.__studentEmail
    #
    # # property --> studentMobileNumber
    # @property
    # def studentMobileNumber(self):
    #     return self.__studentMobileNumber
    #
    # @studentMobileNumber.setter
    # def studentMobileNumber(self, studentMobileNumber):
    #     self.__studentMobileNumber = studentMobileNumber
    #
    # @studentMobileNumber.deleter
    # def studentMobileNumber(self):
    #     del self.__studentMobileNumber
    #
    # # property --> studentAadhar
    # @property
    # def studentAadhar(self):
    #     return self.__studentAadhar
    #
    # @studentAadhar.setter
    # def studentAadhar(self, studentAadhar):
    #     self.__studentAadhar = studentAadhar
    #
    # @studentAadhar.deleter
    # def studentAadhar(self):
    #     del self.__studentAadhar
    #
    # # property --> studentPAN
    # @property
    # def studentPAN(self):
    #     return self.__studentPAN
    #
    # @studentPAN.setter
    # def studentPAN(self, studentPAN):
    #     self.__studentPAN = studentPAN
    #
    # @studentPAN.deleter
    # def studentPAN(self):
    #     del self.__studentPAN
    #
    # # property --> studentPassport
    # @property
    # def studentPassport(self):
    #     return self.__studentPassport
    #
    # @studentPassport.setter
    # def studentPassport(self, studentPassport):
    #     self.__studentPassport = studentPassport
    #
    # @studentPassport.deleter
    # def studentPassport(self):
    #     del self.__studentPassport
    #
    # # property --> studentPermanantAddress
    # @property
    # def studentPermanantAddress(self):
    #     return self.__studentPermanantAddress
    #
    # @studentPermanantAddress.setter
    # def studentPermanantAddress(self, studentPermanantAddress):
    #     self.__studentPermanantAddress = studentPermanantAddress
    #
    # @studentPermanantAddress.deleter
    # def studentPermanantAddress(self):
    #     del self.__studentPermanantAddress
    #
    # # property --> studentResidentialAddress
    # @property
    # def studentResidentialAddress(self):
    #     return self.__studentResidentialAddress
    #
    # @studentResidentialAddress.setter
    # def studentResidentialAddress(self, studentResidentialAddress):
    #     self.__studentResidentialAddress = studentResidentialAddress
    #
    # @studentResidentialAddress.deleter
    # def studentResidentialAddress(self):
    #     del self.__studentResidentialAddress
    #
    # # property --> studentisAadhar
    # @property
    # def studentisAadhar(self):
    #     return self.__studentisAadhar
    #
    # @studentisAadhar.setter
    # def studentisAadhar(self, studentisAadhar):
    #     self.__studentisAadhar = studentisAadhar
    #
    # @studentisAadhar.deleter
    # def studentisAadhar(self):
    #     del self.__studentisAadhar
    #
    # # property --> studentisPAN
    # @property
    # def studentisPAN(self):
    #     return self.__studentisPAN
    #
    # @studentisPAN.setter
    # def studentisPAN(self, studentisPAN):
    #     self.__studentisPAN = studentisPAN
    #
    # @studentisPAN.deleter
    # def studentisPAN(self):
    #     del self.__studentisPAN
    #
    # # property --> studentisPassport
    # @property
    # def studentisPassport(self):
    #     return self.__studentisPassport
    #
    # @studentisPassport.setter
    # def studentisPassport(self, studentisPassport):
    #     self.__studentisPassport = studentisPassport
    #
    # @studentisPassport.deleter
    # def studentisPassport(self):
    #     del self.__studentisPassport
    #
    # # property --> studentisIndian
    # @property
    # def studentisIndian(self):
    #     return self.__studentisIndian
    #
    # @studentisIndian.setter
    # def studentisIndian(self, studentisIndian):
    #     self.__studentisIndian = studentisIndian
    #
    # @studentisIndian.deleter
    # def studentisIndian(self):
    #     del self.__studentisIndian
    #
    # # property --> isEmailVerified
    # @property
    # def isEmailVerified(self):
    #     return self.__isEmailVerified
    #
    # @isEmailVerified.setter
    # def isEmailVerified(self, isEmailVerified):
    #     self.__isEmailVerified = isEmailVerified
    #
    # @isEmailVerified.deleter
    # def isEmailVerified(self):
    #     del self.__isEmailVerified
    #
    # # property --> isMobileNumberVerified
    # @property
    # def isMobileNumberVerified(self):
    #     return self.__isMobileNumberVerified
    #
    # @isMobileNumberVerified.setter
    # def isMobileNumberVerified(self, isMobileNumberVerified):
    #     self.__isMobileNumberVerified = isMobileNumberVerified
    #
    # @isMobileNumberVerified.deleter
    # def isMobileNumberVerified(self):
    #     del self.__isMobileNumberVerified
    #
    # # property --> studentCollegeId
    # @property
    # def studentCollegeId(self):
    #     return self.__studentCollegeId
    #
    # @studentCollegeId.setter
    # def studentCollegeId(self, studentCollegeId):
    #     self.__studentCollegeId = studentCollegeId
    #
    # @studentCollegeId.deleter
    # def studentCollegeId(self):
    #     del self.__studentCollegeId
    #
    # # property --> studentDepartmentId
    # @property
    # def studentDepartmentId(self):
    #     return self.__studentDepartmentId
    #
    # @studentDepartmentId.setter
    # def studentDepartmentId(self, studentDepartmentId):
    #     self.__studentDepartmentId = studentDepartmentId
    #
    # @studentDepartmentId.deleter
    # def studentDepartmentId(self):
    #     del self.__studentDepartmentId
    #
    # # property --> studentCompanyId
    # @property
    # def studentCompanyId(self):
    #     return self.__studentCompanyId
    #
    # @studentCompanyId.setter
    # def studentCompanyId(self, studentCompanyId):
    #     self.__studentCompanyId = studentCompanyId
    #
    # @studentCompanyId.deleter
    # def studentCompanyId(self):
    #     del self.__studentCompanyId
    #
    # # property --> isPlaced
    # @property
    # def isPlaced(self):
    #     return self.__isPlaced
    #
    # @isPlaced.setter
    # def isPlaced(self, isPlaced):
    #     self.__isPlaced = isPlaced
    #
    # @isPlaced.deleter
    # def isPlaced(self):
    #     del self.__isPlaced
    #
    # # property --> placementTime
    # @property
    # def placementTime(self):
    #     return self.__placementTime
    #
    # @placementTime.setter
    # def placementTime(self, placementTime):
    #     self.__placementTime = placementTime
    #
    # @placementTime.deleter
    # def placementTime(self):
    #     del self.__placementTime
    #
    # # property --> placementSalary
    # @property
    # def placementSalary(self):
    #     return self.__placementSalary
    #
    # @placementSalary.setter
    # def placementSalary(self, placementSalary):
    #     self.__placementSalary = placementSalary
    #
    # @placementSalary.deleter
    # def placementSalary(self):
    #     del self.__placementSalary
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
    # # property --> lastLoggedInTimeStamp
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
    # # property --> lastLoggedOutTimeStamp
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
    # # property --> lastModifiedPassword
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
    # # property --> studentisDocumentVerified
    # @property
    # def studentisDocumentVerified(self):
    #     return self.__studentisDocumentVerified
    #
    # @studentisDocumentVerified.setter
    # def studentisDocumentVerified(self, studentisDocumentVerified):
    #     self.__studentisDocumentVerified = studentisDocumentVerified
    #
    # @studentisDocumentVerified.deleter
    # def studentisDocumentVerified(self):
    #     del self.__studentisDocumentVerified
    #
    # # property --> studentDocumentUpdateTimestamp
    # @property
    # def studentDocumentUpdateTimestamp(self):
    #     return self.__studentDocumentUpdateTimestamp
    #
    # @studentDocumentUpdateTimestamp.setter
    # def studentDocumentUpdateTimestamp(self, studentDocumentUpdateTimestamp):
    #     self.__studentDocumentUpdateTimestamp = studentDocumentUpdateTimestamp
    #
    # @studentDocumentUpdateTimestamp.deleter
    # def studentDocumentUpdateTimestamp(self):
    #     del self.__studentDocumentUpdateTimestamp
    #
    # # property --> studentDocumentCreateTimestamp
    # @property
    # def studentDocumentCreateTimestamp(self):
    #     return self.__studentDocumentCreateTimestamp
    #
    # @studentDocumentCreateTimestamp.setter
    # def studentDocumentCreateTimestamp(self, studentDocumentCreateTimestamp):
    #     self.__studentDocumentCreateTimestamp = studentDocumentCreateTimestamp
    #
    # @studentDocumentCreateTimestamp.deleter
    # def studentDocumentCreateTimestamp(self):
    #     del self.__studentDocumentCreateTimestamp
    #
    # # property --> studentProfileCreationTimestamp
    # @property
    # def studentProfileCreationTimestamp(self):
    #     return self.__studentProfileCreationTimestamp
    #
    # @studentProfileCreationTimestamp.setter
    # def studentProfileCreationTimestamp(self, studentProfileCreationTimestamp):
    #     self.__studentProfileCreationTimestamp = studentProfileCreationTimestamp
    #
    # @studentProfileCreationTimestamp.deleter
    # def studentProfileCreationTimestamp(self):
    #     del self.__studentProfileCreationTimestamp
    #
    # # property --> studentProfileUpdateTimestamp
    # @property
    # def studentProfileUpdateTimestamp(self):
    #     return self.__studentProfileUpdateTimestamp
    #
    # @studentProfileUpdateTimestamp.setter
    # def studentProfileUpdateTimestamp(self, studentProfileUpdateTimestamp):
    #     self.__studentProfileUpdateTimestamp = studentProfileUpdateTimestamp
    #
    # @studentProfileUpdateTimestamp.deleter
    # def studentProfileUpdateTimestamp(self):
    #     del self.__studentProfileUpdateTimestamp
    #
    # # property --> studentDeleteProfileFlag
    # @property
    # def studentDeleteProfileFlag(self):
    #     return self.__studentDeleteProfileFlag
    #
    # @studentDeleteProfileFlag.setter
    # def studentDeleteProfileFlag(self, studentDeleteProfileFlag):
    #     self.__studentDeleteProfileFlag = studentDeleteProfileFlag
    #
    # @studentDeleteProfileFlag.deleter
    # def studentDeleteProfileFlag(self):
    #     del self.__studentDeleteProfileFlag
    #
    # # property --> entityIdentifier
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
    #
    # # property --> studentLinkedInUsername
    # @property
    # def studentLinkedInUsername(self):
    #     return self.__studentLinkedInUsername
    #
    # @studentLinkedInUsername.setter
    # def studentLinkedInUsername(self, studentLinkedInUsername):
    #     self.__studentLinkedInUsername = studentLinkedInUsername
    #
    # @studentLinkedInUsername.deleter
    # def studentLinkedInUsername(self):
    #     del self.__studentLinkedInUsername
    #
    # # property --> studentHackerRankUsername
    # @property
    # def studentHackerRankUsername(self):
    #     return self.__studentHackerRankUsername
    #
    # @studentHackerRankUsername.setter
    # def studentHackerRankUsername(self, studentHackerRankUsername):
    #     self.__studentHackerRankUsername = studentHackerRankUsername
    #
    # @studentHackerRankUsername.deleter
    # def studentHackerRankUsername(self):
    #     del self.__studentHackerRankUsername
    #
    # # property --> studentCodeChefUsername
    # @property
    # def studentCodeChefUsername(self):
    #     return self.__studentCodeChefUsername
    #
    # @studentCodeChefUsername.setter
    # def studentCodeChefUsername(self, studentCodeChefUsername):
    #     self.__studentCodeChefUsername = studentCodeChefUsername
    #
    # @studentCodeChefUsername.deleter
    # def studentCodeChefUsername(self):
    #     del self.__studentCodeChefUsername
    #
    # # property --> studentResume
    # @property
    # def studentResume(self):
    #     return self.__studentResume
    #
    # @studentResume.setter
    # def studentResume(self, studentResume):
    #     self.__studentResume = studentResume
    #
    # @studentResume.deleter
    # def studentResume(self):
    #     del self.__studentResume
