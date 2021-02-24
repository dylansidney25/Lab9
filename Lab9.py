import serial
from guizero import App, Slider, PushButton
from gpiozero import AngularServo
from time import sleep

Servo1_Save = []
Servo2_Save = []

def exitGUI():                                      #This fucntion asks 
    if app.yesno("Close", "Do you want to quit?"):  #this line opens a yesno window asking the user if they wish to close the window
        app.destroy()                               #this line destroys the app when yes is selected
        print("Goodbye")
        ser.close()                                 #This Closes the Serial Port

def Turn_Servo1(slider_value):                      #This function takes the reading from the slider and sends it to the arduino for the motor command
    Servo1_Value = slider_Horizontal.value          #this line reads the slider value
    ser.write(str("M1").encode('utf-8'))            #this line tells the arduino that the following number is for Servo1
    ser.write(str("\n").encode('utf-8'))            #this is the string termination line to seperate "m1" from the angle value
    ser.flush()                                     #this line cleans out the serial port so there is no garbage in the serial port
    ser.write(str(Servo1_Value).encode('utf-8'))    #This line sends the value of the angle for the arduino to write to the servo
    ser.write(str("\n").encode('utf-8'))            #this is the string termination line to seperate the angle value from any following data
    ser.flush()                                     #this line cleans out the serial port so there is no garbage in the serial port
    
def Turn_Servo2(slider_value):                      #This function takes the reading from the slider and sends it to the arduino for the motor command
    Servo2_Value = slider_Vertical.value            #this line reads the slider value
    ser.write(str("M2").encode('utf-8'))            #this line tells the arduino that the following number is for Servo2
    ser.write(str("\n").encode('utf-8'))            #this is the string termination line to seperate "m2" from the angle value
    ser.flush()                                     #this line cleans out the serial port so there is no garbage in the serial port
    ser.write(str(Servo2_Value).encode('utf-8'))    #This line sends the value of the angle for the arduino to write to the servo
    ser.write(str("\n").encode('utf-8'))            #this is the string termination line to seperate the angle value from any following data
    ser.flush()                                     #this line cleans out the serial port so there is no garbage in the serial port
    
def Save_Servos():                                  #This function takes the current reading of the two sliders and saves them into their own arrays
    Servo1_Save.append(slider_Horizontal.value)     #this line saves the value of the horizontal slider
    Servo2_Save.append(slider_Vertical.value)       #This line saves the value of the vertical slider
    
def Recall_Servos():                                #this function reads out all the values in the saved arrays into the arduino for motor command
    for i in range (0, len(Servo1_Save)):           #This line is a for loop that determines the amount of loops by viewing the length of the arrays
        
        ser.write(str("M1").encode('utf-8'))        #this line tells the arduino that the following number is for Servo1
        ser.write(str("\n").encode('utf-8'))        #this is the string termination line to seperate "m1" from the angle value
        ser.flush()                                 #this line cleans out the serial port so there is no garbage in the serial port
        ser.write(str(Servo1_Save[i]).encode('utf-8'))    #This line sends the value of the angle for the arduino to write to the servo. The angle is chosen by the array location = i
        ser.write(str("\n").encode('utf-8'))        #this is the string termination line to seperate "m1" from the angle value
        ser.flush()                                 #this line cleans out the serial port so there is no garbage in the serial port
        
        ser.write(str("M2").encode('utf-8'))        #this line tells the arduino that the following number is for Servo2
        ser.write(str("\n").encode('utf-8'))        #this is the string termination line to seperate "m2" from the angle value
        ser.flush()                                 #this line cleans out the serial port so there is no garbage in the serial port
        ser.write(str(Servo2_Save[i]).encode('utf-8'))    #This line sends the value of the angle for the arduino to write to the servo. The angle is chosen by the array location = i
        ser.write(str("\n").encode('utf-8'))        #this is the string termination line to seperate "m1" from the angle value
        ser.flush()                                 #this line cleans out the serial port so there is no garbage in the serial port
        
        sleep(2)                                    #pauses to show the position

ser = serial.Serial("/dev/ttyUSB0", 9600)           #This line sets up the serial port so data can be sent through it
ser.flush()                                         #this line cleans out the serial port so there is no garbage in the serial port
sleep(3)                                            #this line just gives the arduino time to understand the monitor is being turned on

app = App(title = "servo control with arduino", width = 800, height = 400) #This line sets up the app window with a specific tital and dimensions
app.bg = "blue"                                     #This line sets the app background to be blue

slider_Horizontal = Slider(app, height = 40, width = 750, start = -90, end = 90, command = Turn_Servo1) #This line sets up the slider specs and command line
slider_Horizontal.bg = "red"                        #This line sets the slider background to red

slider_Vertical = Slider(app, height = 40, width = 750, start = -90, end = 90, command = Turn_Servo2)   #This line sets up the slider specs and command line
slider_Vertical.bg = "red"                          #This line sets the slider background to red

Save_Position = PushButton(app, text = "Save Angular Position", command = Save_Servos)                  #This line sets up the save button specs and command line
Save_Position.bg = "green"                         #This line sets the button colour to green

Recall_Position = PushButton(app, text = "View Saved Positions", command = Recall_Servos)               #This line sets up the recall button specs and command line
Recall_Position.bg = "green"                       #This line sets the button colour to green  

app.when_closed = exitGUI
app.display()
                
