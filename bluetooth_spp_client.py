import tkinter as tk
import bluetooth
import random

class BluetoothSPPClient:
    def __init__(self, master):
        self.master = master
        master.title("Bluetooth SPP Client")
        
        self.connect_button = tk.Button(master, text="Connect", command=self.connect)
        self.connect_button.pack()
        
        self.relay_button = tk.Button(master, text="Toggle Relay", command=self.toggle_relay)
        self.relay_button.pack()
        
        self.battery_label = tk.Label(master, text="Battery: --%")
        self.battery_label.pack()
        
        self.info_label = tk.Label(master, text="System Info")
        self.info_label.pack()

    def connect(self):
        nearby_devices = bluetooth.discover_devices()
        print("Found devices:")
        for addr in nearby_devices:
            print(addr)
        
        # Connect to a Bluetooth SPP service
        # self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        # self.sock.connect((addr, port))  # Use appropriate addr and port

    def toggle_relay(self):
        # Code to toggle relay on/off
        print("Relay Toggled")
        
    def update_battery(self):
        battery_level = random.randint(0, 100)  # Simulate battery level
        self.battery_label.config(text=f"Battery: {battery_level}%")
        self.master.after(5000, self.update_battery)  # Update every 5 seconds

if __name__ == '__main__':
    root = tk.Tk()
    client = BluetoothSPPClient(root)
    client.update_battery()  # Start battery monitoring
    root.mainloop()