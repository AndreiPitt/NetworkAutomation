
# Network Automation Project

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Device Configurations](#device-configurations)
- [Usage](#usage)
  - [Menu System](#menu-system)
- [Code Overview](#code-overview)
  - [Device Management](#device-management)
  - [Router Configuration](#router-configuration)
  - [SSH Connection](#ssh-connection)

---

## Introduction

The **Network Automation Project** is a Python-based tool designed to manage and automate the configuration of network devices. It provides a command-line interface (CLI) to interact with devices, configure routers, and manage device connections through a JSON-based device management system. The project focuses on simplifying network automation tasks for administrators.

---

## Features

- **Device Management**: Add, remove, and list devices stored in a JSON file.
- **Router Configuration**: Automate the setup and configuration of routers.
- **SSH Connection Handling**: Establish and manage SSH connections with network devices.
- **Menu System**: Interactive CLI-driven menu for user-friendly operation.
- **Customizable Devices**: Easily add and configure new devices by editing the JSON file.
- **Scalable Design**: Extend functionality by adding new device types and features.

---

## Project Structure

```
/devices            # Contains classes for managing devices
/router             # Router-specific automation functionality
/menu.py            # Command-line menu for interacting with devices
/connection.py      # Manages network connections, particularly SSH
```

---

## Prerequisites

- Python 3.x
- Required libraries: 
  - `paramiko` for SSH connections

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AndreiPitt/NetworkAutomation.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

### Device Configurations

Devices are managed using a `devices.json` file. Each device should be configured as follows:

```json
{
  "hostname": "router1",
  "ip": "192.168.0.1",
  "username": "admin",
  "password": "admin",
  "type": "router"
  "priv_pass": "class"
}
```

You can add multiple devices to the list, allowing you to manage and automate configuration for all of them.

---

## Usage

Run the tool by executing the `main.py` script:

```bash
python main.py
```

### Menu System

The tool offers an interactive CLI-driven menu that allows you to manage devices and perform configuration tasks:

1. **View Devices**: Displays a list of all devices.
2. **Add a Device**: Allows you to add a new device to the system.
3. **Remove a Device**: Deletes an existing device.
4. **Connect to a Device**: Establishes an SSH connection to a selected device.
5. **Configure a Router**: Automates router-specific tasks (e.g., setting up interfaces, routing).

---

## Code Overview

### Device Management

- **File**: `devices.py`
- **Class**: `Devices`
  
This module manages the list of devices stored in the `devices.json` file. It provides functionality to add, remove, and retrieve devices as needed. It is integrated with the menu system to provide easy device management via the CLI.

### Router Configuration

- **File**: `router.py`
- **Class**: `Router`

The router module automates common router configurations such as interface setup, routing protocols, and basic device settings.

### SSH Connection

- **File**: `connection.py`
- **Class**: `Connection`

This class manages the SSH connections to network devices, leveraging the `paramiko` library to securely execute commands remotely. It establishes the connection, executes commands, and closes the session when done.

---


