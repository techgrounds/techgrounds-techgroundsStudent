# Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary.
import csv
import os

# Function to collect user information
def pakUserData():
    first_name = input("Uw voornaam: ")
    last_name = input("Uw achternaam: ")
    job_title = input("Uw functie: ")
    company = input("Uw chef: ")
    return {
        "First name": first_name,
        "Last name": last_name,
        "Job title": job_title,
        "Company": company
    }

# Check if the CSV file exists
csv_file_path = "user_info.csv"
file_exists = os.path.exists(csv_file_path)

# Collect user information
user_info = pakUserData()

# Write user information to CSV file
with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
    fieldnames = user_info.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header only if the file didn't exist before
    if not file_exists:
        writer.writeheader()
    
    writer.writerow(user_info)


