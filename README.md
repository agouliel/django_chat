**Django 5 By Example**   
**Chapter 16 - Building a Chat Server**

A standard HTTP request/response model doesn’t work here because you need the browser to receive notifications as soon as new messages arrive. There are several ways you could implement this feature, using AJAX polling or long polling in combination with storing the messages in your database or Redis.

To work with asynchronous applications, you need to use another interface called **ASGI**, which can handle WebSocket requests as well.

**Channels** builds upon the native ASGI support available in Django and provides additional functionalities to handle protocols that require long-running connections, such as WebSockets, IoT protocols, and chat protocols.

**WebSockets** provide full-duplex communication by establishing a persistent, open, bidirectional TCP connection between servers and clients. Instead of sending HTTP requests to the server, you establish a connection with the server; once the channel is open, messages can be exchanged in both directions without needing to establish a new connection each time.

Channels replaces Django’s request/response cycle with messages that are sent across channels. HTTP requests are still routed to view functions using Django, but they get routed over channels. This allows WebSocket message handling as well, where you have producers and consumers that exchange messages across a channel layer. Channels preserves Django’s synchronous architecture.

An ASGI server is necessary for handling asynchronous requests, and we choose **Daphne** for its simplicity and compatibility, as it comes bundled with Channels.

To implement the chat server, you will need to take the following steps:
1. **Set up a consumer**: Consumers are individual pieces of code that can handle WebSockets in a very similar way to traditional HTTP views. You will build a consumer to read and write messages to a communication channel.
2. **Configure routing**: Channels provides routing classes that allow you to combine and stack your consumers. You will configure URL routing for your chat consumer.
3. **Implement a WebSocket client**: When the student accesses the chat room, you will connect to the WebSocket from the browser and send or receive messages using JavaScript.
4. **Enable a channel layer**: Channel layers allow you to talk between different instances of an application. They're a useful part of making a distributed real-time application. You will set up a channel layer using Redis.

`docker run -it --rm --name redis -p 6379:6379 redis:7.2.4`
