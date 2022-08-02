import time
import robomaster
from robomaster import conn
from MyQR import myqr
from PIL import Image

def connect(ssid,password):
    QRCODE_NAME = "qrcode.png"
    if __name__ == '__main__':
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
