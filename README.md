# Job Application Tracker

## Overview

The Job Application Tracker is a powerful Python program designed to simplify and streamline your job application management process. Whether you're actively job hunting or want to maintain an organized record of your job search efforts, this tool is here to help you effortlessly record, update, and analyze your job applications and their response statuses.

## Features

### 1. Add an Application

- Effortlessly record the details of a new job application, including:
  - **Job Code**: A unique identifier for each application.
  - **Job Title**: The title of the job you're applying for.
  - **Company**: The name of the company or organization.
  - **Application Date**: The date when you submitted your application.
- Default response statuses are provided as "Applications" and "No Response."

### 2. Update an Application

- Seamlessly modify the response status of an existing job application.
- Change response statuses to reflect interview invitations, rejections, or any other relevant updates.

### 3. See All Applications

- Gain comprehensive insights with a detailed list of all your job applications.
- Access vital information such as job code, job title, company, application date, and the latest response status received.

### 4. Print Response Pairs

- Generate formatted response pairs, ideal for visualization using tools like SankeyMATIC ([SankeyMATIC](https://sankeymatic.com)).
- Simplify the tracking and analysis of application responses.

### 5. Remove an Application

- Effortlessly remove a job application from your list by specifying its job code.

### 6. Search for an Application

- Quickly locate specific job applications based on various criteria, including job code, job title, company, or application date.

### 7. Exit

- Gracefully exit the program when you're done managing your job applications.

## Getting Started

1. **Prerequisites**: Ensure that you have Python installed on your system.

2. **Installation**:

   - Clone this repository or download the `job_application_tracker.py` file.

3. **Usage**:

   - Run the `job_application_tracker.py` file.
   - Choose from the available menu options (1 to 7) by entering the corresponding number.
   - Follow the on-screen prompts to add, update, view, or print job applications, remove applications, search, or exit.

## Dependencies

This application relies on the following Python modules:

- `json`: For efficient JSON file handling.
- `os`: For handling operating system-related tasks.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed information.

## Data Storage

All job application data is stored in a JSON file named "job_applications.json."

## Enjoy Your Job Application Tracking

Simplify your job search and keep your applications organized with the Job Application Tracker. Whether you're actively job hunting or simply want to stay organized, this tool can help you manage your applications and monitor your progress effectively.
