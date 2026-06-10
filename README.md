# LAN Chat

A simple real-time chat application for local networks, built with Flask and Socket.IO.

## Overview

LAN Chat allows multiple users on the same local network to communicate in real time through a web browser. Each user is automatically assigned a unique number based on their IP address, so they can return to the same identity after disconnects or page refreshes. The assignment is persisted to disk, making it easy to keep conversations organized without login or accounts.

Who is it for: small teams, classrooms, hackathons, or anyone wanting a quick and private in‑network chat room without internet access.

## Features

- Multi‑user real‑time chat using WebSockets
- Automatic numeric user IDs derived from the client IP address
- Persistent IP‑to‑number mapping stored in a JSON file
- Reconnect support – the same IP always gets the same user number
- Responsive web interface built with Bootstrap 4
- Lightweight and easy to run on any machine with Python

## Tech Stack

- **Backend:** Python 3, Flask, Flask‑SocketIO  
- **Frontend:** HTML/CSS, Bootstrap 4, jQuery, Socket.IO‑client (served by the backend)

## Project Structure

```
.
├── server.py           # Main application (Flask server + Socket.IO events)
├── requirements.txt    # Python dependencies (create manually if missing)
├── templates/          # HTML templates (contains index.html)
└── ip_numbers.json     # Auto‑generated; persists IP‑to‑number mapping
```

*Note: The `templates/` directory and its content are expected to exist alongside `server.py`. The `ip_numbers.json` file is created automatically on the first run.*

## Getting Started

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required packages:

   ```bash
   pip install flask flask-socketio
   ```

   Alternatively, if a `requirements.txt` is present, use:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

The application uses a hard‑coded `SECRET_KEY` in `server.py`. For production use, you should change it to a secure random value.

No other environment variables or configuration files are required.

### Running the Server

Start the server with:

```bash
python server.py
```

The server will listen on **0.0.0.0:5000** (all network interfaces). You should see output similar to:

```
 * Running on http://0.0.0.0:5000/
```

## Usage

1. Ensure the server is running on a machine accessible from your local network.
2. From any device on the same network, open a browser and navigate to:
   ```
   http://<server-ip>:5000
   ```
   (Replace `<server-ip>` with the actual IP address of the server machine.)
3. Each browser window will be assigned a unique number (e.g., `#1`, `#2`) based on the device’s IP. Typing in the message box and pressing Enter sends the message to all connected users.

**Note:** If a user disconnects and reconnects from the same IP address, they will retain the same number.

## How It Works

- On first connection, the server records the client’s IP and assigns the next available integer.
- The mapping is saved to `ip_numbers.json` so it survives server restarts.
- Incoming messages are prefixed with the sender’s number and broadcast to all connected clients.

## Scripts / Commands

There is no additional command‑line interface. The main script is:

| Command           | Description                                    |
|-------------------|------------------------------------------------|
| `python server.py`| Start the Flask‑SocketIO development server    |

## Testing

No automated tests are present in the repository. Manual testing can be performed by opening multiple browser tabs or using different devices on the same network.

## Build / Deployment

This project is intended for local or development use. For production deployment you may:

- Use a production‑grade WSGI server (e.g., Gunicorn with eventlet) instead of the Flask development server.
- Set `debug=False` in `socketio.run()`.
- Place the application behind a reverse proxy (e.g., Nginx) if needed.

No Dockerfile or CI/CD configuration is provided.

## API Reference

The application communicates exclusively through WebSocket events:

| Event      | Direction       | Data                    | Description                              |
|------------|----------------|-------------------------|------------------------------------------|
| `connect`  | Client → Server | (automatic)             | Server assigns a user number             |
| `message`  | Client → Server | String (raw message)    | User sends a chat message                |
| `response` | Server → Client | String (`#<number>: <message>`) | Broadcast of a message with sender’s ID  |
| `disconnect`| Client → Server | (automatic)             | Server removes the client from the list  |

## Examples

Once the server is running, type a message in the web interface. All connected clients will see:

```
#1: Hello everyone!
```

If another user on a different IP joins, their messages appear as:

```
#2: Hi, how are you?
```

Reconnections from the same IP will resume with the original number.

## Roadmap

No planned features are documented in the repository. Potential improvements could include:

- Chat rooms or channels
- Usernames instead of numeric IDs
- Message history
- HTTPS support

## Contributing

Contributions are welcome. Please open an issue to discuss changes before submitting a pull request. Ensure that any modifications keep the project simple and consistent with the original design.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.