
CREATE TABLE IF NOT EXISTS StudentDetailsExtended (
studentExId int AUTO_INCREMENT,
studentExStudentId int, -- foreign key,

-- EDUCATION DETAILS START HERE
studentTenthCGPA float,
studentTwelfthCGPA float,

studentTenthPercentage float,
studentTwelfthPercentage float,

studentFirstSemCGPA float,
studentSecondSemCGPA float,
studentThirdSemCGPA float,
studentFourthSemCGPA float,
studentFifthSemCGPA float,
studentSixthSemCGPA float,
studentSeventhSemCGPA float,
studentEightthSemGCPA float,

studentAvgCGPA float,
studentAvgSGPA float,

studentisDiploma boolean,
studentDiplomaMarks float,

studentisBacklog boolean,
studentNumberOfBacklogs int,
studentActiveBacklog int,
studentPassiveBacklog int,

studentisYD boolean,
studentYDYears int,

studentisEducationGap boolean,
studentEducationGapYears int,

-- Graduation Details
studentGraduationYear date,
studentisGraduated boolean,
studentUniversityName varchar(50),

PRIMARY KEY(studentExId),
INDEX par_ind (studentExId),

CONSTRAINT fk_studentExStudentId FOREIGN KEY (studentExStudentId)  
REFERENCES StudentDetails(studentId)  
ON DELETE CASCADE
);
