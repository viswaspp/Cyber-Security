
import requests, random, time
for i in range(50):
    payload = {
        "src_ip": f"192.168.1.{random.randint(2,250)}",
        "dest":"iot-camera",
        "method": random.choice(["GET","POST"]),
        "path": "/"+"/".join(["a"*random.randint(1,10) for _ in range(random.randint(1,5))]),
        "user_agent": "bot-"+str(random.randint(1,1000))
    }
    try:
        r = requests.post("http://localhost:8000/ingest/log", json=payload, timeout=2)
        print(r.json())
    except Exception as e:
        print("error", e)
    time.sleep(0.05)
