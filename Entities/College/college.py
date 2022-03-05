class College:
    # Attributes
    __collegeId = 1

    __collegeName = "DefaultCollege"
    __collegeAddress = "DefaultCollegeAddress"
    __collegePhoneNumber = "DefaultCollegePhoneNumber"
    __collegePrincipleFirstName = "DefaultPrincipalFirstName"
    __collegePrincipleLastName = "DefaultPrincipalLastName"
    __collegePrincipleEmail, = "DefaultPrincipalEmail@xyz.com"
    __collegePrincipleContactNumber = "1234567890"

    __collegeTPOFirstName = "DefaultTPOFirstName"
    __collegeTPOLastName = "DefaultTPOLastName"
    __collegeTPOEmail = "DefaultTPOEmail@xyz.com"
    __collegeTPOContactNumber = "1234567890"

    # TIMESTAMP DETAILS
    __collegeProfileCreateTimestamp = ""
    __collegeProfileUpdateTimestamp = ""

    def __init__(self, college):
        self.__collegeName = college.__collegeName
        self.__collegeAddress = college.__collegeAddress
        self.__collegePhoneNumber = college.__collegePhoneNumber
        self.__collegePrincipleFirstName = college.__collegePrincipleFirstName
        self.__collegePrincipleLastName = college.__collegePrincipleLastName
        self.__collegePrincipleEmail = college.__collegePrincipleEmail
        self.__collegePrincipleContactNumber = college.__collegePrincipleContactNumber
        self.__collegeTPOFirstName = college.__collegeTPOFirstName
        self.__collegeTPOLastName = college.__collegeTPOLastName
        self.