import RPi.GPIO as GPIO
import time

PIR_PIN = 31
BUZZER_PIN = 40

def initialize_hardware():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    
def read_sensor_data():
    motion_detected = GPIO.input(PIR_PIN)
    return motion_detected

def control_actuator(motion_detected):
    if motion_detected:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        
def cleanup_hardware():
    GPIO.cleanup()