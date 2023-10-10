import json
import os
from datetime import datetime
from collections import defaultdict


# Function to get the current date in the desired format
def get_date():
  return datetime.now().strftime("%m/%d/%Y")


# Function to load job applications from a JSON file
def load_job_applications():
  try:
    with open('job_applications.json', 'r') as json_file:
      job_applications = json.load(json_file)
  except (json.JSONDecodeError, FileNotFoundError):
    job_applications = []

  if not job_applications:
    print("Welcome to the Job Application Tracker!")
    print("No job applications found. Let's add your first job application.")
    add_initial_job(job_applications)
    save_job_applications(job_applications)

  return job_applications


# Function to add an initial job application
def add_initial_job(job_applications):
  job_data = {
      'Job Code': 'Job Code',
      'Job Title': 'Job Title',
      'Company': 'Company',
  }
  # Collect user input for each job data field
  new_application = {
      key: input(f"Enter {value}: ")
      for key, value in job_data.items()
  }
  tmp = get_date()
  new_application['Response Status'] = [{
      "Response": "Applied",
      "Date": tmp
  }, {
      "Response": "No Response",
      "Date": tmp
  }]
  job_applications.append(new_application)


# Function to save job applications to a JSON file
def save_job_applications(job_applications):
  with open('job_applications.json', 'w') as file:
    json.dump(job_applications, file)


# Function to remove a job application by Job Code
def remove_application(job_code, job_applications):
  job_applications = [
      application for application in job_applications
      if application['Job Code'] != job_code
  ]
  save_job_applications(job_applications)
  if not job_applications:
    print(f"No job applications found with Job Code {job_code}.")
  else:
    print(f"Application with Job Code {job_code} has been removed.")


# Function to add a new job application
def add_application(job_applications):
  job_data = {
      'Job Code': 'Job Code',
      'Job Title': 'Job Title',
      'Company': 'Company',
  }

  # Prompt the user for the job code
  job_code = input("Enter Job Code: ")

  # Check if the job code already exists in the list
  if any(app['Job Code'] == job_code for app in job_applications):
    print("Job Code already exists. Please enter a unique Job Code.")
    return  # Exit the function without adding the application

  # Collect user input for the remaining job data fields
  new_application = {'Job Code': job_code}
  for key, value in job_data.items():
    if key != 'Job Code':
      new_application[key] = input(f"Enter {value}: ")

  tmp = get_date()
  new_application['Response Status'] = [{
      "Response": "Applied",
      "Date": tmp
  }, {
      "Response": "No Response",
      "Date": tmp
  }]
  job_applications.append(new_application)
  save_job_applications(job_applications)
  print("Application added successfully!")


# Function to update the response status of a job application by Job Code
def update_application(job_code, new_response_status, job_applications):
  tmp = get_date()
  for application in job_applications:
    if application['Job Code'] == job_code:
      response_statuses = application['Response Status']

      # Check if the new response status is already in the list
      if any(status['Response'] == new_response_status
             for status in response_statuses):
        print("The same response status already exists in this application.")
        return  # Exit the function without making the update

      response_statuses.append({"Response": new_response_status, "Date": tmp})
      save_job_applications(job_applications)
      print("Application updated successfully!")
      return
  print(f"No job application found with Job Code {job_code}.")


# Function to print all job applications
def print_all_applications(job_applications):
  if not job_applications:
    print("No job applications found.")
    return

  print("\nAll Job Applications:")
  for i, application in enumerate(job_applications, 1):
    print(f"\nApplication {i}:")
    for key, value in application.items():
      if key == 'Response Status':
        print(f"{key}:")
        for status in value:
          print(f"  - {status['Response']} ({status['Date']})")
      else:
        print(f"{key}: {value}")
    print()


# Function to print response status pairs
def print_response_pairs(job_applications):
  if not job_applications:
    print("No job applications found.")
    return

  print("\nResponse Status Pairs:")
  response_counts = defaultdict(int)

  for application in job_applications:
    response_statuses = application.get('Response Status', [])
    if response_statuses:
      for i in range(len(response_statuses) - 1):
        response1 = response_statuses[i]["Response"]
        response2 = response_statuses[i + 1]["Response"]
        pair = f"{response1} [{response2}]"
        response_counts[pair] += 1

  for pair, count in response_counts.items():
    response1, response2 = pair.split(' [')
    print(f"{response1} [{count}] {response2[:-1]}")


# Function to search for job applications based on a category and value (case-insensitive)
def search_application(category, value, job_applications):
  found_applications = []
  value = value.lower(
  )  # Convert the search value to lowercase for case-insensitive comparison
  if category not in (1, 2, 3):  # Check if category is not in the range 1-3
    print("Invalid category. Please enter a valid category (1-3).")
    return found_applications  # Invalid category

  if category == 1:  # Search by Job Code
    key = 'Job Code'
  elif category == 2:  # Search by Job Title
    key = 'Job Title'
  elif category == 3:  # Search by Company
    key = 'Company'

  found_applications = [
      app for app in job_applications
      if key in app and app[key].lower() == value
  ]
  return found_applications


# Function to print search results
def print_search_results(results):
  if not results:
    print("No applications found matching the search criteria.")
    return

  print("\nSearch Results:")
  for i, application in enumerate(results, 1):
    print(f"\nResult {i}:")
    for key, value in application.items():
      if key == 'Response Status':
        print(f"{key}:")
        for status in value:
          print(f"  - Response: {status['Response']}  Date: {status['Date']}")
      else:
        print(f"{key}: {value}")
    print()


# Load job applications from file
job_applications = load_job_applications()

# Menu loop for user interaction
while True:
  print("\nMenu:")
  print("1. Add an application")
  print("2. Update an application")
  print("3. See all applications")
  print("4. Print response pairs")
  print("5. Remove an application")
  print("6. Search for an application")
  print("7. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    add_application(job_applications)
  elif choice == '2':
    job_code = input("Enter Job Code to update: ")
    new_response = input("Enter new response: ")
    update_application(job_code, new_response, job_applications)
  elif choice == '3':
    print_all_applications(job_applications)
  elif choice == '4':
    print_response_pairs(job_applications)
  elif choice == '5':
    job_code = input("Enter Job Code to remove: ")
    remove_application(job_code, job_applications)
  elif choice == '6':
    category = int(
        input(
            "Search by category:\n1. Job Code\n2. Job Title\n3. Company\nEnter your choice: "
        ))
    search_value = input("Enter the value to search for: ")
    found_applications = search_application(category, search_value,
                                            job_applications)
    print_search_results(found_applications)
  elif choice == '7':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
