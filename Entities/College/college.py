from Entities import *


class College(Base):
    __tablename__ = 'college'

    collegeId = Column(Integer, primary_key=True, unique=True)
    collegeName = Column(String(100))
    collegeAddressLineOne = Column(String(100))
    collegeAddressLineTwo = Column(String(100))
    collegeCity = Column(String(15))
    collegeState = Column(String(20))
    collegeCountry = Column(String(20))
    collegePhoneNumber = Column(String(100))
    collegePrincipleFirstName = Column(String(100))
    collegePrincipleLastName = Column(String(100))
    collegePrincipleEmail = Column(VARCHAR(320), nullable=False, unique=True)
    collegePrincipleContactNumber = Column(String(100), nullable=False)
    collegeTPOFirstName = Column(String(100))
    collegeTPOLastName = Column(String(100))
    collegeTPOEmail = Column(VARCHAR(320), nullable=False, unique=True)
    collegeTPOContactNumber = Column(String(100), nullable=False, unique=True)
    collegeProfileCreateTimestamp = Column(TIMESTAMP)
    collegeProfileUpdateTimestamp = Column(TIMESTAMP)

    def __init__(self,
                 collegeName="DefaultCollegeName",
                 collegeAddress="DefaultCollegeAddress",
                 collegePhoneNumber="DefaultCollegePhoneNumber",

                 collegePrincipleFirstName="DefaultPrincipalFirstName",
                 collegePrincipleLastName="DefaultPrincipalLastName",
                 collegePrincipleEmail="DefaultPrincipalEmail@xyz.com",
                 collegePrincipleContactNumber="1234567890",

                 collegeTPOFirstName="DefaultTPOFirstName",
                 collegeTPOLastName="DefaultTPOLastName",
                 collegeTPOEmail="DefaultTPOEmail@xyz.com",
                 collegeTPOContactNumber="1234567890",

                 # TIMESTAMP DETAILS
                 collegeProfileCreateTimestamp=None,
                 collegeProfileUpdateTimestamp=None):
        self.__collegeName = collegeName
        self.__collegeAddress = collegeAddress
        self.__collegePhoneNumber = collegePhoneNumber
        self.__collegePrincipleFirstName = collegePrincipleFirstName
        self.__collegePrincipleLastName = collegePrincipleLastName
        self.__collegePrincipleEmail, = collegePrincipleEmail
        self.__collegePrincipleContactNumber = collegePrincipleContactNumber

        self.__collegeTPOFirstName = collegeTPOFirstName
        self.__collegeTPOLastName = collegeTPOLastName
        self.__collegeTPOEmail = collegeTPOEmail
        self.__collegeTPOContactNumber = collegeTPOContactNumber

        # TIMESTAMP DETAILS
        self.__collegeProfileCreateTimestamp = collegeProfileCreateTimestamp
        self.__collegeProfileUpdateTimestamp = collegeProfileUpdateTimestamp

    def __repr__(self):
        reprString = """
        College Object:
        collegeId: {}
        college Name: {}
        college Principle: {} {}
        collegeTPO: {} {}
        """.format(self.collegeId, self.collegeName, self.__collegePrincipleFirstName,
                   self.__collegePrincipleLastName, self.__collegeTPOFirstName, self.__collegeTPOLastName)
        return reprString

    # # ============================================
    # # =========== GETTERS AND SETTERS ============
    # # ============================================
    #
    # # PROPERTY - 1 --> COLLEGE NAME
    # @property
    # def collegeName(self):
    #     return self.__collegeName
    #
    # @collegeName.setter
    # def collegeName(self, collegeName):
    #     self.__collegeName = collegeName
    #
    # @collegeName.deleter
    # def collegeName(self):
    #     del self.__collegeName
    #
    # # PROPERTY - 2 --> COLLEGE ADDRESS
    # @property
    # def collegeAddress(self):
    #     return self.__collegeAddress
    #
    # @collegeAddress.setter
    # def collegeAddress(self, collegeAddress):
    #     self.__collegeAddress = collegeAddress
    #
    # @collegeAddress.deleter
    # def collegeAddress(self):
    #     del self.__collegeAddress
    #
    # # PROPERTY - 3 --> COLLEGE PHONE NUMBER
    # @property
    # def collegePhoneNumber(self):
    #     return self.__collegePhoneNumber
    #
    # @collegePhoneNumber.setter
    # def collegePhoneNumber(self, collegePhoneNumber):
    #     self.__collegePhoneNumber = collegePhoneNumber
    #
    # @collegePhoneNumber.deleter
    # def collegePhoneNumber(self):
    #     del self.__collegePhoneNumber
    #
    # # PROPERTY - 4 --> COLLEGE PRINCIPAL PHONE NUMBER
    # @property
    # def collegePrincipleFirstName(self):
    #     return self.__collegePrincipleFirstName
    #
    # @collegePrincipleFirstName.setter
    # def collegePrincipleFirstName(self, collegePrincipleFirstName):
    #     self.__collegePrincipleFirstName = collegePrincipleFirstName
    #
    # @collegePrincipleFirstName.deleter
    # def collegePrincipleFirstName(self):
    #     del self.__collegePrincipleFirstName
    #
    # # PROPERTY - 5 --> COLLEGE NAME
    # @property
    # def collegePrincipleFirstName(self):
    #     return self.__collegePrincipleFirstName
    #
    # @collegePrincipleFirstName.setter
    # def collegePrincipleFirstName(self, collegePrincipleFirstName):
    #     self.__collegePrincipleFirstName = collegePrincipleFirstName
    #
    # @collegePrincipleFirstName.deleter
    # def collegePrincipleFirstName(self):
    #     del self.__collegePrincipleFirstName
    #
    # # PROPERTY --> collegePrincipleLastName
    # @property
    # def collegePrincipleLastName(self):
    #     return self.__collegePrincipleLastName
    #
    # @collegePrincipleLastName.setter
    # def collegePrincipleLastName(self, collegePrincipleLastName):
    #     self.__collegePrincipleLastName = collegePrincipleLastName
    #
    # @collegePrincipleLastName.deleter
    # def collegePrincipleLastName(self):
    #     del self.__collegePrincipleLastName
    #
    # # PROPERTY --> collegePrincipleEmail
    # @property
    # def collegePrincipleEmail(self):
    #     return self.__collegePrincipleEmail
    #
    # @collegePrincipleEmail.setter
    # def collegePrincipleEmail(self, collegePrincipleEmail):
    #     self.__collegePrincipleEmail = collegePrincipleEmail
    #
    # @collegePrincipleEmail.deleter
    # def collegePrincipleEmail(self):
    #     del self.__collegePrincipleEmail
    #
    # # PROPERTY --> collegePrincipleContactNumber
    # @property
    # def collegePrincipleContactNumber(self):
    #     return self.__collegePrincipleContactNumber
    #
    # @collegePrincipleContactNumber.setter
    # def collegePrincipleContactNumber(self, collegePrincipleContactNumber):
    #     self.__collegePrincipleContactNumber = collegePrincipleContactNumber
    #
    # @collegePrincipleContactNumber.deleter
    # def collegePrincipleContactNumber(self):
    #     del self.__collegePrincipleContactNumber
    #
    # # PROPERTY --> collegeTPOFirstName
    # @property
    # def collegeTPOFirstName(self):
    #     return self.__collegeTPOFirstName
    #
    # @collegeTPOFirstName.setter
    # def collegeTPOFirstName(self, collegeTPOFirstName):
    #     self.__collegeTPOFirstName = collegeTPOFirstName
    #
    # @collegeTPOFirstName.deleter
    # def collegeTPOFirstName(self):
    #     del self.__collegeTPOFirstName
    #
    # # PROPERTY --> collegeTPOLastName
    # @property
    # def collegeTPOLastName(self):
    #     return self.__collegeTPOLastName
    #
    # @collegeTPOLastName.setter
    # def collegeTPOLastName(self, collegeTPOLastName):
    #     self.__collegeTPOLastName = collegeTPOLastName
    #
    # @collegeTPOLastName.deleter
    # def collegeTPOLastName(self):
    #     del self.__collegeTPOLastName
    #
    # # PROPERTY --> collegeTPOEmail
    # @property
    # def collegeTPOEmail(self):
    #     return self.__collegeTPOEmail
    #
    # @collegeTPOEmail.setter
    # def collegeTPOEmail(self, collegeTPOEmail):
    #     self.__collegeTPOEmail = collegeTPOEmail
    #
    # @collegeTPOEmail.deleter
    # def collegeTPOEmail(self):
    #     del self.__collegeTPOEmail
    #
    # # PROPERTY --> collegeProfileCreateTimestamp
    # @property
    # def collegeProfileCreateTimestamp(self):
    #     return self.__collegeProfileCreateTimestamp
    #
    # @collegeProfileCreateTimestamp.setter
    # def collegeProfileCreateTimestamp(self, collegeProfileCreateTimestamp):
    #     self.__collegeProfileCreateTimestamp = collegeProfileCreateTimestamp
    #
    # @collegeProfileCreateTimestamp.deleter
    # def collegeProfileCreateTimestamp(self):
    #     del self.__collegeProfileCreateTimestamp
    #
    # # PROPERTY --> collegeProfileUpdateTimestamp
    # @property
    # def collegeProfileUpdateTimestamp(self):
    #     return self.__collegeProfileUpdateTimestamp
    #
    # @collegeProfileUpdateTimestamp.setter
    # def collegeProfileUpdateTimestamp(self, collegeProfileUpdateTimestamp):
    #     self.__collegeProfileUpdateTimestamp = collegeProfileUpdateTimestamp
    #
    # @collegeProfileUpdateTimestamp.deleter
    # def collegeProfileUpdateTimestamp(self):
    #     del self.__collegeProfileUpdateTimestamp
