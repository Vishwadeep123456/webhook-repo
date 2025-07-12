from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Server is Running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("Webhook Received:")
    print(data)  # 🧪 Just for testing — log it

    # Extract basic info
    event_type = request.headers.get("X-GitHub-Event")
    author = data['pusher']['name'] if 'pusher' in data else 'unknown'
    to_branch = data['ref'].split('/')[-1] if 'ref' in data else 'unknown'
    timestamp = datetime.utcnow().isoformat()

    print(f"{author} pushed to {to_branch} on {timestamp} (Event: {event_type})")

    return jsonify({"status": "received"}), 200
