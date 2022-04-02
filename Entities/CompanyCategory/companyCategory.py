#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------
from Entities import *


class companyCategory(Base):
    __tablename__ = 'companycategory'

    companyCategoryId = Column(Integer, primary_key=True)
    companyCategoryName = Column(String(30))

    def __init__(self,companyCategoryName="DefaultCompanyCategoryName"):
        self.__companyCategoryName = companyCategoryName

    def __repr__(self):
        reprString = """
        Company Category Object:
        Company Category Id: {}
        Company Category Name: {}
        """.format(self.companyCategoryId, self.companyCategoryName)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================

    # # PROPERTY --> CompanycategoryName
    # @property
    # def CompanycategoryName(self):
    #     return self.__CompanycategoryName
    #
    # @CompanycategoryName.setter
    # def CompanycategoryName(self, CompanycategoryName):
    #     self.__CompanycategoryName = CompanycategoryName
    #
    # @CompanycategoryName.deleter
    # def CompanycategoryName(self):
    #     del self.__CompanycategoryName

