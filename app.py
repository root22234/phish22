from flask import Flask, jsonify, render_template_string
from datetime import datetime, timezone
from threading import Lock

app = Flask(__name__)
events = []
lock = Lock()

TEMPLATES = {
    "instagram": ("Instagram", "Your social-media training notification"),
    "facebook": ("Facebook", "Your social-media training notification"),
    "x": ("X", "Your social-media training notification"),
    "linkedin": ("LinkedIn", "Your professional-network training notification"),
    "google": ("Google", "Your account-security training notification"),
    "generic": ("Social Media", "A generic social-media awareness exercise"),
}


def record(event_type, template):
    with lock:
        events.append({
            "event": event_type,
            "template": template,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })


PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Phisher Media — {{ brand }} Training</title>
<style>
body{font-family:system-ui,sans-serif;background:#0b1020;color:#eef2ff;display:grid;place-items:center;min-height:100vh;margin:0}.card{max-width:760px;margin:24px;padding:40px;border:1px solid #38f2b3;border-radius:24px;background:#11182d;box-shadow:0 20px 70px #0008}.badge{display:inline-block;padding:7px 12px;border-radius:999px;background:#15352e;color:#38f2b3;font-weight:700}h1{font-size:42px;margin:18px 0 8px}p{line-height:1.6;color:#b9c3dd}.button{border:0;border-radius:12px;padding:14px 20px;background:#38f2b3;color:#06120e;font-weight:800;cursor:pointer}.notice{margin-top:24px;padding:16px;border-radius:14px;background:#202943}
</style>
</head>
<body><main class="card">
<span class="badge">EDUCATIONAL SIMULATION</span>
<h1>{{ brand }} Awareness Lab</h1>
<p>{{ message }}</p>
<p><b>Important:</b> This is a training page. It does not request or collect passwords, OTPs, cookies, tokens, payment information, or other real credentials.</p>
<button class="button" onclick="simulateClick()">Simulate interaction</button>
<div id="status" class="notice">Ready for an authorized local exercise.</div>
<script>
async function simulateClick(){const r=await fetch('/event/click/{{ slug }}',{method:'POST'});const d=await r.json();document.getElementById('status').textContent=d.message;}
</script>
</main></body></html>
"""


@app.get("/")
def home():
    return render_template_string(PAGE, brand="Phisher Media", message="Choose a training template from the Bash menu.", slug="generic")


@app.get("/simulate/<slug>")
def simulation(slug):
    if slug not in TEMPLATES:
        return jsonify({"error": "unknown training template"}), 404
    brand, message = TEMPLATES[slug]
    record("template_open", slug)
    return render_template_string(PAGE, brand=brand, message=message, slug=slug)


@app.post("/event/click/<slug>")
def click_event(slug):
    if slug not in TEMPLATES:
        return jsonify({"error": "unknown training template"}), 404
    record("simulated_click", slug)
    return jsonify({"ok": True, "message": "Training interaction recorded. No credentials were collected."})


@app.get("/report")
def report():
    with lock:
        snapshot = list(events)
    clicks = sum(e["event"] == "simulated_click" for e in snapshot)
    opens = sum(e["event"] == "template_open" for e in snapshot)
    by_template = {}
    for event in snapshot:
        by_template[event["template"]] = by_template.get(event["template"], 0) + 1
    return jsonify({
        "project": "Phisher Media",
        "founder": "ROOT L00T",
        "purpose": "Educational phishing-awareness simulation",
        "credential_collection": False,
        "template_opens": opens,
        "simulated_clicks": clicks,
        "events_by_template": by_template,
        "events": snapshot,
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
