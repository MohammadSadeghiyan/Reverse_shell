# Reverse Shell Project

This project is a simple implementation of a Reverse Shell, developed as part of a networking course. It consists of a server and a client that connects to the server, receives commands, and executes them.

## Table of Contents
- [Project Description](#project-description)
- [How to Run](#how-to-run)
  - [Prerequisites](#prerequisites)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Project Files](#project-files)
- [Examples](#examples)
  - [Sending Commands](#sending-commands)
  - [Sending Commands to All Clients](#sending-commands-to-all-clients)
- [License](#license)

## Project Description
This project consists of two main components:

1. **Server**: The server waits for client connections, sends commands, and receives results.
2. **Client**: The client connects to the server, executes received commands, and sends results back to the server.

## How to Run

### Prerequisites
- Python 3.x
- Standard Python libraries (`socket`, `subprocess`, `os`, `platform`, `threading`)

### Running the Server
1. Run the `malware_server.py` file:
   ```bash
   python malware_server.py
   ```
   The server will start listening for client connections and display the IP address and port.

### Running the Client
1. Run the `malware_client.py` file:
   ```bash
   python malware_client.py
   ```
   The client will connect to the server and wait to receive commands.

## Project Files
- `malware_server.py`: The server code that sends commands to clients.
- `malware_client.py`: The client code that connects to the server and executes commands.
- `command_process.py`: Contains functions for processing and executing commands.
- `clear_output.py`: Contains functions for clearing the terminal screen and closing processes.
- `launch.json`: Configuration file for debugging the project in VS Code.

## Examples

### Sending Commands
Once the client is connected to the server, you can send commands from the server to the client. For example:

**Change Directory:**
```bash
cd /path/to/directory
```

**List Files:**
```bash
ls
```

**Download a File:**
```bash
DOWNLOAD <file_path> <destination_path>
```

**Upload a File:**
```bash
UPLOAD <file_path> <destination_path>
```

### Sending Commands to All Clients
You can send a command to all connected clients using the `sendall` command:
```bash
sendall <command>
```


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

