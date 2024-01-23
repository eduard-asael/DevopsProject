from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:45431@localhost/devopsproject'
# db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, username, email, phone_number):
        self.username = username
        self.email = email
        self.phone_number = phone_number

@app.route("/add_user", methods=['POST'])
def add_user():
    # Wrap the database operation within an app context
    with app.app_context():
        db.create_all()
        # Get user input from the form
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        
        # Check if the email already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template("used_email.html")
        
        # Create a new user object and add it to the database
        new_user = User(username=username, email=email, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template("thanks-page.html")

# Routes for your web pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/photos-gallery")
def photosgallery():
    return render_template("photos-gallery.html")

@app.route("/videos-gallery")
def videosgallery():
    return render_template("videos-gallery.html")

@app.route("/drone-gallery")
def dronegallery():
    return render_template("drone-gallery.html")

if __name__ == "__main__":
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Run the Flask app
    app.run(debug=True, port=3000)
