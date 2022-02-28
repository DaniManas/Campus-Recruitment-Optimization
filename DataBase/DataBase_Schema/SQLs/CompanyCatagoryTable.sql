-- CREATE TABLE

CREATE TABLE IF NOT EXISTS CompanyCatagory (
CompanycategoryId int NOT NULL AUTO_INCREMENT,
CompanycategoryName varchar(30), -- possible values - Dream, Premium, Semi-Premium, Normal
PRIMARY KEY(CompanycategoryId)
);