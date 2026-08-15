from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)
BACKEND = "http://127.0.0.1:5000"

HTML = """
<!doctype html><html><head><meta charset='utf-8'><title>Phisher Media Dashboard</title>
<style>body{font-family:system-ui;background:#0b1020;color:#eef2ff;margin:0;padding:40px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:18px}.card{background:#11182d;border:1px solid #283553;border-radius:18px;padding:24px}.n{font-size:38px;font-weight:800;color:#38f2b3}</style></head>
<body><h1>Phisher Media — Awareness Dashboard</h1><p>ROOT L00T • Educational lab • No credentials collected</p>
<div class='grid'><div class='card'>Template opens<div class='n'>{{r.template_opens}}</div></div><div class='card'>Simulated clicks<div class='n'>{{r.simulated_clicks}}</div></div><div class='card'>Templates used<div class='n'>{{r.events_by_template|length}}</div></div></div>
<h2>Events by template</h2><pre>{{r.events_by_template}}</pre></body></html>
"""

@app.get("/")
def dashboard():
    try:
        report = requests.get(f"{BACKEND}/report", timeout=2).json()
    except requests.RequestException:
        report = {"template_opens": 0, "simulated_clicks": 0, "events_by_template": {"backend": "not running"}}
    return render_template_string(HTML, r=report)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
