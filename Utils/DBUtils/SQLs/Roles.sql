
CREATE TABLE IF NOT EXISTS Roles (
RoleId int NOT NULL UNIQUE AUTO_INCREMENT,
RoleName varchar(30),
RoleGroup varchar(20),
PRIMARY KEY(RoleId)
);
