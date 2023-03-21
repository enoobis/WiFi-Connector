import tkinter as tk
import subprocess
import time

class WifiConnector:
    def __init__(self, master):
        self.master = master
        master.title("WiFi Connector")

        # Create labels and buttons
        self.label = tk.Label(master, text="Click 'Start' to connect to WiFi network every 2 seconds")
        self.label.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_wifi)
        self.start_button.pack()
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_wifi, state=tk.DISABLED)
        self.stop_button.pack()

        self.process = None
        self.connected = False

    def start_wifi(self):
        self.connected = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.label.config(text="Connecting to WiFi network...")
        self.connect_to_wifi()

    def stop_wifi(self):
        self.connected = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        if self.process:
            self.process.kill()
        self.label.config(text="Click 'Start' to connect to WiFi network every 2 seconds")

    def connect_to_wifi(self):
        if not self.connected:
            return
        try:
            subprocess.check_output(['netsh', 'wlan', 'connect', 'SSID="Your SSID"'])
            self.label.config(text="Connected to WiFi network!")
        except subprocess.CalledProcessError:
            self.label.config(text="Failed to connect to WiFi network")
        time.sleep(2)
        self.connect_to_wifi()

root = tk.Tk()
my_gui = WifiConnector(root)
root.mainloop()
