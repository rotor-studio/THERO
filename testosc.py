
from time import sleep
from pyOSC.OSC import OSCClient, OSCMessage

c = OSCClient()
c.connect( ("192.168.0.198", 40002) )

oscmsg = OSCMessage("/my/osc/address")

c.send(oscmsg)




