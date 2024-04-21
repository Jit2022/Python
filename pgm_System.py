# Import Laberies
import sys
import datetime
#--------------------------------------Print System Statement -----------------------#
dt=datetime.datetime.now()
print ("I am System");
print ("My Python Version is ",sys.version);
print ("System date is ", dt.strftime("%c""%Z"));
#--------------------------------------Name Input ----------------------------------#
correctval="No"
while correctval.upper()=="NO":
    name=input("What is your Name?\n")
    print("Your name is", name)
    correctval=input("Is your name correct?\n")
    if correctval.upper()=='YES':
        print("Your have entered correct name!")
        i=0
        break
    elif correctval.upper()!='YES':
        print("Please enter correct Name")

print("So I got your name as",name, ",So I am existing Now!")