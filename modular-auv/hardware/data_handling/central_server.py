import socket
import threading

class CentralServer:
    def __init__(self, port:int):
        self.PORT = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.incoming_data = {}
    def open(self):
        self.socket.listen()
        threading.Thread(target=self._listen_for_client)
    def _listen_for_client(self):
        conn, addr = self.socket.accept()
        self.clients[addr] = conn
        self.open() # recursive
    def gather_data(self, keep:bool=False):
        return self.incoming_data
        if not keep:
            self.incoming_data.clear()

    def update(self):
        for addr, client in self.clients.items():
            data = client.recv(1024)
            if not data:
                self.clients.pop(addr)
            else:
                if self.incoming_data[addr]:
                    self.incoming_data[addr].append(data)
                else:
                    self.incoming_data[addr] = [data]
