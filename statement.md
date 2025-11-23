# 📝 Project Statement

# 1. 🚩 Problem Statement

In many educational settings, tracking attendance manually is tedious, prone to human error, and lacks immediate feedback. Students often struggle to keep track of their cumulative attendance percentage, leading to last-minute panic regarding exam eligibility or credit requirements. Existing solutions are often too complex or require heavy administrative access, leaving a gap for a simple, personal, or classroom-level tracking tool.

# 2. 🎯 Scope of the project

The scope of this project is to develop a lightweight, web-based application that digitizes the attendance tracking process. The project focuses on:

🖥️ User Interface: Creating a user-friendly interface for inputting student attendance data.

🧮 Automation: Automating the calculation of critical metrics such as "Days Absent" and "Attendance Percentage."

💾 Storage: Implementing a persistent storage system using a local SQLite database to ensure data is not lost between sessions.

📊 Visualization: Providing a summary dashboard to view records for multiple students simultaneously.

⚠️ Current Constraint: The initial version operates on a fixed academic schedule (15 working days) for demonstration purposes, with potential for future scalability.

# 3. 👥 Target users

The application is designed for:

🎓 Students: To track their own attendance and ensure they are meeting required percentage thresholds.

📢 Class Representatives: To maintain a digital log of attendance for their specific batch or section.

👩‍🏫 Teachers/Faculty: For a quick, offline-capable method to calculate and store attendance percentages for small groups without navigating complex institutional portals.

# 4. ⭐ High-level features

⚡ Automated Calculation: Instantly computes the number of days absent and the final attendance percentage based on user input, eliminating manual math errors.

🗄️ Persistent Database Storage: Utilizes SQLAlchemy and SQLite to securely save student records, allowing users to close the app and return to their data later.

✍️ Data Entry Interface: A clean, minimal HTML form that allows for quick addition of new student records.

📋 Summary Dashboard: A dedicated view that retrieves all stored records and presents them in a structured table format for easy comparison and review.
