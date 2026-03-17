from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime
from flask import Flask, render_template, redirect, session, flash


app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

# -------------------------
# Database Connection
# -------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # your MySQL username
        password="@flag961TOAD", # your MySQL password
        database="arrowooddb"
    )

# -------------------------
# Routes
# -------------------------

@app.route('/')
def home():
    return render_template('index.html')  # create a home page template

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        service_type = request.form['service_requested']
        date = request.form['date']
    
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT idcustomer FROM customer WHERE email = %s",
            (email,)
        )
        result = cursor.fetchone()

        if result:
            idcustomer = result[0]
        else:
            # Manually generate a new id
            cursor.execute("SELECT MAX(idcustomer) FROM customer")
            max_id = cursor.fetchone()[0] or 0
            idcustomer = max_id + 1

            cursor.execute("""
                INSERT INTO customer (idcustomer, first_name, last_name, email, phone_number)
                VALUES (%s, %s, %s, %s, %s)
            """, (idcustomer, first_name, last_name, email, phone))


        # 2️⃣ Insert service request
        # Manually generate idservice
        cursor.execute("SELECT MAX(idservice) FROM service")
        max_service_id = cursor.fetchone()[0] or 0
        idservice = max_service_id + 1

        cursor.execute("""
            INSERT INTO service (idservice, service_type, scheduled_date, customer_idcustomer)
            VALUES (%s, %s, %s, %s)
        """, (idservice, service_type, date, idcustomer))
        conn.commit()
        cursor.close()
        conn.close()

        return """
                    <h2>Customer and Service Request submitted.</h2>
                    <style>
                        h2 {
                            text-align: center;
                            margin-top: 50px;
                            color: #333;
                        }
                        body {
                            background-color: #D2B48C;
                        }
                    </style>
                    <script>
                        setTimeout(() => { window.location.href = '/contact'; }, 3000);
                    </script>
                """  # Redirect to the same page after submission

    return render_template('contactus.html')
    
@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/ourwork')
def our_work():
    return render_template('ourwork.html')



# -------------------------
# Run the app
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)