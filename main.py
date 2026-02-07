import bluetooth

# Bluetooth SPP Client
class BluetoothSPPClient:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = None

    def connect(self):
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((self.address, self.port))
            print('Connected to', self.address)
        except bluetooth.btcommon.BluetoothError as e:
            print('Bluetooth Error:', e)

    def send_data(self, data):
        if self.sock:
            self.sock.send(data)
            print('Data sent:', data)
        else:
            print('Socket not connected')

    def receive_data(self):
        if self.sock:
            data = self.sock.recv(1024)
            print('Data received:', data)
            return data
        else:
            print('Socket not connected')

    def close(self):
        if self.sock:
            self.sock.close()
            print('Connection closed')
