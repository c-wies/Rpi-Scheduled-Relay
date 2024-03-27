import sched
import time
import threading
import growLightSwitch as switch

#Set On/Off times as struct_time object

nowTime = time.strptime(time.strftime('%Y %m %d %H:%M:%S', time.localtime()), '%Y %m %d %H:%M:%S')

#Initialize schedulers for On/Off tasks
lampOnScheduler = sched.scheduler(time.time, time.sleep)
lampOffScheduler = sched.scheduler(time.time, time.sleep)  

def startSchedule() :
    while(True):
        lampOnTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 07:00:00', '%Y %m %d %H:%M:%S')
        lampOffTime = time.strptime(time.strftime('%Y %m %d', time.localtime()) + ' 22:30:00', '%Y %m %d %H:%M:%S')
        
        lampOnScheduler.enterabs(time.mktime(lampOnTime), 1, switch.lampOn, ())
        lampOffScheduler.enterabs(time.mktime(lampOffTime), 1, switch.lampOff, ())

        timeArray = [lampOnScheduler, lampOffScheduler]
        
        if time.mktime(nowTime) > time.mktime(lampOnTime) and time.mktime(nowTime) < time.mktime(time.strptime('23:59:59', '%H:%M:%S')):
            switch.lampOn()
            timeArray = [lampOffScheduler, lampOnScheduler]
        
        for x in timeArray:
            x.run()