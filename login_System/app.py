from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from Dbcredential import Token

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
    return render_template('login.html')
    
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobileno = request.form['mobileno']
        password = request.form['password']
        print(fname,lname, email, mobileno, password)
        cur.execute("INSERT INTO register (fname, lname, email, mobileno, password) VALUES (%s,%s,%s,%s,%s)", (fname, lname, email, mobileno, password))
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/login', methods=['POST'])
def login():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur.execute('SELECT * FROM register WHERE email = %s and password = %s', (email, password))
        data = cur.fetchone() # was cur.fetchall()
        
        # Modify
        
        if data:
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'})
                
    #     if (len(data)):
    #         return redirect(url_for('dashboard'))
    # return redirect(url_for('Index'))

@app.route('/dashboard')
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)