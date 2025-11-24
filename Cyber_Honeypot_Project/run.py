
import subprocess

print("Starting Web Honeypot on port 8080...")
subprocess.Popen(["python3", "web_honeypot.py"])

print("Starting SSH Honeypot on port 2222...")
subprocess.Popen(["python3", "ssh_honeypot.py"])

print("Both honeypots running. Logs will be stored in /logs/")
input("Press ENTER to stop...
")
