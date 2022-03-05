
CREATE TABLE IF NOT EXISTS CompanyPOC (

CompanyPOCId int NOT NULL AUTO_INCREMENT,

-- TABLE CROSS_CONNECTION PROPERTIES
companyPOCRoleId int, -- foreign key,
companyPOCCompanyId int, -- foreign key
companyPOCCollegeId int, -- foreign key

-- COMPANY POC DETAILS
companyPOCFirstName varchar(100),
companyPOCLastName varchar(100),
companyPOCEmail nvarchar(320) not null unique,
companyPOCMobileNumber varchar(100) not null unique,
companyPOCDesignation varchar(30),
companyPOCEmailVerified boolean,
companyPOCMobileNumberVerified boolean,


-- LOGIN DETAILS START HERE
username varchar(50),
password varchar(300),
companyPOClastLoggedInTimeStamp TimeStamp,
companyPOClastLoggedOutTimeStamp TimeStamp,
companyPOClastModifiedPassword TimeStamp,
companyPOCentityIdentifier varchar(1), -- possible values C-Company

PRIMARY KEY(CompanyPOCId),
INDEX par_ind (CompanyPOCId),  

CONSTRAINT fk_companyPOCCompanyId FOREIGN KEY (companyPOCCompanyId)  
REFERENCES company(companyId)  
ON DELETE SET NULL,

CONSTRAINT fk_companyPOCCollegeId FOREIGN KEY (companyPOCCollegeId)  
REFERENCES college(collegeId)  
ON DELETE SET NULL ,

CONSTRAINT fk_companyPOCRoleId FOREIGN KEY (companyPOCRoleId)  
REFERENCES roles(RoleId)  
ON DELETE SET NULL 
);