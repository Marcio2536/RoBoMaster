import time
import robomaster
from robomaster import robot
from MyQR import myqr
from PIL import Image
from robomaster import robot

def connect(ssid,password):
    QRCODE_NAME = "qrcode.png"
    helper = conn.ConnectionHelper()
    info = helper.build_qrcode_string(ssid=ssid, password=password)
    myqr.run(words=info)
    time.sleep(1)
    img = Image.open(QRCODE_NAME)
    img.show()
    if helper.wait_for_connection():
        return "Connected"
    else:
        return "Connect Failed"
def __init__():
    ep_robot=robomaster.robot.Robot()
    ep_robot.initialize(conn_type="sta")
    config.DEFAULT_CONN_TYPE = "sta"
    config.DEFAULT_PROTO_TYPE = "tcp"
