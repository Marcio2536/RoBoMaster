command=""
com_list=""
varible=""
action=""
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
        elif command=="combine24":
            if varible=="robo":
                pass
            elif varible=="local":
                pass
        else:
            print("Error: Unrecognised Command")
    elif len(com_list)==1:
        if command=="setdefault":
            pass
        else:
            print("Error: Unrecognised Command")
    else:
        print("Error: Unrecognised Command")
            