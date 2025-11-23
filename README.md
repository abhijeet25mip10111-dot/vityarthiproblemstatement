# vityarthiproblemstatement
ATTENDANCE TRACKER
# 📝Attendance Tracker Flask App

# 📋Overview of the project

This is a simple web application built with Python and Flask designed to track student attendance. It provides an easy interface to input attendance data and automatically calculates the number of days absent and the attendance percentage based on a fixed academic schedule. The application stores all records in a local SQLite database for persistent storage and allows users to view a summary of all entered data.

# ✨Features

Add Attendance Records: Simple form to input a student's name and the number of days they were present.

Automatic Calculation: The system automatically calculates the number of days absent and the attendance percentage based on a fixed total of 15 working days.

Database Integration: Utilizes SQLAlchemy to store student records securely in an attend.db SQLite database.

Summary Dashboard: dedicated summary page that retrieves and displays a table of all students and their attendance statistics.

Responsive Design: Basic HTML/CSS interface for easy navigation.

# 🛠️Technologies/tools used

Programming Language: Python 3

Web Framework: Flask

Database ORM: Flask-SQLAlchemy

Database: SQLite

Frontend: HTML5, CSS3

Version Control: Git

# 🚀Steps to install & run the project

1. Clone the Repository
Download the project files to your local machine:

git clone [https://github.com/yourusername/attendance-tracker.git](https://github.com/abhijeet25mip10111-dot/vityarthiproblemstatement.git)
cd attendance-tracker


2. Create a Virtual Environment (Optional but Recommended)
Isolate your project dependencies:

Windows:

python -m venv venv
.\venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies
Install the required Python libraries (Flask and Flask-SQLAlchemy):

pip install flask flask-sqlalchemy


4. Run the Application
Start the local development server:

python app.py


You should see a message indicating the server is running, typically at http://127.0.0.1:5000.

# 🧪Instructions for testing

To verify the project is working correctly, follow these testing steps:

Open the Application: Open your web browser and navigate to http://127.0.0.1:5000.

Test Data Entry:

On the home page, enter a test student name (e.g., "John Doe").

Enter a number for "Days Present" (e.g., 12).

Click the Submit button.

Verify Calculation:

The app should redirect you back to the home page.

Check your database or the summary page to ensure the calculation is correct (Example: 12/15 = 80%).

Check Summary View:

Navigate to the summary URL: http://127.0.0.1:5000/summary.

Confirm that "John Doe" appears in the table with the correct present, absent (3), and percentage values.
