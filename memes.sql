-- --------------------------------------------------------
-- Host:                         internship-system.cgj7jfy75lmm.us-east-1.rds.amazonaws.com
-- Server version:               10.6.14-MariaDB - managed by https://aws.amazon.com/rds/
-- Server OS:                    Linux
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table internship.Admin_User
CREATE TABLE IF NOT EXISTS `Admin_User` (
  `admin_id` varchar(50) DEFAULT NULL,
  `admin_username` varchar(50) DEFAULT NULL,
  `admin_password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.Admin_User: ~2 rows (approximately)
INSERT INTO `Admin_User` (`admin_id`, `admin_username`, `admin_password`) VALUES
	('admin01', 'admin1', '123456'),
	('admin2', 'John Cena', '54321');

-- Dumping structure for table internship.Company
CREATE TABLE IF NOT EXISTS `Company` (
  `company_id` varchar(50) NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `company_website` varchar(50) DEFAULT NULL,
  `person_in_charge` varchar(50) DEFAULT NULL,
  `contact_number` varchar(50) DEFAULT NULL,
  `company_email` varchar(50) DEFAULT NULL,
  `company_password` varchar(50) DEFAULT NULL,
  `register_status` varchar(50) DEFAULT NULL,
  `company_address` varchar(200) DEFAULT NULL,
  `cert_url` varchar(200) DEFAULT NULL,
  `logo_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.Company: ~5 rows (approximately)
INSERT INTO `Company` (`company_id`, `company_name`, `company_website`, `person_in_charge`, `contact_number`, `company_email`, `company_password`, `register_status`, `company_address`, `cert_url`, `logo_url`) VALUES
	('C0001', 'Sainoforce', 'www.google.com', 'Wong Jeng Liang', '018-388-7670', 'sainoforce@gmail.com', 'sainoforce123', 'approved', NULL, NULL, NULL),
	('C0002', 'Google Sdn Bhd', 'https://www.google.com', 'Colin Eng', '011-2719-2499', 'sainoforce@company.com', '123456', 'approved', NULL, NULL, NULL),
	('C0003', 'Dyodd', 'https://www.google.com', 'Jeff Bezos', '60-9081-0572', 'dydod@hotmail.com', 'cool', 'approved', NULL, NULL, NULL),
	('C0004', 'Microsoft Sdn Bhd', 'https://www.google.com', 'John Cena', '01127192499', 'abc@gmail.com', 'pdnejoh123', 'approved', NULL, NULL, NULL),
	('C0005', 'WWE Sdn Bhd', 'https://www.wwe.com/', 'John Cena', '01127192499', 'lohks6536@gmail.com', '123456', 'approved', '7B, JALAN LEGENDA 2, TAMAN LEGENDA MAS', 'https://lohkangsheng-employee.s3.amazonaws.com/companies/C0005/cert.pdf', 'https://lohkangsheng-employee.s3.amazonaws.com/companies/C0005/logo.png'),
	('C0006', 'Hashcode Studio Sdn Bhd (1331477-H)', 'https://hashcodestudio.com/', 'Mr Wong Jeng Liang', '012-987-1234', 'hello@hashcodestudio.com', '1234567', 'approved', 'D-7-8, Menara Suezcap 1, KL Gateway, No. 2, Jalan Kerinchi, 59200 Bangsar South, Kuala Lumpur.', 'https://s3.amazonaws.com/lohkangsheng-employee/companies/C0006/cert.pdf', 'https://s3.amazonaws.com/lohkangsheng-employee/companies/C0006/logo.png');

-- Dumping structure for table internship.InternshipApplication
CREATE TABLE IF NOT EXISTS `InternshipApplication` (
  `student_id` varchar(50) NOT NULL,
  `offer_id` varchar(50) NOT NULL,
  `application_date` varchar(50) DEFAULT NULL,
  `application_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`,`offer_id`),
  KEY `offer_id` (`offer_id`),
  CONSTRAINT `InternshipApplication_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`),
  CONSTRAINT `InternshipApplication_ibfk_2` FOREIGN KEY (`offer_id`) REFERENCES `InternshipOffer` (`offer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.InternshipApplication: ~7 rows (approximately)
INSERT INTO `InternshipApplication` (`student_id`, `offer_id`, `application_date`, `application_status`) VALUES
	('2205680', '1002', '2023-09-18 15:46:04', 'pending'),
	('22WMR05680', '1001', '2023-09-18 02:11:14', 'pending'),
	('22WMR05680', '1002', '2023-09-18 13:43:58', 'pending'),
	('22WMR05680', '1003', '2023-09-18 16:03:56', 'pending'),
	('22WMR05680', 'o0001', '2023-09-18 02:39:47', 'pending'),
	('22WMR05726', '1002', '2023-09-18 14:12:22', 'pending'),
	('22WMR05729', 'o0001', '2023-09-18 14:21:57', 'pending');

-- Dumping structure for table internship.InternshipOffer
CREATE TABLE IF NOT EXISTS `InternshipOffer` (
  `offer_id` varchar(50) NOT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `job_description` varchar(50) DEFAULT NULL,
  `allowance` varchar(50) DEFAULT NULL,
  `company_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`offer_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `InternshipOffer_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `Company` (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.InternshipOffer: ~4 rows (approximately)
INSERT INTO `InternshipOffer` (`offer_id`, `job_title`, `job_description`, `allowance`, `company_id`) VALUES
	('1001', 'Software Engineer Intern', 'Sleeping', 'RM1000.00 - RM1500.00', 'C0004'),
	('1002', 'Wrestler Intern', 'Fight with John Cena', 'RM5000.00 - RM10000.00', 'C0005'),
	('1003', 'Software Engineer Intern', 'Work as Software Engineer', 'RM 700.00 - RM 700.00', 'C0006'),
	('o0001', 'Engineer Intern', 'Work as An Engineer', 'RM 3000', 'C0001');

-- Dumping structure for table internship.Lecturer
CREATE TABLE IF NOT EXISTS `Lecturer` (
  `lecturer_id` varchar(50) NOT NULL,
  `lecturer_name` varchar(50) DEFAULT NULL,
  `lecturer_email` varchar(50) DEFAULT NULL,
  `lecturer_password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lecturer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.Lecturer: ~1 rows (approximately)
INSERT INTO `Lecturer` (`lecturer_id`, `lecturer_name`, `lecturer_email`, `lecturer_password`) VALUES
	('p123', 'Wong Thein Lai', 'p123@tarc.edu.my', '123456');

-- Dumping structure for table internship.ProgressionLogs
CREATE TABLE IF NOT EXISTS `ProgressionLogs` (
  `log_id` varchar(50) NOT NULL,
  `bucket_url` varchar(50) DEFAULT NULL,
  `upload_date` varchar(50) DEFAULT NULL,
  `student_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `ProgressionLogs_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.ProgressionLogs: ~0 rows (approximately)

-- Dumping structure for table internship.Student
CREATE TABLE IF NOT EXISTS `Student` (
  `student_id` varchar(50) NOT NULL,
  `student_name` varchar(50) DEFAULT NULL,
  `student_nric` varchar(50) DEFAULT NULL,
  `student_gender` varchar(50) DEFAULT NULL,
  `student_programme` varchar(50) DEFAULT NULL,
  `student_email` varchar(50) DEFAULT NULL,
  `mobile_number` varchar(50) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `resume_url` varchar(200) DEFAULT NULL,
  `lecturer_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `lecturer_id` (`lecturer_id`),
  CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturer` (`lecturer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table internship.Student: ~5 rows (approximately)
INSERT INTO `Student` (`student_id`, `student_name`, `student_nric`, `student_gender`, `student_programme`, `student_email`, `mobile_number`, `image_url`, `resume_url`, `lecturer_id`) VALUES
	('2205680', 'Loh Kang Sheng', '020110-10-1469', 'male', 'RSW', 'lohks6536@gmail.com', '011-2719-2499', 'https://s3.amazonaws.com/lohkangsheng-employee/students/2205680/profile.png', 'https://s3.amazonaws.com/lohkangsheng-employee/students/2205680/resume.pdf', 'p123'),
	('22WMR05680', 'Loh Kang Sheng', '020110-10-1469', 'Male', 'RSW', 'lohks-wm20@student.tarc.edu.my', '011-2719-2499', NULL, NULL, NULL),
	('22WMR05689', 'Loh Kang Sheng', '020110-10-1469', 'male', 'RSW', 'lohks6536@gmail.com', '011-2719-2499', NULL, NULL, 'p123'),
	('22WMR05726', 'Foo Yee Soon', '123456-10-9876', 'male', 'RIT', 'fooys-wm20@student.tarc.edu.my', '123-9863-1234', 'https://s3.amazonaws.com/lohkangsheng-employee/student/22WMR05726/profile.png', 'https://s3.amazonaws.com/lohkangsheng-employee/companies/22WMR05726/resume.pdf', 'p123'),
	('22WMR05729', 'Foo Yee Soon', '123456-10-9876', 'male', 'RIT', 'fooys-wm21@student.tarc.edu.my', '123-9863-1234', 'https://s3.amazonaws.com/lohkangsheng-employee/students/22WMR05729/profile.png', 'https://s3.amazonaws.com/lohkangsheng-employee/students/22WMR05729/resume.pdf', 'p123');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
