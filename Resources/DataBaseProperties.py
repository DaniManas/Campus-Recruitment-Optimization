#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

# DATABASE NAME
DB_NAME = "TNP_MADE_EASY"
DB_USER_NAME = "tnpRoot"
DB_PASSWORD = "TNPadmin123"  # NEED TO CHANGE IT TO ENCRYPTED PASSWORD

# TABLE NAMES
COLLEGE_TABLE = "College"
COLLEGE_COMPANY_TABLE = "College_Company"
COLLEGE_DEPARTMENTS_TABLE = "CollegeDepartments"
COMPANY_TABLE = "Company"
COLLEGE_CATEGORY_TABLE = "CompanyCategory"
COLLEGE_POC_TABLE = "CompanyPOC"
FACULTY_TABLE = "Faculty"
ROLES_TABLE = "Roles"
STUDENT_TABLE = "StudentDetails"
STUDENT_EXTENDED_TABLE = "StudentDetailsExtended"

TABLE_NAME_LIST = [COLLEGE_TABLE, COLLEGE_COMPANY_TABLE, COLLEGE_DEPARTMENTS_TABLE, COMPANY_TABLE,
                   COLLEGE_CATEGORY_TABLE, COLLEGE_POC_TABLE, FACULTY_TABLE, ROLES_TABLE,
                   STUDENT_TABLE, STUDENT_EXTENDED_TABLE]

# MY-SQL PROPERTIES
HOST_NAME = "127.0.0.1"
PORT_NAME = "3306"

SQL_CREATE_FILE_NAMES = ['DataBaseCreation.sql', 'CompanyCategoryTable.sql', 'Company.sql', 'College.sql',
                         'CollegeDepartments.sql', 'Roles.sql', 'Faculty.sql', 'CompanyPOC.sql', 'CollegeCompany.sql',
                         'StudentTable.sql', 'StudentExtendedTable.sql']
SQL_DELETE_FILE_NAMES = ['DeleteTable.sql']
# SQL_FILE_NAMES = ['CompanyCategoryTable.sql']
SQL_FILE_PREFIX = "/Utils/DBUtils/SQLs/"
