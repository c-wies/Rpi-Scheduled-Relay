
# RaspberryPi Scheduled Relay

This is just something I slapped together to flip a relay on a schedule to control my garden grow lamp. This just flips a GPIO pin on a raspberry pi at a specific on and off time.

This is a learners project so it's not great. It is only configured for **NO (normally open)** relay logic. No global constants are set for the timers on/off times. 

Here's a tip if your **mains voltage(120V/220V)** through a relay: Get **solid state relays**. Using the cheap mechanical ones, they will start to stick and not make contact when closed unless you jostle them. My understnding is the arcing between contacts when closing builds up residue on the contacts, preventing the circuit from closing normally.



## Setup

Until I update the code (my setup is torn down, so I can't test for a while) here are the variables you need to configure:

|Action |Location |Variable |Type|
|-|-|-|-|
| On Time | schedule.py | lampOnTime | time_struct object |
| Off Time | schedule.py | lampOffTime | time_struct object |
| RPi GPIO Pin | growLightSwitch.py | RELAY_PIN | int |

## Feedback

At the time of writing I've been layed off from my technicians job and am putting all my time into studying programming and hopefully making a career change. I would be more than happy to see any obvious improvments that can be made to this hack if anybody takes the time. Submit a pull request or send me an email at wiesner.connor@gmail.com if you have any pointers!

