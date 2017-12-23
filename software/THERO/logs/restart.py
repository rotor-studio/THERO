import time, subprocess

# Logging function
def AddLog(status):
    # Add line to status log
    logFile = open('/home/pi/Desktop/THERO/logs/restart.txt', 'a')
    timeString = time.asctime(time.localtime(time.time()))
    logFile.write('%s %s\n' % (timeString, status))
    # Force the log to be written out
    logFile.flush()
    logFile.close()

# Start the process first time
process = subprocess.Popen(['python2', '/home/pi/Desktop/THERO/04_THERO._LAB.py'])
AddLog('Started')

while True:
    # Check the state of the process
    status = process.poll()

    if status != None:
        # Terminated, restart process
        process = subprocess.Popen(['python2', '/home/pi/Desktop/THERO/04_THERO._LAB.py'])
        print 'Termination code %d, restarted' % (status)
        AddLog('Restarted')
    else:
        # Still running
        time.sleep(1)
        print 'THERO is still running'
