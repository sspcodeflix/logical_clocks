class VectorClock:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.clock = [0] * num_nodes

    def tick(self):
        # Increment the clock for the node's own event
        self.clock[self.node_id] += 1

    def send_event(self):
        # Increment the clock on send events
        self.tick()
        return self.clock.copy()

    def receive_event(self, received_clock):
        # On receive events, update the clock to the max of current and received clocks
        self.tick()
        self.clock = [max(self.clock[i], received_clock[i]) for i in range(len(self.clock))]

    def get_time(self):
        return self.clock

# Example usage
num_nodes = 3
clock1 = VectorClock(0, num_nodes)
clock2 = VectorClock(1, num_nodes)
clock3 = VectorClock(2, num_nodes)

# Node 1 sends a message
send_clock = clock1.send_event()
print(f"Clock 1 time after sending a message: {clock1.get_time()}")

# Node 2 receives the message
clock2.receive_event(send_clock)
print(f"Clock 2 time after receiving the message: {clock2.get_time()}")

# Node 2 sends a message to Node 3
send_clock = clock2.send_event()
print(f"Clock 2 time after sending a message to Node 3: {clock2.get_time()}")

# Node 3 receives the message
clock3.receive_event(send_clock)
print(f"Clock 3 time after receiving the message: {clock3.get_time()}")
