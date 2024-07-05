from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        """
        The default behavior of the `__hash__` method for an instance of a class is as follows:
            1. It calls the `id()` function to obtain the memory address of the object. This address remains constant during the object's lifetime. Once an object is created, its `id()` is fixed until the object is destroyed, and changes to the object's content do not affect its memory address. In other words, for a given object, the `id()` function always returns the same value while the object exists.
            2. This memory address is used as the hash value.
        """
        self.active_connections: List[WebSocket] = []
        self.usernames: dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.usernames[websocket] = username

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        del self.usernames[websocket]

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)