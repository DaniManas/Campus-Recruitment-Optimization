CREATE TABLE IF NOT EXISTS CollegeCompany (
CCId int AUTO_INCREMENT PRIMARY KEY,

CCCompanyVisitYear datetime,
CCCompanySalaryOffered float,
CCCompanyJD varchar(50), -- will be a path to file to a static folder
CCCompanyRoleNameOffered varchar(50),
CCJobLocationOffered varchar(30),

-- TME STUDENT DETAILS
CCCollegeId int, -- foreign key,
CCCompanyId int, -- foreign key,

-- PROFILE RELATED TIMESTAMPS
CCProfileCreateTimestamp TimeStamp,
CCProfileUpdateTimestamp TimeStamp,

INDEX par_ind (CCId),  
CONSTRAINT fk_CCCompanyId FOREIGN KEY (CCCompanyId)  
REFERENCES company(companyId)  
ON DELETE SET NULL,

CONSTRAINT fk_CCCollegeId FOREIGN KEY (CCCollegeId)  
REFERENCES college(collegeId)  
ON DELETE SET NULL
);