# Nornir-with-Netmiko
Project Overview
This project demonstrates the implementation of a network automation framework using Nornir and Python. The objective was to manage three Cisco IOS routers simultaneously within a simulated environment to perform mass data collection (Interface Status) through SSH.

Technical Stack
  1. Automation Framework: Nornir 3.0
  2. Library: Nornir-Netmiko (for SSH connections)
  3. Simulation: GNS3
  4. Environment: Ubuntu 22.04 LTS (running on VMware)
  5. Devices: 3x Cisco IOS Routers (R1, R2, R3)

Network Topology
  1. The architecture consists of a management workstation (Ubuntu VM) connected to a Layer 2 Ethernet Switch, which provides access to the management       interfaces (FastEthernet 0/0) of all three routers.

<img width="458" height="430" alt="Screenshot 2026-05-06 123918" src="https://github.com/user-attachments/assets/0c768346-8a61-42b7-9947-4e4d70cbf92a">
<br><br>

Inventory Structure
The project follows a decoupled architecture, separating the logic from the data using YAML files:
  1. hosts.yaml: Contains the IP addresses for R1, R2, and R3.
  2. groups.yaml: Defines the ios platform for all Cisco devices.
  3. defaults.yaml: Stores global credentials (username/password).
  4. config.yaml: Configures the Threaded Runner to handle 10 simultaneous workers for parallel execution.

<img width="637" height="73" alt="image" src="https://github.com/user-attachments/assets/6adf1449-63fe-4248-91ca-7545191ad602" />
<br><br>

Main Automation Script (main.py)
The Python script initializes the Nornir object and executes the show ip interface brief command across the entire inventory in parallel.
<img width="585" height="366" alt="image" src="https://github.com/user-attachments/assets/30724abd-275e-4317-a2f1-8644cadb3fc4" />
<br><br>

Results and Validation
The automation was successful. The script successfully bypassed standard Linux SSH security restrictions (obsolete KEX/HostKey algorithms) by using Netmiko's native handling.

Execution Output
Below is the output showing the real-time status of the interfaces for all three routers retrieved in a single execution:
<img width="913" height="376" alt="Screenshot 2026-05-06 123618" src="https://github.com/user-attachments/assets/5056dbe2-e84e-43c6-a981-a70a3e84abbc" />
<br><br>

Author: Jose Armando Martinez Perez
Institution: Instituto Tecnológico de Querétaro (ITQ)
