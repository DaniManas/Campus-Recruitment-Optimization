-- CREATE TABLE

CREATE TABLE IF NOT EXISTS StudentDetails (

-- GENETAL INFORMATION
studentId int NOT NULL UNIQUE AUTO_INCREMENT,
studentRegistrationId varchar(11) not null unique,
studentRollNumber int not null unique,
studentGender varchar(1),
studentNationality varchar(20),
studentRoleId int, -- foreign key,

-- PII DATA STARTS HERE
studentFirstName varchar(100),
studentFathersName varchar(300),
studentMothersName varchar(300),
studentLastName varchar(100),
studentEmail nvarchar(320) not null unique,
studentMobileNumber varchar(100) not null unique,
studentAadhar varchar(100) not null unique,
studentPAN	varchar(100) unique,
studentPassport varchar(100) unique,
studentPermanantAddress varchar(500),
studentResidentialAddress varchar(500),


-- FLAGS FOR PII START HERE
studentisAadhar boolean,
studentisPAN boolean,
studentisPassport boolean,
studentisIndian boolean,
isEmailVerified boolean,
isMobileNumberVerified boolean,


-- COLLEGE DETAILS START HERE
studentCollegeId int, -- foreign key,
studentDepartmentId int, -- foreign key,


-- COMPANY PLACEMENT DETAILS START HERE
studentCompanyId int, -- foreign key,
isPlaced boolean,
placementTime TimeStamp,
placementSalary float,


-- LOGIN DETAILS START HERE
username varchar(50),
password varchar(300),
lastLoggedInTimeStamp TimeStamp,
lastLoggedOutTimeStamp TimeStamp,
lastModifiedPassword TimeStamp,

-- DOCUMENT RELATED STATS
studentisDocumentVerified boolean,
studentDocumentUpdateTimestamp TimeStamp,
studentDocumentCreateTimestamp TimeStamp,

-- PROFILE CREATION TIMESTAMP DETAILS
studentProfileCreationTimestamp TimeStamp,
studentProfileUpdateTimestamp TimeStamp,

-- PROFILE DELETION FLAGS
studentDeleteProfileFlag boolean,
entityIdentifier varchar(1), -- possible values S-Student

-- Student Socials TABLE
studentLinkedInUsername varchar(30),
studentHackerRankUsername varchar(30),
studentCodeChefUsername varchar(30),
studentResume varchar(50),

PRIMARY KEY(studentId),
INDEX par_ind (studentId), 

CONSTRAINT fk_studentDepartmentId FOREIGN KEY (studentDepartmentId)  
REFERENCES collegedepartments(collegeDepartmentsId)  
ON DELETE SET NULL,
 
CONSTRAINT fk_studentCompanyId FOREIGN KEY (studentCompanyId)  
REFERENCES company(companyId)  
ON DELETE SET NULL,

CONSTRAINT fk_studentCollegeId FOREIGN KEY (studentCollegeId)  
REFERENCES college(collegeId)  
ON DELETE SET NULL ,

CONSTRAINT fk_studentRoleId FOREIGN KEY (studentRoleId)  
REFERENCES roles(RoleId)  
ON DELETE SET NULL 
);
