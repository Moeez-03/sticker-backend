from fastapi import APIRouter, Depends, UploadFile, WebSocket, WebSocketDisconnect
from app.services.storage_service import upload_to_aws_s3, upload_to_do_spaces
from typing import List

router = APIRouter()

# WebSocket manager to handle multiple connections
class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_update(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

websocket_manager = WebSocketManager()

@router.websocket("/ws/stickers")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time sticker updates.
    """
    await websocket_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)

@router.post("/upload/")
async def upload_sticker(file: UploadFile, is_premium: bool):
    """
    Upload a new sticker and notify all clients via WebSocket.
    """
    content = file.file.read()
    filename = file.filename
    if is_premium:
        url = upload_to_aws_s3(content, filename)
    else:
        url = upload_to_do_spaces(content, filename)

    # Send a real-time notification to all connected WebSocket clients
    await websocket_manager.send_update(f"New sticker uploaded: {filename}")

    return {"url": url, "message": "Sticker uploaded successfully"}
