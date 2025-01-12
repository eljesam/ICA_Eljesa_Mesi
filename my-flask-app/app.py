from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.hardware.hardware_control import initialize_hardware, read_sensor_data, control_acutator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/vision_control'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import User, Device, ObstacleDetection

@app.route('/')
def index():
    sensor_data = read_sensor_data()
    return render_template('index.html', sensor_data=sensor_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    initialize_hardware()
    app.run(debug=True)