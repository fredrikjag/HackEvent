from flask import Flask, request, render_template
import psycopg2


app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(dbname="webapp", user="webapp", password="application_password1")
    return conn


@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"
    
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

    if result:
        try:
            return render_template('dashboard.html', username=result[0][1])
        except:
            return render_template('login.html', error=True)
    else:
        return render_template('login.html', error=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
