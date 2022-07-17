from appJar import gui
from time import strftime, sleep
from datetime import datetime

#button function
def press(button):
    if button == "Start":
        clock_in()
        start_timer()
        app.registerEvent(update_timer)

    if button == "Stop":
        clock_out()
        off()

#clock functions
def clock_in():
    date = strftime("%d-%m-%Y")
    start = strftime("%H:%M:%S")
    global time1
    global project
    time1 = datetime.strptime(start, "%H:%M:%S")
    project = app.getEntry("Working on:")
    file = open(project + ".txt", "a")
    file.write("Date: " + date)
    file.write("\n")
    file.write("Started at " + start)
    file.write("\n")

def clock_out():
    end = strftime("%H:%M:%S")
    time2 = datetime.strptime(end, "%H:%M:%S")
    project = app.getEntry("Working on:")
    file = open(project + ".txt", "a")
    file.write("Stopped at " + end)
    file.write("\n")
    interval = time2 - time1
    file.write("Worked for " + str(interval))
    file.write("\n\n")

#off function
def off():
    sleep(1)
    app.stop()
    
#timer functions    
def start_timer():
    global value
    current = strftime("%H:%M:%S")
    time0 = datetime.strptime(current, "%H:%M:%S")
    value = time0 - time1
    app.addLabel('timer', str(value))

def update_timer():
    current = strftime("%H:%M:%S")
    time0 = datetime.strptime(current, "%H:%M:%S")
    value = time0 - time1
    app.setLabel('timer', str(value))

#app
app = gui("Worktime Clock","400x200")
app.setIcon("C:/Users/kamil/Pictures/dkicon.ico")
app.setLocation("CENTER")
app.setBg("grey", False, False)
app.addLabel("l1", "Worktime Clock")
app.setFont(size=12, family="Verdana")
app.addLabelEntry("Working on:")
app.addButtons(["Start", "Stop"], press)

app.go()