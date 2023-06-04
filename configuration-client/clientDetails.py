# python file which contains client details
import fcntl
import json
import socket
import struct

class ClientDetails:
   
   def __init__(self):
      self.ServerVendor = self.getVendor()
      self.ServerModel = self.getModel()
      self.ServerSerialNo = self.getSerialNo()
      self.ServerMac = self.getMac()
      self.details = json.dumps({self.ServerMac:{"Vendor":self.ServerVendor,"Model":self.ServerModel,"SerialNo":self.ServerSerialNo,"MAC":self.ServerMac}})
      
   def getVendor(self):
      return "HP Enterprise"
      
   def getModel(self):
      return "DL160 G7"
      
   def getSerialNo(self):
      return "6CD2188GG3"
      
   def getMac(self):
      interface = "enp0s3"
      try:
         sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
         info = fcntl.ioctl(sock.fileno(),0x8927,struct.pack('256s',interface.encode('utf-8')[:15]))
         mac_address = ":".join("%02x" % b for b in info[18:24])
         return mac_address
      except IOError:
         return None

if __name__ == "__main__":

   MyClientDetails = ClientDetails()
   print("Client Details are as follows:")
   print(MyClientDetails.details)
