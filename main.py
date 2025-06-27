# main.py
from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def pubsub_event():
    envelope = request.get_json()
    
    if not envelope or 'message' not in envelope:
        return "Bad Request", 400

    pubsub_msg = envelope["message"]

    if 'data' in pubsub_msg:
        payload = base64.b64decode(pubsub_msg["data"]).decode("utf-8")
        event = json.loads(payload)
        file_name = event.get("name")
        bucket = event.get("bucket")
        print(f"📸 New file uploaded: {file_name} in bucket: {bucket}")
    else:
        print("No data field in message.")

    return "OK", 200


