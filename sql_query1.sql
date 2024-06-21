-- CREATE DATABASE job_from_adzuna;
USE job_from_adzuna;

-- Table to store job postings
CREATE TABLE job_postings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    companyName VARCHAR(255) NOT NULL,
    salaryInsights TEXT,
    applicants INT,
    formattedLocation VARCHAR(255),
    country VARCHAR(2),
    formattedEmploymentStatus VARCHAR(50),
    formattedExperienceLevel VARCHAR(50),
    formattedIndustries TEXT,
    jobDescription TEXT,
    inferredBenefits TEXT,
    jobFunctions VARCHAR(255),
    companyApplyUrl VARCHAR(255),
    easyApplyUrl VARCHAR(255),
    jobPostingUrl VARCHAR(255),
    listedAt VARCHAR(50)
);

select * from job_postings;