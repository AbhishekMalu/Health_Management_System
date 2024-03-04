from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from DBcredential import Token

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

DB_HOST = Token.get("hostname")
DB_NAME = Token.get("database")
DB_USER = Token.get("username")
DB_PASS = Token.get("pwd")
DB_PORT = Token.get("port_id")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "select * from register"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    print(list_users)
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobileno = request.form['mobileno']
        password = request.form['password']
        cur.execute("INSERT INTO register (fname, lname, email, mobileno, password) VALUES (%s,%s,%s,%s,%s)", (fname, lname, email, mobileno, password))
        conn.commit()
        flash('Patient Added successfully')
        return redirect(url_for('Index'))
    

if __name__ == "__main__":
    app.run(debug=True)