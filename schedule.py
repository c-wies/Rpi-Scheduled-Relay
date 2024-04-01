import sched
import time
import growLightSwitch as switch

#Initialize schedulers for On/Off tasks
#lampOnScheduler should only run once if script starts when lamp is supposed to be off
#Normal operation is running a loop between lampTomorrowScheduler and lampOffScheduler
lampOnScheduler = sched.scheduler(time.time, time.sleep)
lampTomorrowScheduler = sched.scheduler(time.time, time.sleep)
lampOffScheduler = sched.scheduler(time.time, time.sleep)  

def startSchedule() :
    while(True):
        #Make time_struct object of current timem to check against the schedule
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
        #If true set up lampTomorrowScheduler and modify timeArray to run schedule in proper order
        if time.mktime(nowTime) > time.mktime(lampOnTime) and time.mktime(nowTime) < time.mktime(lampOffTime):
            switch.lampOn()
            tomorrowOntime = time.mktime(lampOnTime)
            tomorrowOntime = tomorrowOntime + float(86400)
            lampTomorrowScheduler.enterabs(tomorrowOntime, 1, switch.lampOn, ())
            timeArray = [lampOffScheduler, lampTomorrowScheduler]
        
        #Run each scheduler in order
        for x in timeArray:
            x.run()