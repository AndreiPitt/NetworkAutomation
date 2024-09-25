# NetworkAutomation
Overview
The Network Automation Project is a Python-based tool designed to manage and automate the configuration of network devices. It provides a command-line interface (CLI) to interact with devices, configure routers, and manage device connections through a JSON-based device management system. The project focuses on simplifying network automation tasks for administrators.

Features
Device Management: Add, remove, and list devices stored in a JSON file.
Router Configuration: Automate the setup and configuration of routers.
SSH Connection Handling: Establish and manage SSH connections with network devices.
Menu System: Interactive CLI-driven menu for user-friendly operation.
Customizable Devices: Easily add and configure new devices by editing the JSON file.
Scalable Design: Extend functionality by adding new device types and features.

Files
Connection.py: Manages network connections.
Devices.py: Handles device operations via JSON.
Menu.py: CLI interface to interact with the system.
Router.py: Router-specific automation tasks.

Requirements
Python 3.x
Required libraries: paramiko (for SSH connections)

Usage
Clone the repository.
Configure the Devices.json file with your network devices.
Run main.py to start the interactive menu.
