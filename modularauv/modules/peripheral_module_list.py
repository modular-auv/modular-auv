from modules import Module
from enum import Enum

class PMLAdditionStatus(Enum):
    SUCCESS = 0,
    LOCATION_CONFLICT = 1

class PeripheralModuleList:
    def __init__(self):
        self.peripherals = []
    def get(self, id:int):
        try:
            return self.peripherals[id]
        except IndexError:
            return None
    def add(self, peripheral:Module, id:int) -> PMLAdditionStatus:
        if self.get(id):
            return PMLAdditionStatus.LOCATION_CONFLICT
        else:
            self.peripherals[id] = peripheral
            peripheral._on_central_module_addition(self)


