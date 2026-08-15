# Phisher

**Educational phishing-awareness simulator — Founder: ROOT L00T**

Phisher is a deliberately limited cybersecurity training lab. It demonstrates simulated phishing interactions without collecting credentials or exposing a service to the network.

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

In another terminal:

```bash
chmod +x phisher-media.sh
./phisher-media.sh
```

Open `http://127.0.0.1:5000` for the local training backend. The JSON report is available at `http://127.0.0.1:5000/report`.

## GitHub

Repository: `root22234/phish22`

## License

Choose an appropriate open-source license before distributing the project.
