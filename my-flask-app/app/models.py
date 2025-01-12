from app import db 
class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(255), nullable=False)
    
class Device(db.Model):
    __tablename__ = 'Devices'
    DeviceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OwnerName = db.Column(db.String(255), nullable=False)
    Status = db.Column(db.Enum('Active', 'Inactive'), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=True)

class ObstacleDetection(db.Model):
    __tablename__ = 'ObstacleDetections'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    Distance = db.Column(db.Float, nullable=False)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'), nullable=True)