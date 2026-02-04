import time 
import threading

class NormalTimer:
    def __init__(self):
        self.state = "IDLE"
        self.remaining = 0
        self.thread = None

    def start(self, seconds):
        self.state = "RUNNING"
        self.remaining = seconds

        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.remaining > 0 and self.state == "RUNNING":
            time.sleep(1)
            self.remaining -= 1
            print("Remaining:", self.remaining)

        if self.remaining == 0:
            self.state = "FINISHED"
            print("Timer done!")

        def pause(self):
            if self.state == "RUNNING":
                self.state == "PAUSED"
        
        def resume(self):
            if self.state == "PAUSED":
                self.state == "RUNNING"
                self.thread = threading.Thread(target=self.run)
                self.thread.start()

        def cancel(self):
            self.state = "IDLE"
            self.remaining = 0
            