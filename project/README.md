# 🔋 SmartVolt – Battery Swap Appointment Booking (Flask + MySQL)

SmartVolt is a Flask web application that allows users to **sign up / log in**, book battery swap services at nearby stations, and manage appointments seamlessly. It uses a **MySQL database** for storing user and appointment data securely.

---

## 🚀 Features

- 👤 Login / Signup system
- 🔄 Battery Swap options
- 📍 Search nearby stations
- 📅 Add new appointments
- 👓 View existing bookings
- 📦 Admin panel to manage all appointments

---

## 🧠 How to Use

### 1. Start the app:

```bash
python smartvolt.py

Steps for Users:
Login or Sign up using the buttons provided on the home page.

Click on the "Swap Batteries" button.

You’ll be taken to the main interface with services:

🔍 Search nearby stations(it is not in working cause I have not done any work on it but in future I will make it runable)

➕ Add appointments

👁️ View existing appointments

Admin can go to /adminpanel to view and manage all user bookings.(admin panel username = Atharva and pass = 1234 or else you can add your own by inserting it into alogin table in smartvolt database )

Tech Stack:
Backend: Python, Flask
Frontend: HTML, CSS, Javascript
Database: MySQL
Deployment: Localhost
Secrets: Stored securely in .env


📦 Setup Instructions
1. Clone the repository
in terminal 
git clone https://github.com/AtharvaManale/Appointment-Booking.git
cd Appointment-Booking

2. Install the dependencies
firstly install python from browser, then
in terminal 
pip install flask (to install flask)
pip install python-dotenv

secondly install mysql installer from browser, then
in terminal
pip install mysql-connector-python (to install mysql.connector)

3. Setup your .env file
in vs code or any code editor
Create a .env file in the root directory:

env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=yourdatabase or database in schema.sql file(smartvolt)


4. Run the Flask app
in vs code or any code editor
python smartvolt.py

👨‍💻 Made By
Atharva Manale – with Flask, MySQL, and ❤️
(Its my first project please suggest me any improvements and feedbacks so I can make my next project effectively and smoothly)

📄 License
This project is licensed under the MIT License.