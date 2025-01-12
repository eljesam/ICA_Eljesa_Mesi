from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.hardware_code.hardware_control import initialize_hardware, read_sensor_data, control_actuator, cleanup_hardware
from app.pubnub_config import pubnub
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/vision_control'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import User, Device, ObstacleDetection

@app.route('/')
def index():
    sensor_data = read_sensor_data()
    if sensor_data:
        control_actuator('Obstacle detected')
        log = ObstacleDetection(timestamp = datetime.now(), distance = sensor_data, device_id = 1)
        db.session.add(log)
        db.session.commit()
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
    try:
        app.run(debug=True)
        
    finally:
        cleanup_hardware()
    
    
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory

class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNConnectedCategory:
            pubnub.publish().channel('vision_control').message('Hello from the other side').sync()
    def message(self, pubnub, message):
        pass
    
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('vision_control').execute()

@app.route('/publish')
def publish_message():
    pubnub.publish().channel('vision_control').message('Hello from the other side').sync()
    return 'Message published'