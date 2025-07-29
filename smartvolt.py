from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "1234"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "#Atharva25",
    database = "smartvolt",
    port = 3306,
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    Username = request.form['Username']
    Password = request.form['Password']
    
    query1 = "SELECT * FROM login WHERE Username = %s AND Password = %s" 
    mycursor.execute(query1, (Username, Password))
    user = mycursor.fetchone()

    mycursor.execute("SELECT * FROM appointments WHERE username = %s", (Username,))
    exist = mycursor.fetchone()

    if not exist:
        mycursor.execute("INSERT INTO appointments(username) VALUES(%s)", (Username,))
        mydb.commit()

    if user:
        session['Username'] = Username
        return redirect('/home')
    else:
        return "Invalid credentials. Try again." 

@app.route('/signup')
def signup():
    return render_template("create.html")

@app.route('/create', methods = ['POST'])
def create():
    Email = request.form['Email']
    Username = request.form['Username']
    Password = request.form['Password']

    mycursor.execute("SELECT * FROM login WHERE Username = %s", (Username,))
    exist = mycursor.fetchone()

    if not exist:
        mycursor.execute("INSERT INTO login (Email, Username, Password) VALUE(%s, %s, %s)",(Email, Username, Password))
        mydb.commit()

    return redirect('/')

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/swap')
def swap():
    return render_template("swap.html")

@app.route('/date1')
def appdate():
    return render_template("date.html")

@app.route('/date2', methods=['POST'])
def date():
    Date = request.form['Date']
    Username = session.get('Username')

    query2 = "UPDATE appointments SET date_ = %s WHERE username = %s"
    mycursor.execute(query2,(Date, Username))
    mydb.commit()

    query3 = "SELECT * FROM appointments WHERE username = %s AND date_ = %s"
    mycursor.execute(query3, (Username, Date))
    exist = mycursor.fetchone()
        
    session['Date'] = Date

    if not exist:
        query4 = "INSERT INTO appointments (username, date_) VALUES (%s, %s)"
        mycursor.execute(query4, (Username, Date))
        mydb.commit()

    return redirect('/appointment')

@app.route('/appointment')
def appointment():
    return render_template("appointment.html")

@app.route('/select', methods= ['POST'])
def select():
    Station_id = request.form['station_id']
    Time = request.form['time']
    Username = session.get('Username')
    Date = session.get('Date')
        
    query5 = "UPDATE appointments SET station_id = %s, time_ = %s WHERE username = %s"
    mycursor.execute(query5, (Station_id, Time, Username))
    mydb.commit()

    query6 = "SELECT * FROM appointments WHERE username = %s AND station_id = %s AND date_ = %s AND time_ = %s" 
    mycursor.execute(query6, (Username, Station_id, Date, Time))
    exist = mycursor.fetchone()

    session['Station_id'] = Station_id
    session['Time'] = Time

    if not exist:
        query7 = "INSERT INTO appointments (sername, station_id, date_, time_) VALUES(%s, %s, %s, %s)"
        mycursor.execute(query7, (Username, Station_id, Date, Time))
        mydb.commit()
    return render_template("confirm.html")   
        

@app.route('/bookings')
def bookings():
    Username = session.get('Username')

    query8 = "SELECT station_id, date_, time_ FROM appointments WHERE username = %s"
    mycursor.execute(query8, (Username,))
    user_bookings = mycursor.fetchall()

    return render_template("bookings.html", bookings = user_bookings)

@app.route('/delete1', methods=['POST'])
def delete1():
    Username = session.get('Username')
    Station_id = request.form['station_id']
    Date = request.form['date']
    Time = request.form['time']

    query9 = "DELETE FROM appointments WHERE username = %s AND station_id = %s AND date_ = %s AND time_ = %s"
    mycursor.execute(query9, (Username, Station_id, Date, Time))
    mydb.commit()

    return render_template("bookings.html")

@app.route('/a')
def a():
    return render_template("alogin.html")

@app.route('/alogin', methods = ['POST'])
def alogin():
    Username = request.form['Username']
    Password = request.form['Password']

    query10 = "SELECT * FROM alogin WHERE Username = %s AND Password = %s"
    mycursor.execute(query10, (Username, Password))
    admin = mycursor.fetchone()
        
    if admin:
        session['Username'] = Username
        return redirect('/adminpanel')
    else:
        return "Invalid Credentials."

@app.route('/adminpanel')
def adminpanel():

    return render_template("admin.html")

@app.route('/manage')
def allbookings():
    query11 = "SELECT  username, station_id, date_, time_ FROM appointments"
    mycursor.execute(query11)
    all_bookings = mycursor.fetchall()

    return render_template("manage.html", allbookings = all_bookings)

@app.route('/delete2', methods = ['POST'])
def delete2():
    Username = request.form['username']
    Station_id = request.form['station_id']
    Date = request.form['date']
    Time = request.form['time']

    query12 = "DELETE FROM appointments WHERE username = %s AND station_id = %s AND date_ = %s AND time_ = %s"
    mycursor.execute(query12, (Username, Station_id, Date, Time))
    mydb.commit()

    query13 = "SELECT username, station_id, date_, time_ FROM appointments"
    mycursor.execute(query13)
    all_bookings = mycursor.fetchall()

    return render_template("manage.html", allbookings = all_bookings)

if __name__ == '__main__':
    app.run(debug=True)