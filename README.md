# Phisher Media

**Educational phishing-awareness simulator — Founder: ROOT L00T**

Phisher Media is a deliberately limited cybersecurity training lab. It demonstrates a simulated phishing interaction without collecting credentials or exposing a service to the network.

## Safety boundaries

- Localhost-only by default (`127.0.0.1`).
- No username/password collection.
- No credential storage or transmission.
- Only synthetic training events are recorded.
- Use only on systems and participants you are authorized to test.

## Run on Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser. The JSON report is available at `http://127.0.0.1:5000/report`.

## GitHub publishing

This repository is already published under the connected GitHub account as `root22234/phish22`.

To publish a local clone instead:

```bash
git init
git add .
git commit -m "Initial Phisher Media educational lab"
git branch -M main
git remote add origin https://github.com/root22234/phish22.git
git push -u origin main
```

## License

Choose an appropriate open-source license before distributing the project.
