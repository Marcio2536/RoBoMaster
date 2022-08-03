from more_itertools import strip
import Robot_Control.Control as control
command=""
com_list=""
variable=""
action=""
error=["Invalid Variable","Unrecognised Command"]
robo_var={"speed":10,"mode":"free"}
print("Welcome To RoBoMaster Command Line")

while True:
    command=input("RoBoMaster $")
    ind=command.index(" ")
    ind+=1
    com_list=command.split()
    action=com_list[0]
    variable=com_list[1]
    if action=="setssid":
        command=command+"\""
        ssid=command[ind:-1]
        print("Sucessfully Set SSID",ssid)
    elif action=="setpassword":
        password=variable
        print("Sucessfully Set Password")
    elif action=="combine24":
        if variable=="r":
            pass
        elif variable=="c":
            pass
    elif action=="setspeed":
        if type(variable)=="int" or type(variable)=="float":
            robo_var["speed"]=variable
            print("RoBo Speed Set")
        else:
            print("Error:",error[0])
    elif action=="epconnect":
        message=control.connect(ssid,password)
        print(message)
    elif command=="setdefault":
        pass
    else:
        print("Error:",error[1])
            
