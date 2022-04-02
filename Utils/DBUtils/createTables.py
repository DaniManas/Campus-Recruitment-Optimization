#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

from Entities.College.college import *
from Entities.CollegeDepartments.collegeDepartments import *
from Entities.CompanyCategory.companyCategory import *
from Entities.Roles.roles import *
from Entities.Company.company import *
from Entities.Faculty.faculty import *
from Entities.CollegeCompany.collegeCompany import *
from Entities.CompanyPOC.companyPOC import *
from Entities.Student.studentDetails import *
from Entities.StudentExtended.studentDetailsExtended import *
from Entities import *


def createTablesUsingSQLAlchemy():
    metadata.create_all(bind=engine)
# createTablesUsingSQLAlchemy()
