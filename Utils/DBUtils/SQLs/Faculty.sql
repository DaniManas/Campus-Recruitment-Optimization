-- CREATE TABLE

CREATE TABLE IF NOT EXISTS Faculty (

facultyId int NOT NULL UNIQUE AUTO_INCREMENT,
facultyRegId varchar(10),
facultyFirstName varchar(100),
facultyLastName varchar(100),
facultyEmail nvarchar(320) not null unique,
facultyMobileNumber varchar(100) not null unique,

facultyCollegeId int, -- foreign key,
facultyDepartmentId int, -- foreign key,
facultyRoleId  int, -- foreign key,

facultyisEmailVerified boolean,
facultyisMobileNumberVerified boolean,


-- LOGIN DETAILS START HERE
username varchar(50),
password varchar(300),
lastLoggedInTimeStamp TimeStamp,
lastLoggedOutTimeStamp TimeStamp,
lastModifiedPassword TimeStamp,
entityIdentifier varchar(1), -- possible values F-faculty

PRIMARY KEY(facultyId),

INDEX par_ind (facultyId),  
CONSTRAINT fk_facultyDepartmentId FOREIGN KEY (facultyDepartmentId)  
REFERENCES collegedepartments(collegeDepartmentsId)  
ON DELETE SET NULL,
  
CONSTRAINT fk_facultyCollegeId FOREIGN KEY (facultyCollegeId)  
REFERENCES college(collegeId)  
ON DELETE SET NULL ,

CONSTRAINT fk_facultyRoleId FOREIGN KEY (facultyRoleId)  
REFERENCES roles(RoleId)  
ON DELETE SET NULL 

);