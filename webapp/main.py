import uvicorn

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from connection.manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()

templates = Jinja2Templates(directory="templates")


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    '''
    Handle websocket connections and broadcast messages to all connected clients.
    '''
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{manager.usernames[websocket]}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast(f"{username} left the chat")
    except Exception as e:
        manager.disconnect(websocket)
        print(f"Error: {e}")



@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    '''
    This is a web page for testing the websocket_endpoint.
    ''' 
    return templates.TemplateResponse("index.html", {"request" : request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)