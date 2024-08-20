# Purpose to create the 3 csv files required to add a new user to Canvas
# 001_CreateUser.csv
# 002_CreateSandbox.csv
# 003_CreateEnrolment.csv
# These files are processed using SIS Import to create the user account, create the users sandbox, and enroll the user in the sandbox
# 30 July 2024

import csv
import os
import webbrowser

def open_webpage(url):
    try:
        # Open the URL in the default web browser
        webbrowser.open(url)
        print(f"Webpage opened: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")



def check_file_open(file_path):
    try:
        # Try to open the file in append mode to check if it's open elsewhere
        with open(file_path, mode='a', newline='', encoding='utf-8'):
            pass
    except PermissionError:
        return True
    return False

def create_csv_with_header(file_path, fieldnames):
    # Create a new CSV file with headers if it does not exist
    if not os.path.isfile(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
def delete_file_if_exists(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Attempt to remove the file
            os.remove(file_path)
        else:
            print(f"File '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied: The file '{file_path}' may be open or in use.")
    except Exception as e:
        print(f"Error occurred while deleting file '{file_path}': {e}")
        

def get_user_details():
    while True:
        user_id = input("Enter User ID: ").strip()
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        email = input("Enter Email Address: ").strip()

        # Validate the input
        if not user_id or not first_name or not last_name or not email:
            print("All fields are required. Please enter the details again.")
        else:
            return user_id, first_name, last_name, email

def display_and_confirm(user_id, first_name, last_name, email):
    print("Please confirm the entered details:")
    print(f"User ID: {user_id}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")
    confirm = input("Is the information correct? (Yes/y or No/n): ").strip().lower()
    return confirm in ('yes', 'y')

   
 
def create_sandbox_csv(user_id, first_name, last_name):
    course_id = f"{user_id.lower()}_sb"
    short_name = f"{first_name}'s Sandbox"
    long_name = f"{first_name} {last_name}'s Sandbox"
    account_id = "ACU_Staff_Sandboxes"
    status = "active"

    csv_file_path = os.path.join(os.getcwd(), '002_CreateSandbox.csv')
    fieldnames = ['course_id', 'short_name', 'long_name', 'account_id', 'status']

    create_csv_with_header(csv_file_path, fieldnames)

    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'course_id': course_id,
            'short_name': short_name,
            'long_name': long_name,
            'account_id': account_id,
            'status': status
        })

    print(f"\nSandbox details saved to {csv_file_path}")

def create_user_csv(user_id, first_name, last_name, email):
    login_id = user_id
    status = "Active"

    csv_file_path = os.path.join(os.getcwd(), '001_CreateUser.csv')
    fieldnames = ['user_id', 'login_id', 'first_name', 'last_name', 'email', 'status']

    create_csv_with_header(csv_file_path, fieldnames)

    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'user_id': user_id,
            'login_id': login_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'status': status
        })

    print(f"\nUser details saved to {csv_file_path}")

def create_enrolment_csv(user_id):
    course_id = f"{user_id.lower()}_sb"
    role = "Editing Lecturer"
    status = "Active"

    csv_file_path = os.path.join(os.getcwd(), '003_CreateEnrolment.csv')
    fieldnames = ['course_id', 'user_id', 'role', 'status']

    create_csv_with_header(csv_file_path, fieldnames)

    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'course_id': course_id,
            'user_id': user_id,
            'role': role,
            'status': status
        })
    print(f"https://canvas.acu.edu.au/courses/{course_id}")
    # print(f"\nEnrolment details saved to {csv_file_path}")

# Log activity
def create_log_csv(user_id):
    course_id = f"{user_id.lower()}_sb"
    role = "Editing Lecturer"
    status = "Active"

    csv_file_path = os.path.join(os.getcwd(), 'Enrolment_Log.csv')
    fieldnames = ['course_id', 'user_id', 'role', 'status']

    create_csv_with_header(csv_file_path, fieldnames)

    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'course_id': course_id,
            'user_id': user_id,
            'role': role,
            'status': status
        })

def main():
    csv_user_path = os.path.join(os.getcwd(), '001_CreateUser.csv')
    csv_sandbox_path = os.path.join(os.getcwd(), '002_CreateSandbox.csv')
    csv_enrolment_path = os.path.join(os.getcwd(), '003_CreateEnrolment.csv')
    csv_log_path = os.path.join(os.getcwd(), 'Enrolment_Log.csv')

    # Check if any of the CSV files are open before proceeding
    if check_file_open(csv_sandbox_path) or check_file_open(csv_user_path) or check_file_open(csv_enrolment_path) or check_file_open(csv_log_path) :
        print(f"\r\n *** One or more CSV file is open! ***\r\n *** Exiting the Python Script.    ***\r\n")
        return  # Abort the script
        
    # Clean out any existing data in the csv files.
    delete_file_if_exists(csv_user_path)
    delete_file_if_exists(csv_user_path)
    delete_file_if_exists(csv_sandbox_path)
    delete_file_if_exists(csv_enrolment_path)

    while True:
        while True:
            user_id, first_name, last_name, email = get_user_details()
            
            if display_and_confirm(user_id, first_name, last_name, email):
                create_sandbox_csv(user_id, first_name, last_name)
                create_user_csv(user_id, first_name, last_name, email)
                create_enrolment_csv(user_id)
                create_log_csv(user_id)
                
                print("Details confirmed and saved.")
                break  # Exit the inner loop to proceed with adding another user
            else:
                print("Details not confirmed. The data has been discarded. Please re-enter your details.")

        # Ask if the user wants to add another user
        another_user = input("Do you want to add another user? (Yes/y or No/n): ").strip().lower()
        if another_user not in ('yes', 'y'):
            break  # Exit the loop and end the script

    # print(f"User details saved to {csv_user_path}")
    # print(f"Sandbox details saved to {csv_sandbox_path}")
    # print(f"Enrolment details saved to {csv_enrolment_path}")
    
    # Example usage:
    open_webpage("https://canvas.acu.edu.au/accounts/1/sis_import")


    open_webpage(f"https://canvas.acu.edu.au/accounts/1?search_term={user_id}")
    
if __name__ == "__main__":
    main()
