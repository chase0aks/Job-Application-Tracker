import json

# Initialize a list to store job application data
job_applications = []

# Load data from the JSON file (if it exists)
try:
  with open('job_applications.json', 'r') as json_file:
    job_applications = json.load(json_file)
except FileNotFoundError:
  # If the JSON file doesn't exist, start with an empty list
  job_applications = []


# Function to save job applications data to a JSON file
def save_job_applications():
  with open('job_applications.json', 'w') as file:
    json.dump(job_applications, file)


# Function to add a new application
def add_application(job_code, job_title, company, app_date):
  new_application = {
      'Job Code': job_code,
      'Job Title': job_title,
      'Company': company,
      'Application Date': app_date,
      'Response Status': ["Applications",
                          "No Response"]  # Default response statuses
  }

  job_applications.append(new_application)

  # Save the updated data to the JSON file
  save_job_applications()

  print("Application added successfully!")


# Function to update an existing application
def update_application(job_code, new_response_status):
  for application in job_applications:
    if application['Job Code'] == job_code:
      response_statuses = application.get('Response Status', [])

      if response_statuses and response_statuses[-1] == 'No Response':
        response_statuses[-1] = new_response_status
      else:
        response_statuses.append(new_response_status)

      # Save the updated data to the JSON file
      save_job_applications()

      print("Application updated successfully!")
      return

  print("Job not found!")


# Function to print all applications with their last response status
def print_all_applications():
  for application in job_applications:
    job_code = application.get('Job Code', '')
    job_title = application.get('Job Title', '')
    company = application.get('Company', '')
    app_date = application.get('Application Date', '')
    response_statuses = application.get('Response Status', [])

    # Get the last response status (if any)
    last_response = response_statuses[-1] if response_statuses else ''

    print(f"Job Code: {job_code}")
    print(f"Job Title: {job_title}")
    print(f"Company: {company}")
    print(f"Application Date: {app_date}")
    print(f"Last Response Status: {last_response}")
    print()


# Function to print response pairs
def print_response_pairs():
  print("\n")
  response_counts = {}  # Dictionary to store response status counts

  # Iterate through applications and their response statuses
  for application in job_applications:
    response_statuses = application.get('Response Status', [])
    if response_statuses:
      for i in range(len(response_statuses) - 1):
        pair = f"{response_statuses[i]} [{response_statuses[i + 1]}]"
        response_counts[pair] = response_counts.get(pair, 0) + 1

  # Display the response pairs and their counts in the middle
  for pair, count in response_counts.items():
    response1, response2 = pair.split('[')
    response2 = response2.rstrip(']')
    print(f"{response1} [{count}] {response2}")


# Main menu loop
while True:
  print("\nMenu:")
  print("1. Add an application")
  print("2. Update an application")
  print("3. See all applications")
  print("4. Print response pairs")
  print("5. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    job_code = input("Enter Job Code: ")
    job_title = input("Enter Job Title: ")
    company = input("Enter Company: ")
    app_date = input("Enter Application Date: ")
    add_application(job_code, job_title, company, app_date)
  elif choice == '2':
    job_code = input("Enter Job Code to update: ")
    new_response = input("Enter new response: ")
    update_application(job_code, new_response)
  elif choice == '3':
    print_all_applications()
  elif choice == '4':
    print_response_pairs()
  elif choice == '5':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
