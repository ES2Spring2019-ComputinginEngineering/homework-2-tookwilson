import microbit
import random
import math


display.show(Image.BUTTERFLY) # Butterfly displays when program starts correctly
a= str(random.randomint(1, 1000))
filename= "pendulum_data_" + a + ".txt" #assorted number and name so data won't overwrite

while not button_a.is_pressed(): #wait for button A to be pressed to start collecting data
    sleep(10)

with open(filename, 'm') as file: # open text file to write to
   sleep (80) #give things time to happen
   display.show(Image.CLOCK1) #display clock while logging
   time0 = microbit.running_time() #get current time set the start point immediately before the while loop

   while not button_a.is_pressed():
       elapsed_time = microbit.running_time()- time0;
       accel_x = microbit.accelerometer.get_x()
       accel_y = microbit.accelerometer.get_y()
       accel_z = microbit.accelerometer.get_z()
       accel_pendulum = str(elapsed_time) + "\t" + str(accel_x) + "\t" + str(accel_y) + "\t" + str(accel_z) + "\n"
       file.write(accel_pendulum)

    display.show(Image.TARGET) #display target when program concludessw
file.close()
