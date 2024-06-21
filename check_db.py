import mysql.connector
from mysql.connector import Error


# Function to connect to MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="job_portal",
            user="root",
            password="$Mysql7676",
        )

        if connection.is_connected():
            print("Connected to MySQL database")

        return connection

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# Function to insert data into 'jobs' table
def insert_job(cursor, title, company, location, description, posted_date):
    try:
        insert_query = "INSERT INTO jobs (title, company, location, description, posted_date) VALUES (%s, %s, %s, %s, %s)"
        job_data = (title, company, location, description, posted_date)

        cursor.execute(insert_query, job_data)
        print("Job inserted successfully")

    except Error as e:
        print(f"Error inserting job: {e}")


# Function to insert data into 'candidates' table
def insert_candidate(cursor, full_name, email, phone, cv_file, applied_date):
    try:
        insert_query = "INSERT INTO candidates (full_name, email, phone, cv_file, applied_date) VALUES (%s, %s, %s, %s, %s)"
        candidate_data = (full_name, email, phone, cv_file, applied_date)

        cursor.execute(insert_query, candidate_data)
        print("Candidate inserted successfully")

    except Error as e:
        print(f"Error inserting candidate: {e}")


# Function to insert data into 'applications' table
def insert_application(cursor, job_id, candidate_id, application_date):
    try:
        insert_query = "INSERT INTO applications (job_id, candidate_id, application_date) VALUES (%s, %s, %s)"
        application_data = (job_id, candidate_id, application_date)

        cursor.execute(insert_query, application_data)
        print("Application inserted successfully")

    except Error as e:
        print(f"Error inserting application: {e}")


# Main function to execute the script
def main():
    # Connect to MySQL
    connection = connect_to_mysql()
    if not connection:
        return

    try:
        # Create cursor object to execute queries
        cursor = connection.cursor()

        # Example data for jobs, candidates, and applications
        job_data = (
            "hackathon_job",
            "Example ",
            "Ingolstadt",
            "Looking for a skilled software engineer...",
            "2024-06-21",
        )
        candidate_data = (
            "Shree",
            "john.doe@example.com",
            "123-456-7890",
            "john_doe_cv.pdf",
            "2024-06-21",
        )
        application_data = (
            4,
            1,
            "2025-06-21",
        )  # Assuming job_id and candidate_id exist

        # Insert data into tables
        insert_job(cursor, *job_data)
        insert_candidate(cursor, *candidate_data)
        insert_application(cursor, *application_data)

        # Commit changes and close cursor
        connection.commit()

    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

    finally:
        # Close cursor and connection
        if "connection" in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    main()
