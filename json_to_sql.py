import json

import mysql.connector
from mysql.connector import Error

# MySQL connection configuration
hostname = "localhost"
username = "root"
password = "$Mysql7676"  # Replace with your MySQL root password
database = "job_from_adzuna"


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


# Function to read JSON file and insert data into MySQL
def insert_from_json_to_mysql():
    try:
        # Read JSON file

        with open("company_jobs.json", "r") as file:
            data = json.load(file)
            job_data = data["response"]["data"]["jobs"]

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
                job["title"],
                job["companyName"],
                job["salaryInsights"],
                job["applicants"],
                job["formattedLocation"],
                job["country"],
                job["formattedEmploymentStatus"],
                job["formattedExperienceLevel"],
                job["formattedIndustries"],
                job["jobDescription"],
                job["inferredBenefits"],
                job["jobFunctions"],
                job["companyApplyUrl"],
                job["easyApplyUrl"],
                job["jobPostingUrl"],
                job["listedAt"],
            )
            cursor.execute(sql, values)
            connection.commit()

        print("Data inserted successfully into MySQL")
        cursor.close()

    except Error as e:
        print(f"Error inserting data into MySQL: {e}")

    finally:
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


# Main function to execute the script
def main():
    insert_from_json_to_mysql()


if __name__ == "__main__":
    main()
