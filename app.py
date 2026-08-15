from flask import Flask, jsonify, render_template_string
from datetime import datetime, timezone
from threading import Lock

app = Flask(__name__)

# Intentionally local-only demo storage. No passwords or real credentials are accepted.
events = []
lock = Lock()

PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Phisher Media — Awareness Lab</title>
<style>
body{font-family:system-ui,sans-serif;background:#0b1020;color:#eef2ff;display:grid;place-items:center;min-height:100vh;margin:0}
.card{max-width:760px;margin:24px;padding:40px;border:1px solid #38f2b3;border-radius:24px;background:#11182d;box-shadow:0 20px 70px #0008}
.badge{display:inline-block;padding:7px 12px;border-radius:999px;background:#15352e;color:#38f2b3;font-weight:700}
h1{font-size:48px;margin:18px 0 8px} p{line-height:1.6;color:#b9c3dd}
button{border:0;border-radius:12px;padding:14px 20px;background:#38f2b3;color:#06120e;font-weight:800;cursor:pointer}
.notice{margin-top:24px;padding:16px;border-radius:14px;background:#202943}
</style>
</head>
<body>
<main class="card">
<span class="badge">EDUCATIONAL LAB ONLY</span>
<h1>Phisher Media</h1>
<p>A safe phishing-awareness simulation by <b>ROOT L00T</b>. This demonstration records only training events such as a simulated click. It never requests, stores, or transmits passwords, tokens, payment data, or other real credentials.</p>
<button onclick="simulateClick()">Open simulated training message</button>
<div id="status" class="notice">Ready for a local training exercise.</div>
</main>
<script>
async function simulateClick(){
  const r = await fetch('/event/click', {method:'POST'});
  const data = await r.json();
  document.getElementById('status').textContent = data.message;
}
</script>
</body>
</html>
"""


def record(event_type):
    with lock:
        events.append({
            "event": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })


@app.get("/")
def home():
    return render_template_string(PAGE)


@app.post("/event/click")
def click_event():
    record("simulated_click")
    return jsonify({"ok": True, "message": "Training event recorded. No credentials were collected."})


@app.get("/report")
def report():
    with lock:
        snapshot = list(events)
    clicks = sum(e["event"] == "simulated_click" for e in snapshot)
    return jsonify({
        "project": "Phisher Media",
        "founder": "ROOT L00T",
        "purpose": "Educational phishing-awareness simulation",
        "credential_collection": False,
        "total_events": len(snapshot),
        "simulated_clicks": clicks,
        "events": snapshot,
    })


if __name__ == "__main__":
    # Localhost only by default so the lab is not exposed to the network.
    app.run(host="127.0.0.1", port=5000, debug=False)
