
import os, json, time

def analyze():
    report = {
        "web_requests": 0,
        "ssh_attempts": 0
    }

    if os.path.exists("logs/web_requests.log"):
        with open("logs/web_requests.log") as f:
            report["web_requests"] = len(f.readlines())

    if os.path.exists("logs/ssh_attempts.log"):
        with open("logs/ssh_attempts.log") as f:
            report["ssh_attempts"] = len(f.readlines())

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report generated:", report)

if __name__ == "__main__":
    analyze()
