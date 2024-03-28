import sched
import time
import growLightSwitch as switch

#Initialize schedulers for On/Off tasks
lampOnScheduler = sched.scheduler(time.time, time.sleep)
lampOffScheduler = sched.scheduler(time.time, time.sleep)  

def startSchedule() :
    while(True):
        #GMake time_struct object of current timem to check against the schedule
        nowTime = time.strptime(time.strftime('%Y %m %d %H:%M:%S', time.localtime()), '%Y %m %d %H:%M:%S')

        #Make time_struct objects off scheduled On/Off times
        lampOnTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 08:00:00', '%Y %m %d %H:%M:%S')
        lampOffTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 22:30:00', '%Y %m %d %H:%M:%S')
        
        #Configure On/Off schedulers
        lampOnScheduler.enterabs(time.mktime(lampOnTime), 1, switch.lampOn, ())
        lampOffScheduler.enterabs(time.mktime(lampOffTime), 1, switch.lampOff, ())

        #Init array of schedulers
        timeArray = [lampOnScheduler, lampOffScheduler]
        
        #Check if the Lamp is supposed to be On. Turn on if True.
        #If true reverse scheduler array to make next schedule lampOffScheduler
        #Add one day to current (86400 seconds) lampOnTimeValue so light will turn on according to schedule tomorrow
        if time.mktime(nowTime) > time.mktime(lampOnTime) and time.mktime(nowTime) < time.mktime(lampOffTime):
            switch.lampOn()
            lampOnScheduler.enterabs(time.mktime(lampOnTime) + float(86400), 1 , switch.lampOn, ())
            timeArray = [lampOffScheduler, lampOnScheduler]
        
        #Run each scheduler in order. Exit loop to reset time time objects to the current date.
        for x in timeArray:
            x.run()