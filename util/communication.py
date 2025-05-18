#Confirm ess dac register format and value format during implementation

#from .smbus2 import SMBus
#bus=SMBus(1)
def read(devAddr, addr):
  return 00000000000000000
  #return bus.read_byte_data(devAddr, addr)
def write(devAddr, addr, value):
  return "0"
  #bus.write_byte_data(devAddr, addr, value)
def write_bulk(deAddr, addr, values):
  for v in values:
    #bus.write_byte_data(devAddr, addr, v)
    pass
  
    