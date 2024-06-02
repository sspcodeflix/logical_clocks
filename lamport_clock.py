
class LamportClock:
    def __init__(self):
        self.time = 0

    def tick(self):
        # Increment the clock on internal events
        self.time += 1

    def send_event(self):
        # Increment the clock on send events and return the time
        self.tick()
        return self.time

    def receive_event(self, received_time):
        # On receive events, update the clock to the max of current time and received time + 1
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        return self.time

# Example usage
clock1 = LamportClock()
clock2 = LamportClock()

# Node 1 sends a message
send_time = clock1.send_event()
print(f"Clock 1 time after sending a message: {clock1.get_time()}")

# Node 2 receives the message
clock2.receive_event(send_time)
print(f"Clock 2 time after receiving the message: {clock2.get_time()}")
