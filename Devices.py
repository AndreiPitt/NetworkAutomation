import json
import time


class Devices:
    """
    The Devices class manages a list of device objects and updates the list from a JSON file.

    Methods:
        update_devices(): Reads device data from 'devices.json' and updates the devices_list with new device instances.
        test_ping(): Tests network connectivity using ping.
    """
    devices_list = []

    def __init__(self, type_device, name, ip, username, password, priv_password):
        """
        Initializes a device object with its necessary details.
        """
        self.type_device = type_device
        self.name = name
        self.ip = ip
        self.username = username
        self.password = password
        self.priv_password = priv_password

    @classmethod
    def update_devices(cls):
        """
        Reads device data from 'devices.json' and updates the devices_list with new device instances.

        Raises:
            FileNotFoundError: If the 'devices.json' file is not found.
            json.JSONDecodeError: If the JSON data is not formatted correctly.
        """
        try:
            with open("devices.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("The 'devices.json' file was not found.")
        except json.JSONDecodeError:
            print("The JSON data is not formatted correctly.")

        for element in data:
            try:
                Devices.devices_list.append(
                    Devices(element['type'], element['name'], element['ip'], element['username'], element['password'],
                            element['privileged_password']))
            except KeyError as e:
                print(f"Missing key in JSON data: {e}")

    def test_ping(self, connector: object) -> None:
        """
        Tests network connectivity by sending a ping from the switch to another device.
        """
        ip = input("What is the IP address of the device you want to ping? ")
        print(f"Testing ping from device to ip {ip}")
        connector.send_command(f'do ping {ip}\n')
        time.sleep(2)

    def configure_hsrp(self, connector: object) -> None:
        """
        Configure HSRP on the device.
        """
        int_or_vlan = input("Do you want to configure HSRP on switch interface or switch vlan? (vlan/interface)")
        if int_or_vlan == "interface":
            interface = input("Enter the name of the interfaces you want to configure HSRP.")
            ip = input("Enter the ip address: ")
            sm = input("Please enter the subnet mask: ")
            id_standby = input("Enter the standby number: ")
            ip_virtual = input("Enter the ip address of the virtual router: ")

            command = connector.send_command(f'interface {interface}\nno sw\nstandby version 2\nip add {ip} {sm}\n'
                                             f'standby {id_standby} ip {ip_virtual}\n'
                                             f'standby {id_standby} pree\n')
            time.sleep(2)
            priority = input("Do you want to set priority on this interface? (yes/no)")
            if priority == "yes":
                command = connector.send_command(f"standby {id_standby} pri 109")
        if int_or_vlan == "vlan":
            vlan = input("Enter the name of the vlan you want to configure HSRP.")
            ip = input("Enter the ip address: ")
            sm = input("Please enter the subnet mask: ")
            id_standby = input("Enter the standby number: ")
            ip_virtual = input("Enter the ip address of the virtual router: ")

            command = connector.send_command(f'vlan {vlan}\nenc dot {vlan}\nstandby version 2\nip add {ip} {sm}\n'
                                             f'standby {id_standby} ip {ip_virtual}\n'
                                             f'standby {id_standby} pree\n')
            time.sleep(2)
            priority = input("Do you want to set priority on this interface? (yes/no)")
            if priority == "yes":
                command = connector.send_command(f"standby {id_standby} pri 109")
