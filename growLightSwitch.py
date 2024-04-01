'''GPIO Control and state tracking for grow light relay
RELAY_PIN is is toggle for NO active low relay (pull pin down to close relay)
Using RPi pin numbering (Not Broadcom)'''
import RPi.GPIO as GPIO

#Relay trigger is RPi pin 7
RELAY_PIN = 7

#Declare lamp state tracking variable
#State of lamp True=ON False=OFF
lampState = False

#Init GPIO Interface
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)

#Check/Set lampState
if GPIO.input(RELAY_PIN):
    lampState = False
else:
    lampState = True

#Pass RPi pin to pull it low
def relayOn(PIN):
    GPIO.output(PIN, GPIO.LOW)
    
#Pass RPi pin number to pull it high
def relayOff(PIN):
    GPIO.output(PIN, GPIO.HIGH)
    
def lampOn():
    relayOn(RELAY_PIN)
    lampState = True
    
def lampOff():
    relayOff(RELAY_PIN)
    lampState = False
    
def lampToggle():
    if lampState:
        relayOff(RELAY_PIN)
    else:
        relayOn(RELAY_PIN)

