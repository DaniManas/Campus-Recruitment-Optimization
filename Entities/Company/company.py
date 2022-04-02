#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------
from Entities import *


class Company(Base):
    __tablename__ = 'company'

    companyId = Column(Integer, primary_key=True, index=True)
    companyName = Column(String(30))
    companyLocation = Column(String(20))
    companyCompanyCategoryId = Column(ForeignKey('companycategory.companyCategoryId', ondelete='SET NULL'), index=True)

    companycategory = relationship('Companycategory')

    def __init__(self,
                 companyName="DefaultCompanyName",
                 companyLocation="DefaultCompanyLocation",
                 companyCompanyCategoryId=1):
        self.__companyName = companyName
        self.__companyLocation = companyLocation
        self.__companyCompanyCategoryId = companyCompanyCategoryId

    def __repr__(self):
        reprString = """
        Company Category Object:
        company Name: {}
        company Location: {}
        companyCompanyCategoryId: {}
        """.format(self.CompanycategoryId, self.CompanycategoryName, self.companyCompanyCategoryId)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================

    # # PROPERTY --> companyName
    # @property
    # def companyName(self):
    #     return self.__companyName
    #
    # @companyName.setter
    # def companyName(self, companyName):
    #     self.__companyName = companyName
    #
    # @companyName.deleter
    # def companyName(self):
    #     del self.__companyName
    #
    # # PROPERTY --> companyLocation
    # @property
    # def companyLocation(self):
    #     return self.__companyLocation
    #
    # @companyLocation.setter
    # def companyLocation(self, companyLocation):
    #     self.__companyLocation = companyLocation
    #
    # @companyLocation.deleter
    # def companyLocation(self):
    #     del self.__companyLocation
    #
    # # PROPERTY --> companyCompanyCategoryId
    # @property
    # def companyCompanyCategoryId(self):
    #     return self.__companyCompanyCategoryId
    #
    # @companyCompanyCategoryId.setter
    # def companyCompanyCategoryId(self, companyCompanyCategoryId):
    #     self.__companyCompanyCategoryId = companyCompanyCategoryId
    #
    # @companyCompanyCategoryId.deleter
    # def companyCompanyCategoryId(self):
    #     del self.__companyCompanyCategoryId
    #
    #
