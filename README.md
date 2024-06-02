```
Lamport Clock:

Each node has a single integer clock.
The clock is incremented on internal events and send events.
Upon receiving a message, the node updates its clock to be the maximum of its current clock and the received clock, plus one.
```
```
Vector Clock:

Each node has a vector of clocks, one for each node in the system.
The node's own clock is incremented on internal events and send events.
Upon receiving a message, the node updates its clock by taking the element-wise maximum of its current clock and the received clock.
```