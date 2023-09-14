USE internship;

DROP TABLE InternshipApplication
DROP TABLE InternshipOffer;
DROP TABLE Company;
DROP TABLE Student;
DROP TABLE Lecturer;
DROP TABLE Admin_User;

CREATE TABLE Admin_User (
	admin_id VARCHAR(50),
	admin_username VARCHAR(50),
	admin_password VARCHAR(50)
);

CREATE TABLE Lecturer (
	lecturer_id VARCHAR(50),
	lecturer_name VARCHAR(50),
	lecturer_email VARCHAR(50),
	lecturer_password VARCHAR(50),
	PRIMARY KEY (lecturer_id)
);

CREATE TABLE Student (
	student_id VARCHAR(50),
	student_name VARCHAR(50),
	student_nric VARCHAR(50),
	student_gender VARCHAR(50),
	student_programme VARCHAR(50),
	student_email VARCHAR(50),
	mobile_number VARCHAR(50),
	lecturer_id VARCHAR(50),
	PRIMARY KEY (student_id),
	FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id)
);

CREATE TABLE Company(
	company_id VARCHAR(50),
	company_name VARCHAR(50),
	company_website VARCHAR(50),
	person_in_charge VARCHAR(50),
	contact_number VARCHAR(50),
	company_email VARCHAR(50),
	company_password VARCHAR(50),
	register_status VARCHAR(50),	
	PRIMARY KEY(company_id)
);

CREATE TABLE InternshipOffer(
	offer_id VARCHAR(50),
	job_title VARCHAR(50),
	job_description VARCHAR(50),
	allowance VARCHAR(50),
	company_id VARCHAR(50),
	PRIMARY KEY(offer_id),
	FOREIGN KEY(company_id) REFERENCES Company(company_id)
);

CREATE TABLE InternshipApplication(
	student_id VARCHAR(50),
	offer_id VARCHAR(50),
	application_date VARCHAR(50),
	application_status VARCHAR(50),
	PRIMARY KEY(student_id, offer_id),
	FOREIGN KEY(student_id) REFERENCES Student(student_id),
	FOREIGN KEY(offer_id) REFERENCES InternshipOffer(offer_id)
);

/* Query for Insert Student */
INSERT INTO Student VALUES ("22WMR05680", "Loh Kang Sheng", "020110-10-1469", "Male", "RSW", "lohks-wm20@student.tarc.edu.my", "011-2719-2499", null)

INSERT INTO Lecturer VALUES("p123", "Wong Thein Lai", "p123@tarc.edu.my", "123456")