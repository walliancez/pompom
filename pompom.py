# A small script that replicates the timer
# that is used when doing the pomodore study
# method. It's pretty damn uninteresting but
# it kinda works. // hannes

import time
import sys
import os

WORK_TIME = 11
SMALL_BREAK_TIME = 5*60
LONG_BREAK_TIME = 20*60
BREAK_COUNT = 0

def intro():
    print('Welcome to PomPom! Would you like to start?')
    response = raw_input('->')
    if(response == 'yes' or response == 'y'):
        start()


def start():
    break_count = 0
    while(True):
        timerLoop(WORK_TIME)
        if(get_response('Well done! Would you lke to take a break?')):
            if(break_count >= 4):
                timerLoop(LONG_BREAK_TIME)
                break_count = 0
            else:
                timerLoop(SMALL_BREAK_TIME)
                break_count += 1
        else:
            break
        if(not get_response('Break\'s over! Would you like to get start again?')):
            break

def formatTime(theTime):
    return ('0' if (theTime/60) < 10 else '')+str(theTime/60) + ':' + ('0' if (theTime%60) < 10 else '') +str(theTime % 60)

def get_response(title):
    response = raw_input(title + '\n->')
    if(response.lower() == 'yes' or response.lower() == 'y'):
        return True
    else:
        return False #should fix this shit sometime but prolly won't

def displayTime(t_time):
    sys.stdout.write(formatTime(t_time) + '\r')
    sys.stdout.flush()  

def timerLoop(t_time):
    while(True):
        t_time = t_time - 1
        displayTime(t_time)
        if(t_time == 0):
            break
        time.sleep(1)
    os.system('aplay -q sms-alert-5-daniel_simon.wav &> /dev/null')
intro()
