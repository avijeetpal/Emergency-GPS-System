from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the MySQL connection string with your MySQL database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@hostname/user'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    aadhar_number = db.Column(db.String(12), unique=True)
    dob = db.Column(db.String(10))
    phone_number = db.Column(db.String(10))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        aadhar_number = request.form['aadhar']
        dob = request.form['dob']
        phone_number = request.form['phone_number']
        
        new_user = User(name=name, aadhar_number=aadhar_number, dob=dob, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))  # Redirect to homepage after account creation
    return render_template('createaccount.html')

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)

