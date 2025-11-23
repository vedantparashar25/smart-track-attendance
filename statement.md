Project Statement: Smart Track Attendance System 

1. Problem Definition

In many educational institutions and small coaching centers, attendance is still marked manually using paper registers. This traditional method presents several challenges:
Data Loss: Physical registers can be lost or damaged.
Calculation Errors: Manually calculating attendance percentages for every student is time-consuming and prone to human error.
Lack of Insights: It is difficult to instantly identify students with low attendance (e.g., below 75%) without manual auditing.
Redundancy: Teachers often have to re-write student names for every new month or session.

2. Proposed Solution

Smart Track (CLI Version) is a Python-based desktop application designed to digitize and automate the attendance process. It serves as a lightweight, offline tool that allows instructors to manage student records and track daily attendance efficiently without needing complex database servers.

3. Key Objectives

Digital Record Keeping: To replace paper registers with a persistent digital storage system using JSON.
Automation: To automatically calculate total sessions, days present, and attendance percentages.
Validation: To ensure data integrity by preventing duplicate Roll Numbers and handling invalid inputs.
Instant Reporting: To provide a "Low Attendance" warning immediately for students falling below the required threshold (75%).

4. Technical Scope

The project is built using Core Python and adheres to the following technical specifications:
Language: Python 3.x
Data Storage: JSON (JavaScript Object Notation) for lightweight, human-readable, and portable data persistence.
Interface: Command Line Interface (CLI) for fast, keyboard-driven interaction.
Modules Used:
`json`: For data serialization and storage.
`os`: For file system checks (verifying database existence).
`datetime`: For automatic date stamping.

5. Functional Requirements

The system fulfills the following user needs:
Student Registration: Ability to add students with unique identifiers (Roll No).
Daily Tracking: Ability to mark students as Present/Absent for specific dates.
Data Persistence: The system must remember data after the application is closed.
Analytics: The system must generate a tabular report showing the current status of all students.

6. Future Enhancements

While the current version is a functional CLI tool, future iterations may include:
GUI Implementation: Adding a graphical interface using `Tkinter` or `PyQt`.
Export Feature: Ability to export reports to CSV or Excel formats.
Authentication: Adding a login system for teachers to secure the data.