import requests
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

def postServer(payload):
    r = requests.post('http://3.18.215.148:8080/lab10Pi', json=payload)
    j = r.json()
    if j['total'] >= 0:
        result = j['display']
        GPIO.output(0, result[0] == '1')
        GPIO.output(1, result[1]=='1')
        GPIO.output(7, result[2]=='1')
        GPIO.output(8, result[3]=='1')
        GPIO.output(4, result[4] =='1')
        GPIO.output(5, result[5] == '1')
        GPIO.output(6, result[6] == '1')
    #GPIO.output(3, j['r'] == '1')
        return j['total']
    else:
        return 0

while True:
    
    if GPIO.input(14):
        codigo = '0' if GPIO.input(15) else '1'
        codigo += '0' if GPIO.input(18) else '1'
        codigo += '0' if GPIO.input(23) else '1'
        codigo += '0' if GPIO.input(24) else '1'
        total = postServer({'pi': codigo})
        while total > 0:
            total-=1
            time.sleep(1)
            GPIO.output(3, True)
            time.sleep(1)
            GPIO.output(3, False)
            time.sleep(1)
            
GPIO.cleanup()