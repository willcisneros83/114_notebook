from asyncio.base_futures import _format_callbacks
from flask import (
    Flask,
    request
)
from app.lib import Queue


QUEUE = Queue()
app = Flask(__name__)



@app.post("/messages")
def queue_messages():
    msg_data = request.json
    QUEUE.enqueue(msg_data)
    return "OK", 204

@app.get("/messages/<int:qty>")
def get_messages(qty):
    if qty < 0:
       return "ERROR", 400
    if qty > 10:
       return "ERROR", 400
    out = {}
    out_list = []
    for _ in range(qty):
        msg = QUEUE.dequeue()
        out_list.append(msg)
    out["messages"] = out_list
    return out
