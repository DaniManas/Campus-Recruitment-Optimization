CREATE TABLE IF NOT EXISTS Company (

-- GENERAL INFORMATION
companyId int AUTO_INCREMENT,
companyName varchar(30),
companyLocation varchar(20),


-- Company category Ideantifier
companyCompanyCategoryId int,
PRIMARY KEY(companyId),

INDEX par_ind (companyId),  
CONSTRAINT fk_companyCategoryId FOREIGN KEY (companyCompanyCategoryId)  
REFERENCES companycatagory(CompanycategoryId)  
ON DELETE SET NULL 
);
