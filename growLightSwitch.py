'''GPIO Control and state tracking for grow light relay
RELAY_PIN is is toggle for NO active low relay (pull pin down to close relay)
Using RPi pin numbering (Not Broadcom)'''
import RPi.GPIO as GPIO
#State of lamp True=ON False=OFF
#Relay trigger is board pin #3
RELAY_PIN = 7
TEST_PIN = 3
lampState = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(TEST_PIN, GPIO.OUT)
if GPIO.input(RELAY_PIN):
    lampState = False
else:
    lampState = True

    
#Pull relay pin low and toggle set state variable
def relayOn(PIN):
    GPIO.output(PIN, GPIO.LOW)
    if PIN == RELAY_PIN:
        lampState = True
    elif PIN == TEST_PIN:
        testState == True

#Set relay pin high and set state variable
def relayOff(PIN):
    GPIO.output(PIN, GPIO.HIGH)
    if PIN == RELAY_PIN:
        lampState = False
    elif PIN == TEST_PIN:
        testState == False
    #GPIO.cleanup()
    
def lampOn():
    relayOn(RELAY_PIN)
    
def lampOff():
    relayOff(RELAY_PIN)
    
def lampToggle():
    if lampState:
        relayOff(RELAY_PIN)
    else:
        relayOn(RELAY_PIN)
    
def testToggle():
    if testState:
        relayOff(TEST_PIN)
    else:
        relayOn(TEST_PIN)

