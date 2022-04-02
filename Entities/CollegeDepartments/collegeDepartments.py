#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------
from Entities import *


class Collegedepartment(Base):
    __tablename__ = 'collegedepartments'

    collegeDepartmentsId = Column(Integer, primary_key=True, unique=True)
    collegeDepartmentsName = Column(String(30))

    def __init__(self, collegeDepartmentsName="DefaultCollegeDepartmentsName"):
        self.__collegeDepartmentsName = collegeDepartmentsName

    def __repr__(self):
        reprString = """
        College Department Object:
        college Department Id: {}
        college Department Name: {}
        """.format(self.collegeId, self.collegeDepartmentsName)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================
    #
    # # PROPERTY --> collegeDepartmentsName
    # @property
    # def collegeDepartmentsName(self):
    #     return self.__collegeDepartmentsName
    #
    # @collegeDepartmentsName.setter
    # def collegeDepartmentsName(self, collegeDepartmentsName):
    #     self.__collegeDepartmentsName = collegeDepartmentsName
    #
    # @collegeDepartmentsName.deleter
    # def collegeDepartmentsName(self):
    #     del self.__collegeDepartmentsName
