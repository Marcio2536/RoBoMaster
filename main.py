import Robot_Control.Control as control
command=""
com_list=""
varible=""
action=""
error=["Invalid Variable","Unrecognised Command"]
robo_var={"speed":10,"mode":"free"}

print("Welcome To RoBoMaster Command Line")
while True:
    command=input("RoBoMaster $")
    com_list=command.split()
    action=com_list[0]
    if len(com_list)==2:
        varible=com_list[1]
        if action=="setssid":
            ssid=varible
            print("Sucessfully Set SSID")
        elif action=="setpassword":
            password=varible
            print("Sucessfully Set Password")
        elif action=="combine24":
            if varible=="r":
                pass
            elif varible=="c":
                pass
        elif action=="setspeed":
            if type(varible)=="int" or type(varible)=="float":
                robo_var["speed"]=varible
                print("RoBo Speed Set")
            else:
                print("Error:",error[0])
        elif action=="epconnect":
            message=control.connect(ssid,password)
            print(message)
        else:
            print("Error:",error[1])
    elif len(com_list)==1:
        if command=="setdefault":
            pass
        else:
            print("Error:",error[1])
    else:
        print("Error:",error[1])
            
