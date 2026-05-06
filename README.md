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
