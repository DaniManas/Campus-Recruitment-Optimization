#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

from Entities import *


class Role(Base):
    __tablename__ = 'roles'

    RoleId = Column(Integer, primary_key=True, unique=True)
    RoleName = Column(String(30))
    RoleGroup = Column(String(20))

    def __init__(self,
                 RoleName="DefaultRoleName",
                 RoleGroup="DefaultRoleGroup"
                 ):
        self.__RoleName = RoleName
        self.__RoleGroup = RoleGroup

    def __repr__(self):
        reprString = """
        Role Object:
        Role Id: {}
        Role Name: {}
        Role Group: {}
        """.format(self.RoleName, self.RoleGroup, self.RoleGroup)
        return reprString

    # ============================================
    # =========== GETTERS AND SETTERS ============
    # ============================================

    # # PROPERTY --> RoleName
    # @property
    # def RoleName(self):
    #     return self.__RoleName
    #
    # @RoleName.setter
    # def RoleName(self, RoleName):
    #     self.__RoleName = RoleName
    #
    # @RoleName.deleter
    # def RoleName(self):
    #     del self.__RoleName
    #
    # # PROPERTY --> RoleGroup
    # @property
    # def RoleGroup(self):
    #     return self.__RoleGroup
    #
    # @RoleGroup.setter
    # def RoleGroup(self, RoleGroup):
    #     self.__RoleGroup = RoleGroup
    #
    # @RoleGroup.deleter
    # def RoleGroup(self):
    #     del self.__RoleGroup
    #
    #
