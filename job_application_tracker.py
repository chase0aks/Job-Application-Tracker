import json
import os


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
      'Application Date': 'Application Date',
  }
  # Collect user input for each job data field
  new_application = {
      key: input(f"Enter {value}: ")
      for key, value in job_data.items()
  }
  new_application['Response Status'] = ["Applications", "No Response"]
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
      'Application Date': 'Application Date',
  }
  # Collect user input for each job data field
  new_application = {
      key: input(f"Enter {value}: ")
      for key, value in job_data.items()
  }
  new_application['Response Status'] = ["Applications", "No Response"]
  job_applications.append(new_application)
  save_job_applications(job_applications)
  print("Application added successfully!")


# Function to update the response status of a job application by Job Code
def update_application(job_code, new_response_status, job_applications):
  for application in job_applications:
    if application['Job Code'] == job_code:
      response_statuses = application.setdefault('Response Status', [])
      if response_statuses and response_statuses[-1] == 'No Response':
        response_statuses[-1] = new_response_status
      else:
        response_statuses.append(new_response_status)
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
      print(f"{key}: {value}")
    print()


# Function to print response status pairs
def print_response_pairs(job_applications):
  if not job_applications:
    print("No job applications found.")
    return

  print("\nResponse Status Pairs:")
  response_counts = {}

  for application in job_applications:
    response_statuses = application.get('Response Status', [])
    if response_statuses:
      for i in range(len(response_statuses) - 1):
        pair = f"{response_statuses[i]} [{response_statuses[i + 1]}]"
        response_counts[pair] = response_counts.get(pair, 0) + 1

  for pair, count in response_counts.items():
    response1, response2 = pair.split('[')
    response2 = response2.rstrip(']')
    print(f"{response1} [{count}] {response2}")


# Function to search for job applications based on a category and value
def search_application(category, value, job_applications):
  found_applications = []
  if category == 1:  # Search by Job Code
    key = 'Job Code'
  elif category == 2:  # Search by Job Title
    key = 'Job Title'
  elif category == 3:  # Search by Company
    key = 'Company'
  elif category == 4:  # Search by Application Date
    key = 'Application Date'
  else:
    return found_applications  # Invalid category

  found_applications = [
      app for app in job_applications if key in app and app[key] == value
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
            "Search by category:\n1. Job Code\n2. Job Title\n3. Company\n4. Application Date\nEnter your choice: "
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
