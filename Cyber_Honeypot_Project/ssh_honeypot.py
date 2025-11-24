
import socket, threading, time, os

HOST = "0.0.0.0"
PORT = 2222
LOG_FILE = "logs/ssh_attempts.log"

os.makedirs("logs", exist_ok=True)

def handle_client(conn, addr):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} | {addr} | SSH connection attempt\n")

    conn.send(b"SSH-2.0-OpenSSH_7.9
")
    time.sleep(1)
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(50)

print("SSH Honeypot running on port", PORT)

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
