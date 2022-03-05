CREATE TABLE IF NOT EXISTS CollegeDepartments (
collegeDepartmentsId int NOT NULL UNIQUE AUTO_INCREMENT,
collegeDepartmentsName varchar(30), -- possible values - ECE, CSE, IT, etc
PRIMARY KEY(collegeDepartmentsId)
);
