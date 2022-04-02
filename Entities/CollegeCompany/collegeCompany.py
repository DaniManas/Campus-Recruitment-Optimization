#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------
from Entities import *


class Collegecompany(Base):
    __tablename__ = 'collegecompany'

    CCId = Column(Integer, primary_key=True, index=True)
    CCCompanyVisitYear = Column(DateTime)
    CCCompanySalaryOffered = Column(Float)
    CCCompanyJD = Column(String(50))
    CCCompanyRoleNameOffered = Column(String(50))
    CCJobLocationOffered = Column(String(30))
    CCCollegeId = Column(ForeignKey('college.collegeId', ondelete='SET NULL'), index=True)
    CCCompanyId = Column(ForeignKey('company.companyId', ondelete='SET NULL'), index=True)
    CCProfileCreateTimestamp = Column(TIMESTAMP)
    CCProfileUpdateTimestamp = Column(TIMESTAMP)

    college = relationship('College')
    company = relationship('Company')

    def __init__(self,
                 CCCompanyVisitYear=1900,
                 CCCompanySalaryOffered=0.0,
                 CCCompanyJD="DefaultPathToJD",
                 CCCompanyRoleNameOffered="DefaultSDERole",
                 CCJobLocationOffered="DefaultLocation",
                 CCCollegeId=None,
                 CCCompanyId=None,
                 CCProfileCreateTimestamp=None,
                 CCProfileUpdateTimestamp=None
                 ):
        self.__CCCompanyVisitYear = CCCompanyVisitYear,
        self.__CCCompanySalaryOffered = CCCompanySalaryOffered,
        self.__CCCompanyJD = CCCompanyJD,
        self.__CCCompanyRoleNameOffered = CCCompanyRoleNameOffered,
        CCJobLocationOffered = CCJobLocationOffered,
        self.__CCCollegeId = CCCollegeId,
        self.__CCCompanyId = CCCompanyId,
        self.__CCProfileCreateTimestamp = CCProfileCreateTimestamp
        self.__CCProfileUpdateTimestamp = CCProfileUpdateTimestamp


def __repr__(self):
    reprString = """
        College Company Object:
        CollegeCompany Id: {}
        College Id: {}
        Company Id: {}
        """.format(self.CCId, self.CCCollegeId, self.CCCompanyId)
    return reprString

# ============================================
# =========== GETTERS AND SETTERS ============
# ============================================

# # PROPERTY --> companyCategoryName
# @property
# def companyCategoryName(self):
#     return self.__companyCategoryName
#
# @companyCategoryName.setter
# def companyCategoryName(self, companyCategoryName):
#     self.__companyCategoryName = companyCategoryName
#
# @companyCategoryName.deleter
# def companyCategoryName(self):
#     del self.__companyCategoryName
