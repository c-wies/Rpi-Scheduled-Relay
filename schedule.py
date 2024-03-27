import sched
import time
import growLightSwitch as switch

#Get current time to check against the schedule
nowTime = time.strptime(time.strftime('%Y %m %d %H:%M:%S', time.localtime()), '%Y %m %d %H:%M:%S')

#Initialize schedulers for On/Off tasks
lampOnScheduler = sched.scheduler(time.time, time.sleep)
lampOffScheduler = sched.scheduler(time.time, time.sleep)  

def startSchedule() :
    while(True):
        #Make time_struct objects off scheduled On/Off times
        lampOnTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 08:00:00', '%Y %m %d %H:%M:%S')
        lampOffTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 22:30:00', '%Y %m %d %H:%M:%S')
        
        #Configure On/Off schedulers
        lampOnScheduler.enterabs(time.mktime(lampOnTime), 1, switch.lampOn, ())
        lampOffScheduler.enterabs(time.mktime(lampOffTime), 1, switch.lampOff, ())

        #Init array of schedulers
        timeArray = [lampOnScheduler, lampOffScheduler]
        
        #Check if the Lamp is supposed to be On/Off at the current time
        #Modify order of scheduler array if necessary
        if time.mktime(nowTime) > time.mktime(lampOnTime) and time.mktime(nowTime) < time.mktime(time.strptime('23:59:59', '%H:%M:%S')):
            switch.lampOn()
            timeArray = [lampOffScheduler, lampOnScheduler]
        
        #Run each scheduler in order. Exit loop to reset On/Off time objects to the new date
        for x in timeArray:
            x.run()