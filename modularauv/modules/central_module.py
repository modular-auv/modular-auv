from modules import Module, PeripheralModuleList
from hardware.data_handling import CentralServer

class CentralModule(Module):
    def __init__(self, clock):
        self.peripherals = PeripheralModuleList()
        self.central_server = CentralServer(65432)