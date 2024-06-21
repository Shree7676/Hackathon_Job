import json

import mysql.connector
import requests
from mysql.connector import Error

# MySQL connection configuration
hostname = "localhost"
username = "root"
password = "$Mysql7676"  # Replace with your MySQL root password
database = "job_from_adzuna"

# API endpoint URL
api_url = "https://linkedin-data-scraper.p.rapidapi.com/company_jobs"

# RapidAPI headers
headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
    "x-rapidapi-key": "0443d83d4dmsh92e89bd423ce76fp1d2d1bjsn6c17c89f24d4",
}


# Function to connect to MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host=hostname, user=username, password=password, database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# Function to fetch data from API and insert into MySQL
def fetch_and_insert_data(company_url, count=10):
    try:
        # Data for API request
        data = {"company_url": company_url, "count": count}

        # Fetch data from API
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            job_data = response.json()["response"]["data"]

            # Connect to MySQL
            connection = connect_to_mysql()
            if not connection:
                return

            # Insert data into MySQL table
            cursor = connection.cursor()
            for job in job_data:
                sql = """
                    INSERT INTO job_postings (title, companyName, salaryInsights, applicants, formattedLocation, 
                                              country, formattedEmploymentStatus, formattedExperienceLevel, 
                                              formattedIndustries, jobDescription, inferredBenefits, jobFunctions, 
                                              companyApplyUrl, easyApplyUrl, jobPostingUrl, listedAt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    job.get("title", ""),
                    job.get("companyName", ""),
                    job.get("salaryInsights", ""),
                    job.get("applicants", None),
                    job.get("formattedLocation", ""),
                    job.get("country", ""),
                    job.get("formattedEmploymentStatus", ""),
                    job.get("formattedExperienceLevel", ""),
                    job.get("formattedIndustries", ""),
                    job.get("jobDescription", ""),
                    job.get("inferredBenefits", ""),
                    job.get("jobFunctions", ""),
                    job.get("companyApplyUrl", ""),
                    job.get("easyApplyUrl", ""),
                    job.get("jobPostingUrl", ""),
                    job.get("listedAt", ""),
                )
                cursor.execute(sql, values)
                connection.commit()

            print("Data inserted successfully")
            cursor.close()

    except Error as e:
        print(f"Error inserting data into MySQL: {e}")

    finally:
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


# Main function to execute the script
def main():
    company_url = "http://www.linkedin.com/company/google"  # Example company URL
    fetch_and_insert_data(company_url)


if __name__ == "__main__":
    main()
