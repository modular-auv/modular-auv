from hardware.data_handling import DataTransferer
from modules import CentralModule
from abc import ABC, abstractmethod
class Module(ABC):
    def __init__(self, ID:int):
        self.ID = ID
        self.central_module = None

    @abstractmethod
    def _on_central_module_addition(self, central_module:CentralModule):
        self.central_module = central_module