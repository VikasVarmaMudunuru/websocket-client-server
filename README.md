# websocket-client-server
WebSocket Client–Server Communication in Python

Assignment: Bidirectional Messaging (Server <-> Client) 
This project demonstrates real-time two-way communication between a client and a server using Python and WebSockets.
Unlike traditional HTTP communication (which is request-response based), WebSockets enable full-duplex communication, allowing both the client and the server to send messages to each other independently.

Project Objective
The objective of this assignment is to:
Implement WebSocket communication using Python
Enable client-to-server message transfer
Enable server-to-client response
Understand asynchronous programming using asyncio
Build a basic real-time messaging system

Communication Flow
1️. Client → Server
The client connects to the server using a WebSocket connection.
The client sends a message to the server.
The server receives and processes the message.

2️. Server → Client

After receiving the client’s message, the server sends a response back.
The client waits asynchronously to receive the reply.
The communication happens in real time without closing the connection.
This demonstrates bidirectional (two-way) communication.

Technologies Used
Python 3
asyncio (Asynchronous Programming)
websockets library

Learning Outcomes
Through this assignment, I gained understanding of:
WebSocket protocol
Event loop handling in Python
Asynchronous functions (async / await)
Real-time client-server architecture
Bidirectional data transmission

Learning Conclusion
This project successfully demonstrates a simple yet effective implementation of real-time bidirectional communication between a client and a server using Python WebSockets. It highlights the importance of asynchronous programming in modern network applications.
