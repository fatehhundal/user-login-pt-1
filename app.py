from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods="GET")
def login():
    msg = ''
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        mydb = mysql.connector.connect(
            host='localhost',
            user ='root',
            password ='yourpassword',
            database = 'yourdatabase'
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name=%s AND Password=%s")
        account=mycursor

        if account:
            name = account[1]
            msg = "Logged in Successfully"
            return render_template('welcome.html', name=name, msg=msg)
        else:
            msg = "Incorrect Credentials. Kindly check."
    
    return render_template('login.html', msg=msg)

@app.route('/logour')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)