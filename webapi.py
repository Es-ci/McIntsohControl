import socket
import sys
from time import sleep
import tkinter as tk
from tkinter import messagebox
from flask import Flask, request, jsonify
import threading

# Command map for McIntosh controls
COMMAND_MAP = {
    "Power On": "PON Z1",
    "Power Off": "POF Z1",
    "Volume Up": "VUP Z1 5",
    "Volume Down": "VDN Z1 5",
    "Zone 1 On": "OP1 Z1 1",
    "Zone 1 Off": "OP1 Z1 0",
    "Zone 2 On": "OP2 Z1 1",
    "Zone 2 Off": "OP2 Z1 0",
    "Input TV": "INP Z1 12",
    "Input Phono": "INP Z1 8",
    "Input USB": "INP Z1 10",
    "Input Roon": "INP Z1 4",
    "Mute": "MUT Z1 1",
    "Unmute": "MUT Z1 0",
}

def send_command(command):
    host = '192.168.1.99'  # Replace with actual IP
    port = 4999  # Replace with actual port
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            # Wrap command in parentheses as required
            full_command = f"({command})"
            s.sendall(full_command.encode('ascii'))
            response = s.recv(1024)
            try:
                response_text = response.decode('ascii')
            except UnicodeDecodeError:
                response_text = response.hex()
            #messagebox.showinfo("Response", f"Command '{full_command}' sent.\nResponse: {response_text}")
            return response_text
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return str(e)

# Flask app for API
app = Flask(__name__)

@app.route('/mcintosh', methods=['POST'])
def control():
    key = request.json.get('command')  # Now expecting the key name, like "Power On"
    command = COMMAND_MAP.get(key)  # Look up the command in the map
    if command:
        response = send_command(command)  # Send the mapped command
        return jsonify({"status": "success", "command": key, "response": response})
    else:
        return jsonify({"status": "error", "message": "Invalid command key"}), 400


# Start Flask in a separate thread
def start_flask():
    app.run(host="0.0.0.0", port=5001)

# Tkinter UI setup
def start_tkinter():
    root = tk.Tk()
    root.title("McIntosh Control")

    # Create buttons for each command
    for name, command in COMMAND_MAP.items():
        button = tk.Button(root, text=name, command=lambda cmd=command: send_command(cmd))
        button.pack(fill="x", padx=10, pady=5)

    root.mainloop()

# Run both Tkinter and Flask simultaneously
if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()
    start_tkinter()
